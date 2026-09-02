# -*- coding: utf-8 -*-
"""
Gerador de PDF de PEÇA GFES: markdown -> HTML -> PDF (Chrome headless).
Uso:  python3 gerar_pdf.py "/caminho/da/peca.md"   (gera peca.pdf ao lado)
      python3 gerar_pdf.py "peca.md" --sem-validacao  (pula o gate de norma culta)

GATE (05/06/2026): antes de gerar, roda scripts/validar_norma_culta.py sobre o corpo
(sem frontmatter, igual ao que vira PDF). Se houver ERRO (AO 1990 / vazamento / IA),
ABORTA e não gera o PDF — corrija ou use --sem-validacao.

Padrão = REGRA CANÔNICA DE TIPOGRAFIA de 14/08/2026 (método Tipografia Jurídica —
references/tipografia-pecas-2026-08-14.md; revoga o padrão Times/1,5 de 03/06/2026).
Histórico (03/06/2026):
- **Times New Roman 12** (corpo e títulos); A4; margens 3 (sup) / 2 (inf) / 3 (esq) / 2 (dir) cm;
  entrelinha 1,5; corpo justificado; recuo de 1ª linha 1,25 cm.
- SEM logomarca e SEM rodapé de endereço.
- Vocativo CENTRALIZADO; qualificação à ESQUERDA (Processo n.:/Juízo/Apelante…);
  título da peça CENTRALIZADO em negrito; seções (I —, II —) à ESQUERDA em negrito;
  data + assinatura CENTRALIZADAS.
- Frontmatter YAML removido (não vaza).

Marcação no .md:
  `@@ texto`  -> linha CENTRALIZADA (vocativo, título, data, assinatura)
  `# texto`   -> seção (negrito, esquerda, maiúsculas)
  `## texto`  -> subseção (negrito, esquerda)
  `### texto` -> sub-subseção (negrito itálico, esquerda)
  `- texto`   -> item de lista
  `**Rótulo:** ...` no início da linha -> qualificação (sem recuo, esquerda)
  demais linhas -> parágrafo justificado com recuo de 1ª linha
ADENDO 02/09/2026 (adoção dos 14 itens da reanálise dos cursos):
  `@numerar`                         -> liga a numeração automática de seções (I —, I.1 —)
  `> [!requerimentos] Rótulo` + `> [x] …`/`> [ ] …` -> quadro de requerimentos com caixas
  `[provatrio] a | b | c | rótulos ; separados | legenda` -> série de três imagens
  `[provaquadro] doc.png | rótulo | legenda` + linhas `- Campo: teor (coord.)` -> quadro de apoio
  títulos `#` e vocativo `@@` em CAIXA ALTA -> caixa mista em VERSALETE (sintetizado)
  o par `[provapar]` ganha seta entre a página e o zoom
"""
import re, html, sys, os, subprocess, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from metadados_pdf import limpar_metadados, titulo_de_arquivo

