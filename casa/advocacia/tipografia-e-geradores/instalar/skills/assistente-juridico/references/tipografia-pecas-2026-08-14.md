> ⚠️ **AVISO DE REVOGAÇÃO (02/09/2026).** As MEDIDAS citadas neste arquivo são históricas.
> A régua vigente é só `references/tipografia-vigente.json` (Times 12 · Charter 11 a **3 cm** ·
> entrelinha **1,35** · margens 3/3 e 2,3/1,8 · recuo 2 cm · negrito **e** itálico · versalete nos
> títulos). Onde este texto trouxer outro número, o número está revogado. Arquivo mantido por
> histórico (regra 25); correção feita na reanálise dos cursos de 02/09/2026.

# REGRA CANÔNICA DO ESCRITÓRIO — tipografia de toda a escrita (14/08/2026)

> Instituída pelo Gabriel em 14/08/2026, por escrito no chat, e ampliada por ele no mesmo dia:
> o método do curso "Tipografia Jurídica" (Júlio Xavier) é o padrão canônico de TODA A
> ESCRITA DO ESCRITÓRIO — petições, pareceres, relatórios, contratos e documentos. Fontes do método, estudadas na
> íntegra em 14/08/2026: e-book "7 erros tipográficos que comprometem sua petição"
> (`~/Downloads/E-book-tipografia-v12-1.pdf`) e os 7 vídeos complementares nele linkados
> (transcrições lidas por completo: sublinhado lmpSsbWJOmg; parágrafo/recuo roqP7Z6a9_g;
> citações svRwYDupTfc; fontes proibidas mlnNNG5IlK4; análises 1Wn8xxkYa7c, GCn_rMaYdNk,
> _YfwBNm7HOI). Substitui o padrão de 03/06/2026 (Times 12 / 1,5 / recuo 1,25 cm) para
> peças novas. Registrada por escrito e datada, como a casa exige.

## Princípios do método (regem qualquer dúvida)

- **Tipografia é em benefício do leitor** (juiz/assessor): clareza, credibilidade, foco.
- **Menos é mais**: primeiro subtrair, depois organizar. Cada elemento precisa ter função.
- **Destaque é contraste**: quem destaca tudo não destaca nada; UM marcador de destaque
  basta — nunca acumular (negrito + sublinhado + caixa alta = ruído).
- **Familiaridade**: a peça deve parecer texto jurídico profissional (livro, decisão de
  tribunal), nunca folder, catálogo ou trabalho escolar.
- **Documento de texto se faz em processador de texto**, não em programa gráfico.

## O padrão da peça forense GFES

1. **Fonte:** Georgia, corpo 12 pt, peso normal, PRETO sobre branco. (Serifada
   transicional indicada nominalmente pelo método como alternativa à Times; disponível no
   macOS. Bookman Old Style é alternativa aprovada. Fallback: Times New Roman.)
   **Proibidas** (vídeo "fontes que você não deve usar"): monoespaçadas (Courier),
   condensadas/Narrow, pesos Light/finos no corpo, fontes sem credibilidade (Comic Sans,
   Algerian etc.) e geométricas (Century Gothic) no corpo.
2. **Entrelinha 1,5** (revisado por ordem do Gabriel em **19/08/2026**; revoga o item
   original do método, que pedia 1,25 e rejeitava 1,5 por "frouxo/ABNT"). Aplicada ao corpo
   de peça, parecer/relatório e contrato nos três geradores da casa. Títulos, timbre, rodapé
   e bloco de citação mantêm entrelinha própria, mais justa, por função — não são corpo
   corrido.
3. **Parágrafo:** recuo de primeira linha de **1 cm** (≈1 em — "extremamente razoável"
   no método), **sem** espaçamento entre parágrafos. Recuo E espaçamento juntos =
   pleonasmo tipográfico. Nada de recuos de 3-4 cm. Formatação por estilo, nunca TAB/Enter.
