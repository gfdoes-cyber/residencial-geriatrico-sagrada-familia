# 📐 CANÔNICA: Tipografia jurídica e design da informação (24/08/2026)

**Fonte:** auditoria integral do site Tipografia Jurídica (tipografiajuridica.com.br), de
**Júlio Xavier** — pós-graduado em Direito Público, 15 anos como assessor na Justiça Federal
do RJ, especialista em tipografia e design de documentos jurídicos. Cinco artigos legítimos
lidos por inteiro em 24/08/2026 (o restante do site estava tomado por spam de invasão — ver
nota de segurança ao fim). Conteúdo **parafraseado e sistematizado** para uso da casa; a
fundamentação científica citada pelo autor: Reber, Schwarz & Winkielman, *Processing Fluency
and Aesthetic Pleasure* (Pers. Soc. Psychol. Rev., 2004).

Instituída pelo Gabriel como **nota canônica do escritório**: toda peça, parecer e documento
da casa segue estes princípios.

⚠️ **Este documento é APROFUNDAMENTO, não novidade.** O método Tipografia Jurídica já era o
padrão da casa desde **14/08/2026** — o que esta auditoria acrescenta é a camada de **design
da informação e ciência cognitiva** (as seis leis, a fluência de processamento, enquadrar ×
distinguir), que não estava sistematizada.

**Complementa — e NÃO revoga — a tipografia material vigente** (`tipografia-pecas-2026-08-14.md`,
revisada em 19 e 20/08/2026):
- **As medidas moram em `tipografia-vigente.json`** (fonte única desde 27/08/2026): Times New
  Roman 12 · Charter 11 a **3 cm**, entrelinha 1,3 · entrelinha do corpo **1,35** · recuo 2 cm ·
  margens 3/3 e 2,3/1,8 · destaque por **negrito e itálico** · versalete nos títulos (02/09).
  *(Corrigido em 02/09/2026: esta lista dizia entrelinha 1,5, citação a 4 cm e "só negrito",
  revogadas em 27/08/2026.)*
- Sublinhado, marca-texto e caixa alta no corpo: proibidos
- Hifenização ligada; zero ornamento; elemento visual só com função

## 1. O princípio-mestre: fluência de processamento

Quanto mais fácil é ler, navegar e compreender um documento, **melhor ele parece** — a
impressão de qualidade nasce ANTES da análise racional da tese, e a primeira impressão
condiciona a justificativa que vem depois (coerência emocional + viés de confirmação).
Facilidade é percebida como qualidade; esforço é percebido como fraqueza.

**Tradução operacional:** a forma não compete com o conteúdo — ela é a **infraestrutura de
leitura** que decide como a tese será acessada, compreendida e lembrada. Peça confusa não só
comunica mal: **enfraquece o argumento**. Juiz e assessor leem sob volume alto e tempo curto;
reduzir a fricção cognitiva deles é vantagem concreta.

## 2. As seis leis do design da informação aplicadas à peça

1. **Familiaridade (Lei de Jakob).** O leitor prefere estrutura que já conhece. A peça não
   pode exigir que o juiz "aprenda" como ela funciona. Inovar é usar o padrão a favor, nunca
   romper com ele. Sequência lógica reconhecível, títulos claros.
2. **Complexidade (Lei de Hick).** Cada opção a mais atrasa a decisão. Excesso de teses,
   pedidos subsidiários desorganizados e caminhos paralelos competem entre si: quando tudo é
   relevante, nada se destaca. **Hierarquizar teses e conduzir à central.** (O autor aponta
   este como o principal obstáculo real à admissibilidade nos tribunais superiores — os
   requisitos são objetivos; o recurso é que chega desorganizado.)
3. **Contraste (Efeito Von Restorff).** Destacar é ESCOLHER. Tudo em negrito = nada em
   destaque, só ruído. Grifo não é sinônimo de destaque. Parcimônia e intenção: sinalizar
   apenas o que decide.
4. **Fragmentação (Lei de Miller / chunking).** Bloco longo de texto é barreira. Parágrafos
   delimitados, títulos e subtítulos, quebras estratégicas, elementos visuais que deem
   dinâmica. Navegabilidade não é conveniência — é condição de análise eficiente.