CHROME = os.environ.get("GFES_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

CSS = """
/* MARGENS — laterais pela Masterclass (aula 2, transcrita em 27/08/2026): são elas que
   definem o comprimento da linha, "em regra não menos de 5 cm no total lateral"; o
   professor usa 3 + 3.
   VERTICAIS (ordem do Dr. Gabriel, 27/08/2026): *"um espaço entre o final da folha e o
   início da outra está ficando muito espaço em branco"*. Medido: 6,42 cm em média entre
   o último texto de uma folha e o primeiro da seguinte — 22 % de uma folha inteira.
   A aula é clara em que a margem superior/inferior "depende do que você vai colocar no
   cabeçalho e no rodapé": a PEÇA FORENSE da casa não tem timbre nem rodapé, logo 3 cm no
   topo era branco herdado de documento timbrado. Passa a 2,3 sup / 1,8 inf.
   ⚠️ Não descer mais: o eproc carimba a TARJA do processo na faixa superior do PDF, e a
   margem tem de sobrar para ela sem cobrir texto. */
@page { size: A4; margin: 2.3cm 3cm 1.8cm 3cm; }
* { box-sizing: border-box; }
/* 27/08/2026 — piso global de viuva/orfa, herdado por todo bloco de texto. */
body, div, li, td { orphans: 2; widows: 2; }
/* ENTRELINHA — mesma aula: "fuja daquele entrelinhamento de 1,5, é muito entrelinhamento
   para a maioria das fontes... o teu olho é seu amigo". Times New Roman 12 em linha de
   15 cm assenta em 1,35 (o professor usa 1,15–1,2 numa fonte de altura-x maior). */
body { font-family: 'Times New Roman', Times, serif; font-size: 12pt;
       line-height: 1.35; text-align: justify; color:#000; margin:0;
       hyphens: auto; -webkit-hyphens: auto; }
h1.sec { font-size: 12pt; font-weight: bold; text-align:left; text-indent:0; margin: 18pt 0 10pt 0;
         color:#1F3864; border-bottom: 0.6pt solid #B8C4D4; padding-bottom: 2pt;
         /* 27/08/2026 — regra de viuva/orfa: titulo nunca fica no pe da pagina */
         page-break-after: avoid; break-after: avoid;
         page-break-inside: avoid; break-inside: avoid; }
h2.sub { font-size: 12pt; font-weight: bold; text-align:left; text-indent:0; margin: 15pt 0 8pt 0;
         color:#2E5077;
         /* 27/08/2026 — regra de viuva/orfa: titulo nunca fica no pe da pagina */
         page-break-after: avoid; break-after: avoid;
         page-break-inside: avoid; break-inside: avoid; }
h3.subsub { font-size: 12pt; font-weight: bold; font-style: italic; text-align:left;
           text-indent:0; margin: 13pt 0 7pt 0;
           page-break-after: avoid; break-after: avoid;
           page-break-inside: avoid; break-inside: avoid; }
/* 27/08/2026 — ordem do Gabriel: em petição não pode haver linha órfã nem página em branco.
   orphans = mínimo de linhas que ficam no PÉ da página; widows = mínimo que passa para a
   página seguinte. Valor 2/2 medido no Chrome headless em 27/08/2026: com 3/3 o parágrafo
   de 4 ou 5 linhas torna a restrição impossível (3+3 > 4) e o Chrome DESCARTA a widow,
   produzindo exatamente a linha solta no topo que a regra proíbe. Com 2/2 nenhuma quebra
   observada deixou linha sozinha. */
p { text-indent: 2cm; margin: 0; orphans: 2; widows: 2; }
/* CITAÇÃO EM BLOCO — Masterclass, aula 2: "não precisa ser de 4 centímetros; quanto maior
   o recuo, menor a coluna, mais problema de formatação a gente vai ter" (o professor usa
   3 cm). As ÚNICAS marcas da citação são recuo à esquerda e fonte menor — nunca itálico,
   porque o itálico é da citação direta no corpo do texto, não da citação em bloco. */
p.cit { font-family: Charter, 'Bitstream Charter', Georgia, serif; font-size: 11pt; line-height: 1.3;
        margin: 10pt 0 10pt 3cm; text-indent: 0; orphans: 2; widows: 2; }
/* PARÁGRAFO CURTO — 27/08/2026. Medição no Chrome headless: orphans/widows só são
   respeitados quando o parágrafo tem linhas suficientes para satisfazer os dois limites
   (2+2). Num parágrafo de 3 linhas a restrição é impossível e o Chrome quebra 2+1,
   deixando a linha sozinha no topo. Parágrafo curto, portanto, não se quebra: ou cabe,
   ou vai inteiro para a página seguinte. */
p.curto, li.curto { page-break-inside: avoid; break-inside: avoid; }
/* FECHO — "Nestes termos", data e assinatura nunca abrem página sozinhos: colam-se ao
   texto que os precede (regra de viúva/órfã, 24/08/2026, seção 7). */
p.fecho { page-break-before: avoid; break-before: avoid;
          page-break-after: avoid; break-after: avoid; }
/* Os cinco últimos blocos antes da assinatura descem com ela (classe posta pelo gerador),
   para que a última página nunca nasça só com fecho e assinatura. */
.colanofecho { page-break-after: avoid; break-after: avoid;
               /* e não se parte no meio: alínea cortada ao meio na última folha
                  conta como uma linha só e mantém a página abaixo do mínimo. */
               page-break-inside: avoid; break-inside: avoid; }
/* 27/08/2026 — TÍTULO NO PÉ DA PÁGINA. `break-after: avoid` no título não basta: se o
   parágrafo seguinte não couber inteiro (orphans/widows), o Chrome manda só ele para a
   folha nova e o título fica órfão no pé. O gerador passa a envolver o título E o primeiro
   parágrafo da seção num bloco indivisível — os dois viajam juntos. */
.secjunta { page-break-inside: avoid; break-inside: avoid; }
/* 27/08/2026 (vista) — o RÓTULO da janela nunca se separa do seu conteúdo, e a primeira
   linha do quadro não abre página sozinha: quadro que quebra tem de quebrar no MEIO da
   tabela, nunca entre o título e ela. */
.jan .jrot { page-break-after: avoid; break-after: avoid; }
.jan table.q { page-break-before: avoid; break-before: avoid; }
table.q thead { page-break-after: avoid; break-after: avoid; }
/* 27/08/2026 (vista, defeito visto DUAS vezes — pp. 4→5 e 8→9 da defesa 5013466): nas
   janelas de CITAÇÃO, DOUTRINA e JURISPRUDÊNCIA o rótulo vai ABAIXO (order:2) e é a
   ETIQUETA DE FONTE. Nelas a regra acima é a errada: a fonte não pode abrir página
   sozinha, deixando na folha anterior a moldura vazia e o trecho sem credencial.
   Aqui o avoid é ANTES, e o último parágrafo desce com ela. */
.jan.cita .jrot, .jan.dout .jrot, .jan.jur .jrot {
  page-break-after: auto; break-after: auto;
  page-break-before: avoid; break-before: avoid; }
/* ...e para que a fonte tenha COM QUEM descer sem arrastar a janela inteira (vão de
   27,7 % medido na p.8 quando o parágrafo era indivisível), a citação longa quebra
   entre LINHAS, com o mínimo de duas de cada lado. O que não pode partir é a linha. */
.jan.longa.cita > p, .jan.longa.dout > p, .jan.longa.jur > p {
  page-break-inside: auto; break-inside: auto; orphans: 2; widows: 2; }
p.center { text-align:center; text-indent:0; margin: 0;
           /* 27/08/2026 (ordem do Dr. Gabriel): o endereçamento ao juízo NUNCA se
              separa. Sem hifenização e sem quebra dentro de palavra. */
           hyphens: none; -webkit-hyphens: none; overflow-wrap: normal;
           word-break: keep-all; }
/* ASSINATURA CANÔNICA — marca registrada do advogado (ordem do Dr. Gabriel, 27/08/2026).
   Sempre nome inteiro, "Advogado" abaixo e a OAB abaixo, centralizados, com dois espaços
   de respiro acima para não se misturar ao texto final. Escreve-se `@assinatura` no .md. */
.assin { margin: 26pt 0 0 0; text-align: center;
         page-break-inside: avoid; break-inside: avoid;
         page-break-before: avoid; break-before: avoid; }
.assin p { text-indent: 0; margin: 0; text-align: center; line-height: 1.35; }
.assin-nome  { font-size: 12pt; }
.assin-cargo { font-size: 12pt; }
.assin-oab   { font-size: 12pt; }
p.flush  { text-indent:0; margin:0; }
ul { margin: 0; padding-left: 2cm; }   /* mesmo eixo do recuo de 1ª linha */
li { margin: 0 0 2pt 0; text-align: justify; }
strong { font-weight: bold; }
.sp { height: 0.5cm; }
/* Respiro entre o endereçamento ao juízo e a qualificação: QUATRO linhas
   (ordem do Dr. Gabriel, 27/08/2026). 4 x 18pt = 72pt. */
.vocgap { height: 72pt; }

/* ═══ VÃO NO PÉ DA PÁGINA — ordem do Dr. Gabriel, 27/08/2026 ═══════════════════════════
   "final de algumas páginas continua um espaço em branco, quase quarenta por cento".
   CAUSA: bloco alto e INDIVISÍVEL (`break-inside: avoid`) que não cabe no resto da folha
   é empurrado inteiro para a página seguinte — e o buraco fica. Agrava quando um título
   com `break-after: avoid` gruda nesse bloco: os dois viram uma peça só.
   REGRA: o que não pode partir é a LINHA (parágrafo, marco da linha do tempo, linha da
   tabela) — nunca o bloco inteiro. Bloco marcado `.longa` pelo gerador quebra entre
   páginas, como faz qualquer tabela longa de livro.
   ═════════════════════════════════════════════════════════════════════════════════════ */
.jan.longa       { page-break-inside: auto;  break-inside: auto; }
.jan.longa > p,
.jan.longa li    { page-break-inside: avoid; break-inside: avoid; }
table.q.longa    { page-break-inside: auto;  break-inside: auto; }
table.q.longa thead { display: table-header-group; }
table.q tr       { page-break-inside: avoid; break-inside: avoid; }
ul.tl.longa      { page-break-inside: auto;  break-inside: auto; }
/* ...mas MARCO ÓRFÃO é o mesmo defeito de outro nome: um único marco sozinho no topo da
   folha seguinte (ou no pé da anterior) é linha solta. O último marco não abre página e o
   primeiro não fecha página — assim a quebra deixa no mínimo dois de cada lado.
   Vista da p.5 em 27/08/2026: "20/03/2026 — Expedido o edital" havia ficado sozinho. */
ul.tl.longa li:last-child  { page-break-before: avoid; break-before: avoid; }
ul.tl.longa li:first-child { page-break-after: avoid;  break-after: avoid; }
.jan.longa > p:last-child  { page-break-before: avoid; break-before: avoid; }
.jan.longa > p:first-child { page-break-after: avoid;  break-after: avoid; }

/* Quadro sóbrio — elemento visual com função (regra de 14/08/2026) */
table.q { width:100%; border-collapse: collapse; margin: 10pt 0 12pt 0;
          font-size: 11pt; line-height: 1.3; page-break-inside: avoid; }
table.q caption { caption-side: top; text-align:left; font-weight:bold; font-size:11pt;
                  color:#1F3864; padding: 0 0 4pt 0; }
table.q th { background:#EDF0F5; color:#1F3864; font-weight:bold; text-align:left;
             border: 0.6pt solid #B8C4D4; padding: 4pt 6pt; }
table.q td { border: 0.6pt solid #D5DCE6; padding: 4pt 6pt; text-align:left; vertical-align: top; }
/* 27/08/2026 — quadro DENTRO de janela é mais compacto: a janela já lhe dá moldura e
   respiro. Compactar aqui é o que faz o bloco caber na folha em vez de ser empurrado
   inteiro e abrir vão no pé da página anterior. */
.jan table.q th, .jan table.q td { padding: 2.5pt 6pt; }
.jan table.q { line-height: 1.22; }
/* a linha de TOTAL nunca abre página sozinha, separada das rubricas que a compõem */
table.q tr.tot { page-break-before: avoid; break-before: avoid; }
table.q tr.tot td { background:#F5F7FA; font-weight:bold; }
table.q td.num, table.q th.num { text-align:right; white-space:nowrap; }

/* JANELAS SUSPENSAS DA PEÇA (padrão canônico 26/08/2026 — ordem do Dr. Gabriel).
   Cores discretas, sóbrias, próprias do Judiciário: sem saturação, sem "marca-texto".
   Servem para: qualificação da parte, citação, linha do tempo e cálculo. */
.jan { border: 0.6pt solid; border-left-width: 3pt; border-radius: 2pt;
       padding: 7pt 10pt 6pt 10pt; margin: 10pt 0 12pt 0; text-align: justify;
       page-break-inside: avoid; text-indent: 0; }
.jan p { text-indent: 0; margin: 0 0 4pt 0; }
.jan p:last-child { margin: 0; }
.jan .jrot { display:block; font-size: 10pt; font-weight: bold; letter-spacing: 0.3pt;
             text-transform: uppercase; margin: 0 0 4pt 0; }
/* qualificação da parte — azul-ardósia do escritório, muito claro.
   Alinhada no MESMO recuo da citação (ordem do Dr. Gabriel, 26/08/2026). */
.jan.qualif { background:#F4F6FA; border-color:#C3CDDE; border-left-color:#1F3864;
              margin-left: 2.55cm;   /* + padding 10pt + borda 3pt = 3,00 cm de recuo do texto */ }
.jan.qualif .jrot { color:#1F3864; }
/* citação (dispositivo, documento dos autos) — cinza-pergaminho neutro; mantém o recuo.
   Na citação o rótulo vai ABAIXO, como ETIQUETA de fonte (ordem do Dr. Gabriel, 26/08/2026):
   identifica de onde saiu o trecho, no mesmo registro visual das etiquetas das provas. */
.jan.cita { background:#F7F7F4; border-color:#DCDCD4; border-left-color:#6E6E62;
            margin-left: 2.55cm;   /* + padding 10pt + borda 3pt = 3,00 cm de recuo do texto */ font-family: Charter, 'Bitstream Charter', Georgia, serif;
            font-size: 11pt; display: flex; flex-direction: column; }
.jan.cita .jrot { order: 2; align-self: flex-end; margin: 5pt 0 0 0;
                  font-size: 8.5pt; font-weight: bold; text-transform: none;
                  color: #1F3864; background: #EDF1F7; border: 0.5pt solid #C3CDDE;
                  border-radius: 2pt; padding: 2pt 6pt; letter-spacing: 0.2pt; }
/* linha do tempo — mesma família do quadro sóbrio */
.jan.tempo { background:#F5F7FA; border-color:#CBD4E0; border-left-color:#2E5077; }
.jan.tempo .jrot { color:#2E5077; }
.jan.tempo ul.tl { margin: 2pt 0 0 0; }

/* PROVA RECORTADA — recorte do documento dos autos, com seta apontando o ponto discutido
   (ordem do Dr. Gabriel, 26/08/2026). O documento entra na peça pelos olhos do julgador. */
figure.prova { margin: 10pt 0 12pt 0; padding: 0; text-align: center;
               page-break-inside: avoid; }
/* Borda + sombra externa (Intensivo Printscreens, aula 4, transcrita em 27/08/2026):
   "toda imagem branca precisa de uma borda, senão fica muito ruim" — e a sombra externa
   de deslocamento inferior direito é sóbria e recorta o documento do fundo da página.
   Nada de moldura decorativa do editor: o professor as classifica como cafonas. */
figure.prova img { max-width: 100%; height: auto; border: 0.6pt solid #B8B8B0;
                   box-shadow: 2pt 2pt 3pt rgba(0,0,0,0.18); }
figure.prova figcaption { font-size: 9pt; line-height: 1.3; color: #3A3A34;
                          text-align: left; text-indent: 0; margin: 4pt 0 0 0; }
figure.prova figcaption .fig { font-weight: bold; color: #1F3864; }

/* PROVA EM PAR — a PÁGINA INTEIRA do documento à ESQUERDA e o trecho DESTACADO à DIREITA,
   na mesma folha (ordem do Dr. Gabriel, 26/08/2026): o julgador vê a origem e o detalhe. */
/* 27/08/2026 — espaçamento do BLOCO de figura (não é tipografia de texto): 10/12pt
   deixavam o par a 0,3 cm de caber na folha, e o gate de paginação reprovava por
   subocupação. 6/8pt mantêm o respiro e fecham o buraco. */
figure.provapar { margin: 4pt 0 6pt 0; padding: 0; page-break-inside: avoid; }
figure.provapar .par { display: flex; align-items: center; gap: 11pt; }
figure.provapar .lado { text-align: center; }
/* 27/08/2026 — a PÁGINA INTEIRA apenas SITUA ("o documento todo serve para mostrar que o
   documento existe"); quem se lê é o ZOOM. Dando 38% da largura a uma página vertical,
   era ela que ditava a altura do bloco e espremia o zoom. Com 30%, o zoom ganha largura
   e altura — mais legível, e o bloco fica mais baixo. (Intensivo Printscreens, aula 7.) */
figure.provapar .pag { flex: 0 0 24%; }
figure.provapar .amp { flex: 1 1 auto; }
/* ALTURA MÁXIMA — Intensivo Printscreens, aula 3 (transcrita em 27/08/2026): "se eu
   aumento esse print screen, olha o que acontece: ele joga para baixo e a minha peça fica
   uma bagunça… quando a gente está falando de prints verticais, a gente vai preferir
   REDUZIR esses print screens". Imagem não quebra entre páginas; se for alta demais, é ela
   que abre o vão. Teto de 7 cm por lado: o par inteiro (etiquetas + imagens + legenda)
   cabe em ~10 cm, menos da metade da mancha de 24,7 cm. */
figure.provapar img { max-width: 100%; max-height: 7.4cm; width: auto; height: auto;
                      border: 0.6pt solid #B8B8B0;
                      box-shadow: 2pt 2pt 3pt rgba(0,0,0,0.18); }
/* etiqueta azul de discriminação, acima de cada lado */
figure.provapar .rot { display: block; font-size: 8.5pt; font-weight: bold; color: #1F3864;
                       background: #EDF1F7; border: 0.5pt solid #C3CDDE; border-radius: 2pt;
                       padding: 2pt 5pt; margin: 0 0 3pt 0; text-align: center;
                       letter-spacing: 0.2pt; line-height: 1.2; }
figure.provapar figcaption { font-size: 9pt; line-height: 1.3; color: #3A3A34;
                             text-align: left; text-indent: 0; margin: 5pt 0 0 0; }
figure.provapar figcaption .fig { font-weight: bold; color: #1F3864; }

/* EIXO DO TEMPO — linha horizontal com seta (esquerda -> direita) e cortes verticais
   marcando cada momento (ordem do Dr. Gabriel, 26/08/2026). */
.eixo { position: relative; margin: 12pt 0 2pt 0; padding-top: 2pt;
        page-break-inside: avoid; }
.eixo .trilho { position: relative; height: 0; border-top: 1.1pt solid #2E5077;
                margin: 0 14pt 0 2pt; }
/* ponta de seta no fim do trilho */
.eixo .trilho::after { content: ""; position: absolute; right: -12pt; top: -4.2pt;
                       border-left: 9pt solid #2E5077;
                       border-top: 4.2pt solid transparent;
                       border-bottom: 4.2pt solid transparent; }
.eixo .marcos { display: flex; width: 100%; margin: 0; padding: 0 14pt 0 2pt; }
.eixo .mk { flex: 1 1 0; position: relative; padding: 0 4pt 0 0; text-align: left;
            text-indent: 0; }
/* corte vertical que marca o tempo */
.eixo .mk::before { content: ""; position: absolute; left: 0; top: -7pt;
                    width: 0; height: 9pt; border-left: 1.1pt solid #2E5077; }
.eixo .mk .dt { display: block; font-weight: bold; font-size: 9.5pt; color: #1F3864;
                margin: 3pt 0 1pt 0; line-height: 1.15; }
.eixo .mk .tx { display: block; font-size: 9pt; line-height: 1.25; color: #1a1a1a;
                text-align: left; hyphens: auto; }
.eixo .mk.mark .dt { color: #8C2B2B; }
.eixo .mk.mark::before { border-left-color: #8C2B2B; border-left-width: 1.6pt; }
/* DOUTRINA — poucas linhas, quando a tese se apoia em lição doutrinária (26/08/2026).
   Verde-oliva dessaturado: distingue-se da citação de documento sem competir com ela. */
.jan.dout { background:#F4F7F1; border-color:#CDD9C4; border-left-color:#4A6B3A;
            margin-left: 2.55cm;   /* + padding 10pt + borda 3pt = 3,00 cm de recuo do texto */ font-family: Charter, 'Bitstream Charter', Georgia, serif;
            font-size: 11pt; display: flex; flex-direction: column; }
/* A etiqueta é FAIXA DE LARGURA TOTAL: cabe a referência completa, que existe para o julgador
   CONFERIR a fonte (lição do Dr. Gabriel, de quando foi assessor de juiz — 26/08/2026). */
.jan.dout .jrot { order: 2; align-self: stretch; margin: 6pt 0 0 0;
                  font-size: 8.5pt; font-weight: normal; text-transform: none;
                  text-align: left; line-height: 1.3;
                  color: #3B5730; background: #EDF3E8; border: 0.5pt solid #CDD9C4;
                  border-radius: 2pt; padding: 3pt 7pt; letter-spacing: 0; }
.jan.dout .jrot::before { content: "Fonte: "; font-weight: bold; }
/* SÚMULA / JURISPRUDÊNCIA — enunciado com a REFERÊNCIA COMPLETA na etiqueta, de modo que
   quem lê ache o julgado direto (exigência do Dr. Gabriel, 26/08/2026). */
.jan.jur { background:#F7F4F9; border-color:#DACFE2; border-left-color:#5B4576;
           margin-left: 2.55cm;   /* + padding 10pt + borda 3pt = 3,00 cm de recuo do texto */ font-family: Charter, 'Bitstream Charter', Georgia, serif;
           font-size: 11pt; display: flex; flex-direction: column; }
.jan.jur .jrot { order: 2; align-self: stretch; margin: 6pt 0 0 0;
                 font-size: 8.5pt; font-weight: normal; text-transform: none;
                 text-align: left; line-height: 1.3;
                 color: #4A3663; background: #F1EBF5; border: 0.5pt solid #DACFE2;
                 border-radius: 2pt; padding: 3pt 7pt; letter-spacing: 0; }
.jan.jur .jrot::before { content: "Fonte: "; font-weight: bold; }
/* poderes / objeto — núcleo do instrumento (procuração, contrato) */
.jan.poderes { background:#F5F7FA; border-color:#CBD4E0; border-left-color:#2E5077; }
.jan.poderes .jrot { color:#2E5077; }
/* cálculo — creme sóbrio, distingue número de texto sem gritar */
.jan.calc { background:#FAF7F0; border-color:#E2D9C4; border-left-color:#8C7340; }
.jan.calc .jrot { color:#6E5A2E; }
.jan.calc table.q { margin: 2pt 0 0 0; }

/* Linha do tempo */
ul.tl { list-style:none; margin: 8pt 0 12pt 0; padding-left: 1.2cm; }
ul.tl li { position:relative; margin: 0 0 6pt 0; text-align:left; line-height:1.35;
           padding-left: 0.5cm; border-left: 1.2pt solid #B8C4D4; page-break-inside: avoid; }
ul.tl li .dt { display:inline-block; font-weight:bold; color:#1F3864; min-width:3.1cm; }
ul.tl li.mark { border-left-color:#1F3864; }
ul.tl li.mark .dt { color:#8C2B2B; }

/* ═══ ADENDO 02/09/2026 — adoção dos 14 itens da reanálise dos dois cursos (ordem do
   Gabriel: "adote os 14 itens"). Cada bloco cita o item do arquivo 02-auditoria-de-lacunas.
   ═══════════════════════════════════════════════════════════════════════════════════ */
/* 3.1 VERSALETE nos títulos de seção e no cabeçalho da peça (vocativo e título), como a
   Masterclass faz (aula 2: título em versalete; capa com qualificação em versalete). Times
   não tem versalete nativo: o Chrome sintetiza (capitais a ~70 %). O gerador converte
   caixa-alta em caixa mista antes de aplicar, porque versalete sobre CAIXA ALTA não faz
   nada. Caixa-alta no CORPO continua proibida. Corpo do título permanece 12 (item 3.6). */
h1.sec, p.center.voc { font-variant: small-caps; letter-spacing: 0.5pt; }
/* 3.5 NUMERAÇÃO AUTOMÁTICA de seções — ligada pela diretiva `@numerar` no .md: seções em
   romanos ("I —"), subseções "I.1 —". Título que já começa numerado não recebe contador. */
body { counter-reset: sec; }
h1.sec.num { counter-increment: sec; counter-reset: sub; }
h1.sec.num::before { content: counter(sec, upper-roman) " — "; }
h2.sub.num { counter-increment: sub; }
h2.sub.num::before { content: counter(sec, upper-roman) "." counter(sub) " — "; }
/* 3.2 QUADRO DE REQUERIMENTOS PRELIMINARES — na capa, logo abaixo da SÍNTESE (modelo de
   inicial do curso, com caixas de seleção). Caixa desenhada em CSS, sem depender de glifo. */
.jan.req { background:#F4F6FA; border-color:#C3CDDE; border-left-color:#1F3864; }
.jan.req .jrot { color:#1F3864; }
ul.req { list-style:none; margin:0; padding:0; columns: 2; column-gap: 14pt; }
ul.req li { text-align:left; text-indent:0; margin:0 0 3pt 0; break-inside: avoid;
            padding-left: 15pt; position: relative; font-size: 11pt; line-height: 1.3; }
ul.req li .cx { position:absolute; left:0; top:2.2pt; width:9pt; height:9pt;
                border:0.8pt solid #1F3864; border-radius:1pt; background:#fff; }
ul.req li.on .cx::after { content:""; position:absolute; left:2.6pt; top:0.2pt; width:2.4pt;
                height:5pt; border:solid #1F3864; border-width:0 1.4pt 1.4pt 0;
                transform: rotate(45deg); }
ul.req li.off { color:#5A5A5A; }
/* 3.10 SETA entre a página inteira e o zoom no par de prova (o "efeito de ampliação" das
   aulas 5 e 7 do Intensivo). Fina e cinza: aponta, não chama atenção para si. */
figure.provapar .seta, figure.provaquadro .seta { flex: 0 0 14pt; position: relative; height: 0;
     border-top: 1pt solid #8A8A82; }
figure.provapar .seta::after, figure.provaquadro .seta::after { content:""; position:absolute;
     right:-1pt; top:-3.5pt; border-left: 6pt solid #8A8A82;
     border-top: 3.5pt solid transparent; border-bottom: 3.5pt solid transparent; }
/* 3.8 SÉRIE DE TRÊS IMAGENS com legenda única (Intensivo, aula 6: três fotos ou prints
   em datas distintas provam mais que duas páginas de conversa). */
figure.provatrio { margin: 4pt 0 6pt 0; padding: 0; page-break-inside: avoid; }
figure.provatrio .tri { display:flex; gap: 8pt; align-items:flex-start; }
figure.provatrio .tri > div { flex: 1 1 0; text-align:center; }
figure.provatrio img { max-width:100%; max-height: 7.4cm; width:auto; height:auto;
     border: 0.6pt solid #B8B8B0; box-shadow: 2pt 2pt 3pt rgba(0,0,0,0.18); }
figure.provatrio .rot { display:block; font-size:8.5pt; font-weight:bold; color:#1F3864;
     background:#EDF1F7; border:0.5pt solid #C3CDDE; border-radius:2pt; padding:2pt 5pt;
     margin:0 0 3pt 0; letter-spacing:0.2pt; line-height:1.2; }
figure.provatrio figcaption { font-size:9pt; line-height:1.3; color:#3A3A34; text-align:left;
     text-indent:0; margin:5pt 0 0 0; }
figure.provatrio figcaption .fig { font-weight:bold; color:#1F3864; }
/* 3.9 QUADRO DE APOIO ao lado do documento reduzido (Intensivo, aula 5 — "a técnica mais
   forte"): à esquerda o documento com borda e sombra, seta, e à direita a tabela com os
   campos que o julgador procura. Cada valor leva coordenada (regra do portador): dado ao
   lado do print é lido como verdadeiro pelo assessor, e dado falso ali é má-fé (CPC 80, II). */
figure.provaquadro { margin: 4pt 0 6pt 0; padding: 0; page-break-inside: avoid; }
figure.provaquadro .par { display:flex; gap: 11pt; align-items:center; }
figure.provaquadro .doc { flex: 0 0 34%; text-align:center; }
figure.provaquadro .doc img { max-width:100%; max-height:8.2cm; width:auto; height:auto;
     border:0.6pt solid #B8B8B0; box-shadow: 2pt 2pt 3pt rgba(0,0,0,0.18); }
figure.provaquadro .doc .rot { display:block; font-size:8.5pt; font-weight:bold; color:#1F3864;
     background:#EDF1F7; border:0.5pt solid #C3CDDE; border-radius:2pt; padding:2pt 5pt;
     margin:0 0 3pt 0; letter-spacing:0.2pt; line-height:1.2; }
figure.provaquadro .campos { flex: 1 1 auto; }
figure.provaquadro table.q { margin:0; font-size:10.5pt; page-break-inside: avoid; }
figure.provaquadro table.q th { background:#1F3864; color:#fff; border-color:#1F3864; }
figure.provaquadro table.q td:first-child { font-weight:bold; color:#1F3864; white-space:nowrap; }
figure.provaquadro figcaption { font-size:9pt; line-height:1.3; color:#3A3A34; text-align:left;
     text-indent:0; margin:5pt 0 0 0; }
figure.provaquadro figcaption .fig { font-weight:bold; color:#1F3864; }
"""

# Limite de "parágrafo curto" (27/08/2026): a linha do corpo comporta ~85 caracteres
# (Times New Roman 12 em coluna de 15 cm, medido no PDF). Três linhas, descontado o
# recuo de 2 cm da primeira, cabem em ~245 caracteres; usa-se 265 por folga, porque
# marcar um parágrafo de 4 linhas como indivisível é inofensivo (ele apenas migra
# inteiro), ao passo que deixar um de 3 linhas divisível reintroduz a linha órfã.
LIMITE_CURTO = 265

def curto(txt):
    """Texto visível do parágrafo, sem marcação, curto o bastante para não se quebrar."""
    t = re.sub(r"\*\*|\*|`", "", txt.strip())
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return len(t) <= LIMITE_CURTO


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s

def _celulas(s):
    return [c.strip() for c in s.strip().strip("|").split("|")]

def _num(c):
    return " class='num'" if re.match(r"^\*?\*?(R\$\s*)?[\d.,%()+\-]+\*?\*?$", c.strip()) else ""

_FIG = [0]    # numeração automática das provas recortadas
_BASE = [""]  # diretório do .md, para resolver caminho relativo das provas

def prova_html(spec, base_dir):
    """`[prova] arquivo.png | Legenda` -> figura embutida (base64) com legenda numerada.
    O recorte anotado é produzido pela ferramenta `recorte` (PDFKit) a partir dos autos."""
    import base64, mimetypes
    caminho, _, legenda = spec.partition("|")
    caminho = caminho.strip(); legenda = legenda.strip()
    if not os.path.isabs(caminho):
        caminho = os.path.join(base_dir, caminho)
    if not os.path.exists(caminho):
        return "<p><strong>[prova ausente: %s]</strong></p>" % html.escape(os.path.basename(caminho))
    tipo = mimetypes.guess_type(caminho)[0] or "image/png"
    with open(caminho, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    _FIG[0] += 1
    cap = ""
    if legenda:
        cap = ("<figcaption><span class='fig'>Figura %d —</span> %s</figcaption>"
               % (_FIG[0], inline(legenda)))
    return ("<figure class='prova'><img src='data:%s;base64,%s'>%s</figure>"
            % (tipo, b64, cap))

def _img64(caminho, base_dir):
    import base64, mimetypes
    if not os.path.isabs(caminho):
        caminho = os.path.join(base_dir, caminho)
    if not os.path.exists(caminho): return None
    tipo = mimetypes.guess_type(caminho)[0] or "image/png"
    with open(caminho, "rb") as fh:
        return "data:%s;base64,%s" % (tipo, base64.b64encode(fh.read()).decode("ascii"))

def provapar_html(spec, base_dir):
    """`[provapar] pagina.png | destaque.png | Etiqueta do destaque | Legenda`
    -> PÁGINA INTEIRA do documento à esquerda e o TRECHO DESTACADO à direita, na mesma folha.
    As etiquetas azuis discriminam cada lado (padrão canônico 26/08/2026)."""
    partes = [p.strip() for p in spec.split("|")]
    if len(partes) < 2:
        return "<p><strong>[provapar: informe pagina.png | destaque.png | etiqueta | legenda]</strong></p>"
    pag, amp = _img64(partes[0], base_dir), _img64(partes[1], base_dir)
    etiqueta = partes[2] if len(partes) > 2 and partes[2] else "Trecho destacado"
    legenda = partes[3] if len(partes) > 3 else ""
    if amp is None or pag is None:
        falta = partes[0] if pag is None else partes[1]
        return "<p><strong>[prova ausente: %s]</strong></p>" % html.escape(os.path.basename(falta))
    _FIG[0] += 1
    cap = ""
    if legenda:
        cap = ("<figcaption><span class='fig'>Figura %d —</span> %s</figcaption>"
               % (_FIG[0], inline(legenda)))
    return ("<figure class='provapar'><div class='par'>"
            "<div class='lado pag'><span class='rot'>Documento na íntegra</span>"
            "<img src='" + pag + "'></div>"
            "<div class='seta'></div>"   # 02/09/2026, item 3.10
            "<div class='lado amp'><span class='rot'>" + inline(etiqueta) + "</span>"
            "<img src='" + amp + "'></div>"
            "</div>" + cap + "</figure>")

# ───────── ADENDO 02/09/2026 — funções dos itens 3.1, 3.2, 3.5, 3.8, 3.9 e 3.10 ─────────
# Tokens que continuam em caixa alta dentro do versalete (siglas, romanos, números).
_SIGLAS = {"OAB", "SC", "TJSC", "STJ", "STF", "TRF4", "TST", "TRT", "TRT12", "CPC", "CPP", "CC",
           "CLT", "CDC", "CF", "INSS", "ED", "RE", "AI", "AC", "MM", "PJE", "EPROC", "GFES", "ILPI",
           "ADI", "ADC", "HC", "MS", "JEC", "CNJ", "CNPJ", "CPF", "RG", "DJE", "DJEN", "ECA",
           "LGPD", "IRDR", "IAC", "RISTJ", "RITJSC", "EOAB", "AJG", "UF", "PPP", "CEP", "GP", "CGJ"}
_MINUSCULAS = {"de", "do", "da", "dos", "das", "e", "em", "a", "o", "ao", "à", "às", "aos", "com",
               "por", "para", "sob", "sobre", "no", "na", "nos", "nas", "ou", "que", "se"}

def versalete_txt(t):
    """Converte texto em CAIXA ALTA para caixa mista, para que `font-variant: small-caps`
    tenha efeito (versalete sobre caixa alta não faz nada). Preserva siglas, romanos e
    tokens com dígito ou barra. Texto que já está em caixa mista volta intacto."""
    letras = re.sub(r"[^A-Za-zÀ-ÿ]", "", t)
    if not letras or letras != letras.upper():
        return t
    def _tok(tok, primeiro):
        if "/" in tok:
            return "/".join(_tok(x, primeiro) for x in tok.split("/"))
        nucleo = tok.strip(".,;:()[]\"'«»—–-")
        if (not nucleo or re.fullmatch(r"[IVXLCDM]+", nucleo) or nucleo in _SIGLAS
                or re.search(r"\d", nucleo)):
            return tok
        low = tok.lower()
        if not primeiro and nucleo.lower() in _MINUSCULAS:
            return low
        m = re.match(r"^([^A-Za-zÀ-ÿ]*)(.)(.*)$", low)
        return m.group(1) + m.group(2).upper() + m.group(3) if m else low
    toks = t.split(" ")
    return " ".join(_tok(tok, i == 0 or toks[i - 1] in ("—", "–", "-", ":"))
                    for i, tok in enumerate(toks))

def ja_numerado(t):
    return bool(re.match(r"^\s*(?:[IVXLC]+|\d+(?:\.\d+)*)\s*[\.\)\u2014\u2013\-]", t))

def requerimentos_html(linhas):
    """`> [x] texto` marca; `> [ ] texto` não marca. Vira lista com caixas de seleção."""
    itens = []
    for l in linhas:
        s = l.strip()
        if not s: continue
        m = re.match(r"^(?:-\s*)?\[([ xX])\]\s*(.*)$", s)
        if m:
            on = m.group(1).strip() != ""
            itens.append("<li class='%s'><span class='cx'></span>%s</li>"
                         % ("on" if on else "off", inline(m.group(2).strip())))
        else:
            itens.append("<li class='on'><span class='cx'></span>" + inline(s) + "</li>")
    return "<ul class='req'>" + "".join(itens) + "</ul>"

def provatrio_html(spec, base_dir):
    """`[provatrio] a.png | b.png | c.png | Rótulo A ; Rótulo B ; Rótulo C | Legenda`"""
    partes = [p.strip() for p in spec.split("|")]
    if len(partes) < 3:
        return "<p><strong>[provatrio: informe a.png | b.png | c.png | rótulos | legenda]</strong></p>"
    imgs = [_img64(p, base_dir) for p in partes[:3]]
    if any(i is None for i in imgs):
        falta = partes[[k for k, i in enumerate(imgs) if i is None][0]]
        return "<p><strong>[prova ausente: %s]</strong></p>" % html.escape(os.path.basename(falta))
    rots = [r.strip() for r in (partes[3] if len(partes) > 3 else "").split(";")]
    while len(rots) < 3: rots.append("")
    legenda = partes[4] if len(partes) > 4 else ""
    _FIG[0] += 1
    cap = (("<figcaption><span class='fig'>Figura %d —</span> %s</figcaption>" % (_FIG[0], inline(legenda)))
           if legenda else "")
    cols = "".join("<div>" + (("<span class='rot'>" + inline(r) + "</span>") if r else "")
                   + "<img src='" + i + "'></div>" for i, r in zip(imgs, rots))
    return "<figure class='provatrio'><div class='tri'>" + cols + "</div>" + cap + "</figure>"

def provaquadro_html(spec, itens, base_dir):
    """`[provaquadro] doc.png | Rótulo do documento | Legenda`, seguido de linhas
    `- Campo: teor (coordenada)`. Documento reduzido à esquerda, seta, quadro à direita."""
    partes = [p.strip() for p in spec.split("|")]
    doc = _img64(partes[0], base_dir) if partes and partes[0] else None
    if doc is None:
        return "<p><strong>[prova ausente: %s]</strong></p>" % html.escape(os.path.basename(partes[0] if partes else "?"))
    rot = partes[1] if len(partes) > 1 else "Documento na íntegra"
    legenda = partes[2] if len(partes) > 2 else ""
    linhas = []
    for it in itens:
        campo, _, teor = it.partition(":")
        if not _:
            campo, teor = "", it
        linhas.append("<tr><td>" + inline(campo.strip()) + "</td><td>" + inline(teor.strip()) + "</td></tr>")
    _FIG[0] += 1
    cap = (("<figcaption><span class='fig'>Figura %d —</span> %s</figcaption>" % (_FIG[0], inline(legenda)))
           if legenda else "")
    return ("<figure class='provaquadro'><div class='par'>"
            "<div class='doc'><span class='rot'>" + inline(rot) + "</span><img src='" + doc + "'></div>"
            "<div class='seta'></div>"
            "<div class='campos'><table class='q'><thead><tr><th>Campo</th><th>Teor (coordenada nos autos)</th></tr></thead>"
            "<tbody>" + "".join(linhas) + "</tbody></table></div>"
            "</div>" + cap + "</figure>")

def eixo_do_tempo(linhas):
    """Renderiza os eventos '~ data | texto' como EIXO HORIZONTAL com seta e cortes
    verticais marcando o tempo (padrão canônico 26/08/2026). Prefixo '!' destaca o marco.
    Linhas que não forem evento entram como parágrafo antes do eixo."""
    antes, marcos = [], []
    for l in linhas:
        s = l.strip()
        if not s: continue
        if s.startswith("~ "):
            corpo = s[2:].strip()
            mark = ""
            if corpo.startswith("!"): mark, corpo = " mark", corpo[1:].strip()
            dt, _, tx = corpo.partition("|")
            marcos.append((dt.strip(), tx.strip(), mark))
        else:
            antes.append("<p>" + inline(s) + "</p>")
    if not marcos:
        return "".join(antes)
    # 27/08/2026 (regra 25, conferência da vista): o eixo HORIZONTAL só é legível com
    # poucos marcos. Com 5 ou mais, ou com texto longo, ele espreme as colunas e pica as
    # palavras — vira lista VERTICAL, que respira e se lê.
    _longo = any(len(t) > 60 for _, t, _ in marcos)
    if len(marcos) >= 5 or _longo:
        itens = "".join("<li class='%s'><span class='dt'>%s</span>%s</li>"
                        % ("mark" if m.strip() else "", inline(d), inline(t))
                        for d, t, m in marcos)
        # 27/08/2026 — a partir de 6 marcos a lista passa de 10 cm e, indivisível,
        # abriria vão no pé da página anterior: ela quebra entre marcos (nunca dentro).
        _cls = "tl longa" if len(marcos) >= 6 else "tl"
        return "".join(antes) + "<ul class='" + _cls + "'>" + itens + "</ul>"
    cels = "".join("<span class='mk%s'><span class='dt'>%s</span>"
                   "<span class='tx'>%s</span></span>" % (m, inline(d), inline(t))
                   for d, t, m in marcos)
    return ("".join(antes) + "<div class='eixo'><div class='trilho'></div>"
            "<div class='marcos'>" + cels + "</div></div>")

JANELAS = {"qualificacao": ("qualif", ""), "qualif": ("qualif", ""),
           "citacao": ("cita", ""), "cita": ("cita", ""),
           "linhadotempo": ("tempo", ""), "tempo": ("tempo", ""),
           "calculo": ("calc", ""), "calc": ("calc", ""),
           # 26/08/2026 — estendido às PROCURAÇÕES e contratos por ordem do Dr. Gabriel:
           # destaca o núcleo do instrumento (os poderes conferidos, o objeto).
           "poderes": ("poderes", ""), "objeto": ("poderes", ""),
           # 26/08/2026 — DOUTRINA (poucas linhas) e SÚMULA/JURISPRUDÊNCIA, ambas com o
           # rótulo virando ETIQUETA DE REFERÊNCIA COMPLETA abaixo do trecho.
           "doutrina": ("dout", ""), "dout": ("dout", ""),
           "sumula": ("jur", ""), "jurisprudencia": ("jur", ""), "jur": ("jur", ""),
           # 02/09/2026 (item 3.2) — quadro de REQUERIMENTOS PRELIMINARES da capa.
           "requerimentos": ("req", ""), "req": ("req", "")}

def body_to_html(body, _nivel=0):
    out, in_list, in_tl = [], False, False
    viu_vocativo, gap_feito = False, False
    # 27/08/2026 — índice do último título emitido, para colar nele o parágrafo
    # seguinte num bloco indivisível (evita título órfão no pé da página).
    _titulo_aberto = [None]
    tab, cap = [], None
    jan_tipo, jan_rot, jan_buf = None, None, []   # janela suspensa em coleta
    numerar = [False]          # 02/09/2026 (3.5): diretiva @numerar
    pq = [None, []]            # 02/09/2026 (3.9): [provaquadro] em coleta
    def flush_pq():
        if pq[0] is not None:
            out.append(provaquadro_html(pq[0], pq[1], _BASE[0])); pq[0], pq[1] = None, []
    def close():
        nonlocal in_list, in_tl
        if in_list: out.append("</ul>"); in_list = False
        if in_tl: out.append("</ul>"); in_tl = False
    def flush_tab():
        nonlocal tab, cap
        if not tab: return
        linhas = [l for l in tab if not re.match(r"^\|[\s:\-|]+\|$", l)]
        # 27/08/2026 — quadro que passa de ~4 cm quebra entre páginas, repetindo o
        # cabeçalho, em vez de ser empurrado inteiro e abrir vão na folha anterior.
        # Limiar de 7 linhas: medido na vista, quadro menor que isso cabe e não deve
        # quebrar; maior, quebra no meio da tabela (o rótulo vai colado, ver CSS).
        out.append("<table class='q longa'>" if len(linhas) >= 7 else "<table class='q'>")
        if cap: out.append("<caption>" + inline(cap) + "</caption>")
        for i, l in enumerate(linhas):
            cs = _celulas(l)
            if i == 0:
                out.append("<thead><tr>" + "".join("<th" + _num(c) + ">" + inline(c) + "</th>" for c in cs) + "</tr></thead><tbody>")
            else:
                tot = " class='tot'" if re.search(r"(?i)\*\*(total|soma)", l) else ""
                out.append("<tr" + tot + ">" + "".join("<td" + _num(c) + ">" + inline(c) + "</td>" for c in cs) + "</tr>")
        out.append("</tbody></table>")
        tab, cap = [], None
    def fecha_janela():
        """Fecha a janela suspensa em coleta, renderizando o conteúdo recursivamente."""
        nonlocal jan_tipo, jan_rot, jan_buf
        if jan_tipo is None: return
        cls = JANELAS.get(jan_tipo, ("qualif", ""))[0]
        if cls == "tempo":
            interno = eixo_do_tempo(jan_buf)
        elif cls == "req":
            interno = requerimentos_html(jan_buf)
        else:
            interno = body_to_html("\n".join(jan_buf), _nivel + 1) if jan_buf else ""
        rot = ("<span class='jrot'>" + inline(jan_rot) + "</span>") if jan_rot else ""
        # 27/08/2026 — janela ALTA quebra entre páginas em vez de abrir vão no pé da
        # anterior. É alta quando o texto passa de ~700 caracteres (≈ 10 cm de mancha)
        # ou quando já contém um bloco longo (linha do tempo ou quadro) dentro dela.
        _texto = "\n".join(jan_buf)
        _alta = (len(_texto) + len(jan_rot or "") > 520 or "'tl longa'" in interno or "'q longa'" in interno)
        out.append("<div class='jan " + cls + (" longa" if _alta else "") + "'>"
                   + rot + interno + "</div>")
        jan_tipo, jan_rot, jan_buf = None, None, []

    for line in body.split("\n"):
        s = line.strip()
        # --- janelas suspensas: > [!tipo] Rótulo ... (linhas seguintes com '>') ---
        m_jan = re.match(r">\s*\[!(\w+)\]\s*(.*)", s)
        if m_jan and _nivel == 0:
            close(); fecha_janela()
            # 27/08/2026: a qualificação passou a vir em JANELA; o respiro do vocativo
            # precisa disparar aqui também, senão o endereçamento fica grudado nela.
            if viu_vocativo and not gap_feito:
                out.append("<div class='vocgap'></div>"); gap_feito = True
            if tab: flush_tab()
            tipo = m_jan.group(1).lower()
            if tipo in JANELAS:
                jan_tipo, jan_rot, jan_buf = tipo, m_jan.group(2).strip(), []
                continue
        if jan_tipo is not None:
            if s.startswith(">"):
                jan_buf.append(re.sub(r"^\s*>\s?", "", line)); continue
            if s == "":
                jan_buf.append(""); continue
            fecha_janela()
        if s.startswith("|") and s.endswith("|"):
            close(); tab.append(s); continue
        if tab: flush_tab()
        if s.startswith("[quadro] "):
            close(); cap = s[9:].strip(); continue
        if s.startswith("[prova] "):
            close(); out.append(prova_html(s[8:].strip(), _BASE[0])); continue
        if s.startswith("[provapar] "):
            close(); out.append(provapar_html(s[11:].strip(), _BASE[0])); continue
        # 02/09/2026 — itens 3.8 e 3.9
        if s.startswith("[provatrio] "):
            close(); out.append(provatrio_html(s[12:].strip(), _BASE[0])); continue
        if s.startswith("[provaquadro] "):
            close(); flush_pq(); pq[0] = s[14:].strip(); continue
        if pq[0] is not None:
            if s.startswith("- "):
                pq[1].append(s[2:].strip()); continue
            flush_pq()
        if s == "@numerar":
            numerar[0] = True; continue
        if s.startswith("~ "):
            close() if in_list else None
            corpo = s[2:].strip()
            marca = ""
            if corpo.startswith("!"): marca, corpo = " class='mark'", corpo[1:].strip()
            dt, _, txt = corpo.partition("|")
            if not in_tl: out.append("<ul class='tl'>"); in_tl = True
            out.append("<li" + marca + "><span class='dt'>" + inline(dt.strip()) + "</span>"
                       + inline(txt.strip()) + "</li>"); continue
        if s == "":
            close(); continue
        # assinatura canônica — marca do advogado (ordem do Dr. Gabriel, 27/08/2026)
        if s.startswith("@assinatura"):
            _cargo = s[len("@assinatura"):].strip() or "Advogado"
            close()
            # 27/08/2026 — ASSINATURA NUNCA FICA QUASE SOZINHA NA ÚLTIMA PÁGINA.
            # O gate de paginação exige um mínimo de linhas na folha final. Em vez de o
            # redator caçar milímetros enxugando texto a cada regeração, o gerador COLA
            # ao fecho os cinco últimos blocos de texto: se a assinatura desce de página,
            # eles descem junto, e a última folha nasce com corpo. `break-after: avoid`
            # em cadeia, aplicado de trás para frente sobre o que já foi emitido.
            _colados = 0
            for _i in range(len(out) - 1, -1, -1):
                if _colados >= 5:
                    break
                _el = out[_i]
                if _el.startswith("<p ") or _el.startswith("<p>") or _el.startswith("<li"):
                    if "class='" in _el:
                        out[_i] = _el.replace("class='", "class='colanofecho ", 1)
                    else:
                        out[_i] = _el.replace("<p>", "<p class='colanofecho'>", 1) \
                                     .replace("<li>", "<li class='colanofecho'>", 1)
                    _colados += 1
                elif _el.startswith("</ul>") or _el.startswith("<div class='sp'"):
                    continue
                else:
                    break
            out.append("<div class='assin'>"
                       "<p class='assin-nome'><strong>Gabriel Fabrízio do Espírito Santo</strong></p>"
                       "<p class='assin-cargo'>" + html.escape(_cargo) + "</p>"
                       "<p class='assin-oab'>OAB/SC 53.040</p></div>"); continue
        if s.startswith("@@ "):
            close(); viu_vocativo = True
            _txt = s[3:].strip()
            _fecho = bool(re.search(r"pede deferimento", _txt)) or bool(
                re.match(r"^[^,]{2,40}/[A-Z]{2},\s+\d", _txt))
            _voc = (not gap_feito) and (versalete_txt(_txt) != _txt)   # 02/09/2026 (3.1)
            if _voc: _txt = versalete_txt(_txt)
            out.append("<p class='center" + (" fecho" if _fecho else "") + (" voc" if _voc else "") + "'>"
                       + inline(_txt) + "</p>"); continue
        # Folga entre o vocativo e a qualificacao (ordem do Gabriel, 20/08/2026): 3 linhas.
        if (viu_vocativo and not gap_feito and re.match(r"^\*\*[^*]+:\*\*", s)):
            close(); out.append("<div class='vocgap'></div>"); gap_feito = True
        if s.startswith("### "):
            close(); out.append("<h3 class='subsub'>" + inline(s[4:].strip()) + "</h3>")
            _titulo_aberto[0] = len(out) - 1; continue
        if s.startswith("## "):
            _t2 = s[3:].strip(); _n2 = " num" if (numerar[0] and not ja_numerado(_t2)) else ""
            close(); out.append("<h2 class='sub" + _n2 + "'>" + inline(_t2) + "</h2>")
            _titulo_aberto[0] = len(out) - 1; continue
        if s.startswith("# "):
            _t1 = versalete_txt(s[2:].strip())   # 02/09/2026 (3.1): versalete pede caixa mista
            _n1 = " num" if (numerar[0] and not ja_numerado(_t1)) else ""
            close(); out.append("<h1 class='sec" + _n1 + "'>" + inline(_t1) + "</h1>")
            _titulo_aberto[0] = len(out) - 1; continue
        if s.startswith("> "):
            close(); out.append("<p class='cit'>" + inline(s[2:].strip()) + "</p>"); continue
        if s.startswith("- "):
            _abriu_lista = not in_list
            if not in_list: out.append("<ul>"); in_list = True
            out.append("<li" + (" class='curto'" if curto(s[2:]) else "") +
                       ">" + inline(s[2:].strip()) + "</li>")
            # título seguido diretamente de LISTA: os dois viajam juntos, como no caso
            # do parágrafo — senão o título fica órfão no pé da página.
            if _abriu_lista and _titulo_aberto[0] is not None and _titulo_aberto[0] == len(out) - 3:
                i = _titulo_aberto[0]
                out[i] = "<div class='secjunta'>" + out[i]
                out[-1] = out[-1] + "</li></ul></div><ul>"
                out[-1] = out[-1].replace("</li></li>", "</li>", 1)
            _titulo_aberto[0] = None
            continue
        if s == "\\":
            close(); out.append("<div class='sp'></div>"); continue
        close()
        classes = []
        if re.match(r"^\*\*[^*]+:\*\*", s): classes.append("flush")   # qualificação (Rótulo:) sem recuo
        if curto(s): classes.append("curto")
        cls = (" class='" + " ".join(classes) + "'") if classes else ""
        out.append("<p" + cls + ">" + inline(s) + "</p>")
        # cola este parágrafo ao título imediatamente anterior, num bloco indivisível.
        # ⚠️ Só quando o parágrafo é CURTO (até ~450 caracteres, ≈ 4 linhas): parágrafo
        # longo tem linhas de sobra para satisfazer orphans/widows sozinho, e colá-lo ao
        # título formaria bloco alto que abre vão na página anterior (medido em 27/08/2026).
        if (_titulo_aberto[0] is not None and _titulo_aberto[0] == len(out) - 2
                and len(s) <= 450):
            i = _titulo_aberto[0]
            out[i] = "<div class='secjunta'>" + out[i]
            out[-1] = out[-1] + "</div>"
        _titulo_aberto[0] = None
    if tab: flush_tab()
    flush_pq()
    close()
    fecha_janela()
    return "\n".join(out)

def main():
    argv = sys.argv[1:]
    sem_validacao = "--sem-validacao" in argv
    argv = [a for a in argv if a != "--sem-validacao"]
    if not argv:
        print("uso: python3 gerar_pdf.py PECA.md [--sem-validacao]"); sys.exit(2)
    md_path = argv[0]
    _BASE[0] = os.path.dirname(os.path.abspath(md_path))
    raw = open(md_path, encoding="utf-8").read()
    if raw.startswith("---"):
        raw = raw.split("---", 2)[2]
    body = raw.strip()
    # Gate de TAG CRUA (ordem do Gabriel, 19/08/2026): nenhum documento da casa sai com
    # marcacao de maquina visivel — ela denuncia confeccao por ferramenta.
    _tags = re.findall(r"<\s*/?\s*(?:br|p|div|span|b|i|u|hr|table|tr|td|th|img|a|h[1-6]|"
                       r"strong|em|ul|ol|li|blockquote|pre|code|font|center)\b[^>]*>|<!--.*?-->",
                       body, flags=re.I | re.S)
    if _tags:
        print("TAGS HTML CRUAS no markdown — o PDF sairia com elas impressas:")
        for _n, _l in enumerate(body.splitlines(), 1):
            for _t in re.findall(r"<[^>\n]{1,80}>", _l):
                if re.match(r"<\s*/?\s*(?:br|p|div|span|b|i|u|hr|table|tr|td|th|img|a|h[1-6]|"
                            r"strong|em|ul|ol|li|blockquote|pre|code|font|center)\b", _t, re.I):
                    print(f"  L{_n}: {_t}    -> {_l.strip()[:70]}")
        print("\nPDF NAO gerado. Use markdown puro — nunca tag HTML.")
        sys.exit(1)
    # Gate de norma culta sobre o corpo que vira PDF (decisão 05/06/2026)
    if sem_validacao:
        print("=" * 72)
        print("⚠️  GATE PULADO (--sem-validacao): o PDF pode conter rastro de IA ou")
        print("    vazamento (frontmatter/[VERIFICAR]). NÃO entregar a terceiro/protocolar")
        print("    sem revisão manual. O arquivo sai com sufixo _SEM-GATE para não ser")
        print("    confundido com o pronto-para-assinar.")
        print("=" * 72)
    if not sem_validacao:
        validador = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "scripts", "validar_norma_culta.py")
        if os.path.exists(validador):
            chk = subprocess.run([sys.executable, validador, "--stdin", "--modo", "peca"],
                                 input=body, text=True, capture_output=True)
            if chk.returncode == 1:
                print(chk.stdout)
                print("PDF NÃO gerado: corrija os ERROS acima (ou rode com --sem-validacao).")
                sys.exit(1)
        else:
            print("[aviso] validar_norma_culta.py não encontrado; gerando sem gate.")
    # Gate da REGRA DO PORTADOR (canônica 19/08/2026) — fato sem coordenada não vira tese.
    # Complementa o gate de norma culta: aquele cuida do DIREITO, este cuida do FATO.
    validador_fato = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "..", "scripts", "validar_ficha_de_fatos.py")
    if os.path.exists(validador_fato):
        chk_fato = subprocess.run([sys.executable, validador_fato, "--stdin", "--modo", "geral"],
                                  input=body, text=True, capture_output=True)
        if chk_fato.returncode == 1:
            print(chk_fato.stdout)
            print("PDF NÃO gerado: corrija os ERROS de fato acima (regra do portador).")
            sys.exit(1)
    else:
        print("[aviso] validar_ficha_de_fatos.py não encontrado; gerando sem esse gate.")

    # ---- TRAVA DE ADMISSIBILIDADE PRÉ-PROTOCOLO (28/08/2026, ordem escrita do Gabriel) ----
    # "Uma peça não se corrige no processo e sim antes de peticionar."
    # Emenda determinada pelo juízo (CPC art. 321) é defeito nosso exposto nos autos; repetida,
    # denuncia produção automatizada. Este gate roda ANTES de o PDF existir.
    # Tipo: --tipo inicial|contestacao|recurso|generico. Sem a flag, infere-se do texto.
    tipo_peca = None
    if "--tipo" in sys.argv:
        tipo_peca = sys.argv[sys.argv.index("--tipo") + 1]
    else:
        b = body.lower()
        if "contestação" in b or "contestacao" in b or "impugna especificamente" in b:
            tipo_peca = "contestacao"
        elif ("apelação" in b or "agravo" in b or "recurso especial" in b
              or "embargos de declaração" in b or "razões recursais" in b):
            tipo_peca = "recurso"
        elif "dá-se à causa" in b or "valor da causa" in b or "requer a citação" in b:
            tipo_peca = "inicial"
        else:
            tipo_peca = "generico"
    admis = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "scripts", "validar_admissibilidade.py")
    if os.path.exists(admis) and not sem_validacao:
        chk_adm = subprocess.run([sys.executable, admis, md_path, "--tipo", tipo_peca],
                                 capture_output=True, text=True)
        if chk_adm.returncode == 1:
            print(chk_adm.stdout)
            print("PDF NÃO gerado: a peça reprovou na TRAVA DE ADMISSIBILIDADE.")
            print("Corrija ANTES de peticionar — peça não se corrige no processo.")
            sys.exit(1)
    elif not os.path.exists(admis):
        print("[aviso] validar_admissibilidade.py não encontrado; gerando sem esse gate.")

    titulo_doc = os.path.splitext(os.path.basename(md_path))[0].replace("_", " ").replace("-", " ")
    full = ("<!doctype html><html lang='pt-br'><head><meta charset='utf-8'><title>" +
            html.escape(titulo_doc) + "</title><style>" + CSS +
            "</style></head><body>" + body_to_html(body) + "</body></html>")
    pdf_path = os.path.splitext(md_path)[0] + ("_SEM-GATE.pdf" if sem_validacao else ".pdf")
    with tempfile.TemporaryDirectory() as td:
        html_tmp = os.path.join(td, "peca.html")
        pdf_tmp  = os.path.join(td, "peca.pdf")
        open(html_tmp, "w", encoding="utf-8").write(full)
        try:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--user-data-dir=" + os.path.join(td, "cdir"),
                            "--no-pdf-header-footer", "--print-to-pdf=" + pdf_tmp,
                            "file://" + html_tmp],
                           timeout=90, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            pass
        if not os.path.exists(pdf_tmp):
            print("ERRO: PDF não gerado"); sys.exit(1)
        shutil.copy(pdf_tmp, pdf_path)
    # Metadados canônicos (regra 19): o Chrome deixa /Title doc.html,
    # /Creator HeadlessChrome e /Producer Skia/PDF — metadado denunciante.
    # Reescreve ANTES do gate forense e antes de qualquer entrega.
    limpar_metadados(pdf_path, titulo=titulo_de_arquivo(pdf_path))
    # Gate FORENSE (regra 19, canônica 24/08/2026): nenhum PDF sai com rastro de IA,
    # marcação crua, tag, camada oculta ou metadado denunciante.
    forense = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "scripts", "forense_documento.py")
    if os.path.exists(forense) and not sem_validacao:
        chk_f = subprocess.run([sys.executable, forense, pdf_path, "--modo", "saida"],
                               capture_output=True, text=True)
        if chk_f.returncode == 1:
            reprovado = os.path.splitext(pdf_path)[0] + "_REPROVADO-FORENSE.pdf"
            os.replace(pdf_path, reprovado)
            print(chk_f.stdout)
            print("PDF REPROVADO no gate forense (regra 19) e renomeado para:", reprovado)
            print("NÃO entregar. Corrija a origem e gere de novo.")
            sys.exit(1)
    # Gate de DIAGRAMAÇÃO (ordem do Dr. Gabriel, 27/08/2026): mede o vão no PÉ de cada
    # página. Bloco alto e indivisível empurrado para a folha seguinte deixa 30-45% de
    # branco — defeito que a conferência da última página NÃO pega. Avisa e não aborta:
    # o conserto pode exigir mover o bloco no texto, decisão de quem escreve.
    diag = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "scripts", "validar_diagramacao.py")
    if os.path.exists(diag):
        chk_d = subprocess.run([sys.executable, diag, pdf_path],
                               capture_output=True, text=True)
        if chk_d.returncode == 1:
            print(chk_d.stdout)
            print(">>> VÃO NO PÉ DA PÁGINA: conserte antes de entregar (regra 27).")
    print("PDF:", pdf_path)

    # ---- GATE DE PAGINAÇÃO E TIPOGRAFIA (27/08/2026) --------------------------------
    # Ordem do Gabriel: "nas petições não pode haver linhas órfãs ou páginas em branco"
    # e "anote para não haver mais erros". Roda DEPOIS de gerar, sobre o PDF, e confere
    # contra references/tipografia-vigente.json (fonte única das medidas). Não aborta a
    # geração — o PDF já existe —, mas GRITA e devolve código 1, para que ninguém entregue
    # peça com órfã, viúva, página em branco ou medida revogada sem ter visto o aviso.
    gate_pag = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "scripts", "validar_paginacao.py")
    if os.path.exists(gate_pag) and not sem_validacao:
        chk = subprocess.run([sys.executable, gate_pag, pdf_path], capture_output=True, text=True)
        if chk.returncode == 1:
            print(chk.stdout)
            print(">>> O PDF FOI GERADO, MAS REPROVOU NO GATE DE PAGINAÇÃO. NÃO ENTREGUE ASSIM.")
            sys.exit(1)

if __name__ == "__main__":
    main()