4. **Destaque:** somente **negrito**, com parcimônia. **Sublinhado e marca-texto:
   proibidos sempre.** Itálico não é destaque de rotina: latim/estrangeirismos e títulos
   de obras (pontualmente admissível como contraste, nunca cumulado com negrito).
   **Caixa alta proibida no corpo** como ênfase (vocativo e títulos curtos de seção são
   praxe e permanecem); ênfase excepcional em versalete.
5. **Citações** (vídeo "como citar jurisprudência"): até 3 linhas → no corpo, entre
   aspas, SEM itálico. Mais de 3 linhas → bloco recuado (**2 cm**), **mesma fonte** em
   corpo **11 pt**, entrelinha mais justa, SEM aspas e SEM itálico — as únicas marcas do
   bloco são o recuo e o corpo menor. Bloco uno (sem espaçamento interno). Citar só o
   núcleo que decide, suprimindo o resto com [...] (jamais suprimir o que contradiga —
   má-fé); destaque nosso em negrito com a nota "(grifamos)". Muitas vezes a citação
   INDIRETA (paráfrase + referência entre parênteses) comunica melhor que o bloco.
   Prova integral vai no ANEXO com remissão; na peça vai o recorte que interessa.
6. **Ornamentos: nenhum.** Sem marca d'água, capa, ícones, QR code (link clicável no
   corpo é superior — se um dia usar QR, dizer aonde leva), barras/fundos coloridos,
   texto cinza (mata contraste), cores primárias, rodapé institucional (dados do
   escritório, quando necessários, no máximo na 1ª página). Peça limpa da casa = mantida.
7. **Elementos visuais só com função real** (facilitar a compreensão de dado concreto):
   tabela sóbria (fundo branco/pastel), gráfico simples (ex.: linhas comparando índices),
   linha do tempo enxuta, print RECORTADO e legível (nunca a tela 16:9 inteira). Sempre
   com respiro antes e depois. Ícone decorativo nunca (avião embaixo de "aéreo" não
   comunica nada).
8. **Página e layout:** A4; margens 3 (sup.) / 2 (inf.) / 3 (esq.) / 2 (dir.) cm —
   generosas (preservam a margem do carimbo do eproc); justificado **com hifenização
   automática ligada** (evita os "rios" brancos do justificado); linha não muito longa;
   evitar título órfão no pé da página; um ponto de atenção por página.
9. **Estrutura:** vocativo centralizado; qualificação à esquerda; título da peça
   centralizado em negrito; seções numeradas à esquerda em negrito; data e assinatura
   centralizadas. **Síntese da controvérsia no início** da peça é boa prática do método
   (o leitor se situa no pico de atenção).

## Implementação

- Gerador oficial: `assets/gerar_pdf.py` — atualizado em 14/08/2026 (backup
  `gerar_pdf_pre-tipografia-20260814.py.bak`). Marcação nova: linha iniciada por `> `
  vira bloco de citação (11 pt, recuo 2 cm). Gate de norma culta continua obrigatório.
- Alcance: TODA a escrita do escritório (ampliação de 14/08/2026): peças (gerar_pdf.py),
  contratos e documentos institucionais (gerar_contrato_pdf.py — mantém papel timbrado,
  mas segue fonte/entrelinha/recuo/destaques do método) e pareceres/relatórios internos
  (gerar_pdf_relatorio.py — paragrafação americana, admitida pelo método). Os três
  geradores foram atualizados em 14/08/2026, com backups .bak ao lado.
- Peças já protocoladas não se retificam por tipografia; pendentes de protocolo
  regeram-se no novo padrão.

## Histórico de aplicação

- 14/08/2026 — regra instituída (e-book); ampliada no mesmo dia com o estudo integral dos
  7 vídeos, a pedido expresso do Gabriel. Regeneradas no novo padrão as 4 peças pendentes
  da auditoria (Memoriais ACP 0900193-90; Aditamento Yagho 5026537-50; Embargos monitória
  5003272-83 v2; Honorários Wesley 5025093-96).