5. **Estética-usabilidade.** Documento organizado é percebido como **rigoroso e confiável**
   antes de qualquer mérito; documento desorganizado sugere raciocínio desestruturado. A
   forma jamais pode contradizer o conteúdo — deve potencializá-lo.
6. **Primazia e recência.** O que abre e o que fecha é o que fica. A abertura instala o mapa
   mental do caso (👉 valida a **SÍNTESE de primeira página**, que já é padrão da casa); o
   fechamento consolida a impressão que estará ativa na decisão (👉 memoriais bem-feitos são
   o efeito de recência em ação). Introdução e conclusão não são protocolo: são ancoragem.

## 3. Convencimento = enquadrar e distinguir

O desafio do advogado quase nunca é convencer da tese em abstrato — o juiz sabe o direito. O
desafio é o **enquadramento fático**: convencer de que os fatos narrados merecem a cobertura
daquela tese (se favorável, enquadrar; se desfavorável, **distinguir**). Por isso a narrativa
dos fatos é estratégica: não listar fatos — construir história coerente, com suporte visual
(linha do tempo, quadro, printscreen com contexto) que guie a interpretação.

Em decisões rápidas (liminar, admissibilidade), o julgador procura **os pressupostos** antes
da tese: estruturar a peça para que ele os encontre de imediato.

## 4. Padronização documental — o produto da advocacia É o documento

- Identidade fragmentada (cada advogado com fonte, destaque e formato próprios) = percepção
  de amadorismo. Consistência é métrica de qualidade.
- Padronizar **não** engessa: tira energia das escolhas irrelevantes e libera o redator para
  a camada estratégica (direito, redação, design da informação).
- O padrão é uma **"gramática visual"** comum, dentro da qual cada um opera com autonomia.
- O padrão define **estilos nomeados** (título, subtítulo, corpo, citação, marcadores) e
  **critérios de decisão**: quando tabela × lista; quando cabe sumário; como destacar citação
  sem poluir.
- Modelos práticos e replicáveis (na casa: os geradores `gerar_pdf*.py` já embutem o padrão;
  a marcação `#`/`##`/`###`/`@@`/`>` é a nossa camada de estilos).
- Três critérios de toda identidade documental: **identidade** (traduz o posicionamento),
  **unidade** (todo documento reconhecível), **praticidade/perpetuidade** (fácil de aplicar,
  logo aplicado de verdade).

## 5. Documento como ativo de marca

Parecer é consultado por anos; petição circula por assessores, juízes, desembargadores e
ministros; contrato é revisitado inúmeras vezes. O documento é a materialização tangível do
escritório — investir na sua identidade é branding, não estética. Retorno mensurável: menos
tempo de formatação, menos retrabalho, mais autonomia; intangível: percepção de valor,
diferenciação, coerência.

## 6. O redator como comunicador estratégico

Competência técnica é requisito mínimo e satura; o diferencial é comunicar o direito. Quem
redige na casa precisa dominar: (a) o leitor e suas limitações; (b) a psicologia do
processamento (fluência → percepção de verdade); (c) a narrativa estratégica dos fatos.
"Quem sabe direito automaticamente sabe comunicar o direito" é falso.

## Como isto se aplica na prática da casa (checklist de saída)

Antes de fechar qualquer peça, conferir contra as seis leis:
- [ ] A estrutura é a esperada pelo leitor daquela peça? (Jakob)
- [ ] As teses estão hierarquizadas, com a central inconfundível? (Hick)
- [ ] O destaque marca só o decisivo? Nada de negrito em série; **nunca** sublinhar. (Von Restorff)
- [ ] Sem parágrafo-muro; títulos que permitem navegar sem ler tudo? (Miller)
- [ ] A página parece cuidada na primeira olhada — margens, alinhamento, consistência? (Estética)
- [ ] A SÍNTESE abre instalando o mapa do caso e a conclusão fecha fixando o essencial? (Primazia/recência)
- [ ] Os fatos estão narrados para ENQUADRAR (ou distinguir), com apoio visual onde ajuda?

## 7. REGRA DE PAGINAÇÃO — assinatura nunca fica órfã (24/08/2026)

Ordem do Gabriel, nascida das procurações do caso David: **documento curto de estrutura fixa
— procuração, declaração, substabelecimento, termo — cabe em UMA folha**, com a assinatura na
mesma página do texto.

**Por quê, além da estética:** assinatura sozinha em folha separada do corpo é **flanco
jurídico** — abre alegação de que a folha de assinatura foi substituída. Em instrumento
particular, isso importa.

**Regra geral de viúva/órfã em QUALQUER documento da casa:**
- ⛔ Nunca deixar sozinha na página final: só a assinatura, só o fecho, só uma linha do último
  item, ou só o nome da parte.
- ⛔ Nunca deixar título de seção no pé da página, separado do texto que ele abre (o CSS já
  usa `page-break-after: avoid` nos títulos).
- ✅ Conferir SEMPRE a contagem de páginas do PDF gerado e o conteúdo da ÚLTIMA página antes
  de entregar — não basta olhar a primeira.

**Como resolver quando estourar por pouco (nesta ordem, sem mexer na tipografia canônica):**
1. remover espaçadores `\` supérfluos;
2. enxugar a redação (rol de poderes prolixo compacta muito sem perda jurídica — conferir
   depois que NENHUM poder sumiu);
3. transformar lista de itens em período corrido, quando forem poucos;
4. só em último caso, e apenas em documento anexo (nunca em peça), reduzir espaçamento.

**Conferência obrigatória após compactar:** extrair o texto do PDF e checar item a item que
todo dado crítico sobreviveu (CPF, RG, números de processo, cada poder especial, data).
Atenção: a extração insere espaços de kerning ("r eceber cita ção") — comparar com os espaços
removidos, senão dá falso alarme de dado faltando.

## ⚠️ Nota de segurança sobre a fonte (24/08/2026)

O site estava **invadido** na data da auditoria: ~270 posts de spam de cassino (Mostbet,
Olimp, Gama...) em russo/azeri injetados no WordPress, misturados aos 5 artigos legítimos.
A auditoria usou a API do WP filtrando as categorias reais e **nenhum link de spam foi
tocado**. Se a casa citar o site a terceiros, conferir antes se foi limpo. A tipografia do
próprio site (webfont Advercase/Fraunces para títulos, Switzer/Inter para texto) é marca da
web dele — **não** é padrão de peça. Peça da casa é **Times New Roman 12** (ver acima).

## 7-A. ADENDO MEDIDO (27/08/2026) — como o CSS cumpre a seção 7

Ordem do Dr. Gabriel: *"nas petições não pode haver linhas órfãs ou páginas em branco"*.
Medição no Chrome headless (motor dos geradores), varrendo a altura do bloco anterior:

- `orphans:3; widows:3` **produz** a linha órfã que pretende impedir: em parágrafo de 4 ou 5
  linhas a soma 3+3 é impossível, e o Chrome descarta a widow, quebrando 3+1.
- `orphans:2; widows:2` nunca deixou linha sozinha em parágrafo de 4 linhas ou mais.
- Sobra o parágrafo de **3 linhas** (2+2 > 3): resolvido no gerador pela classe `curto`
  (`break-inside: avoid`) aplicada a todo parágrafo/item com até 265 caracteres visíveis —
  ou cabe, ou migra inteiro.
- Os títulos passaram a ter de fato `page-break-after: avoid` (a seção 7 afirmava que já
  tinham; **não tinham** até 27/08/2026).
- O fecho ("pede deferimento" + data + assinatura) recebeu `break-before: avoid`.

**Buraco de página por bloco indivisível** (janela `[!tempo]`, quadro, figura) **não é
problema de CSS.** O bloco tem de ficar inteiro; se não cabe no que resta, pula. A correção é
a da seção 7: **enxugar a redação ANTES do bloco** — acrescentar texto para "encher" a página
só empurra o bloco de novo. Limite prático medido: a janela `[!tempo]` de 9 marcos ocupa
459 pt (medidos) contra 700 pt de área útil; acima de ≈ 14 marcos ela não cabe em página
nenhuma.

⚠️ **Ao testar paginação, gerar sempre dentro da pasta do caso.** Fora dela as figuras
`provapar` não são resolvidas, o PDF sai sem imagens e a paginação medida é falsa.

Implementado em `assets/gerar_pdf.py`; backups `gerar_pdf_pre-orfas-20260827.py.bak` e
`gerar_pdf_pre-orfas-v2-20260827.py.bak`.
