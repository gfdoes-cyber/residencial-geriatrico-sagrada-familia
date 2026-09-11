---
arquivo: Tipografia Jurídica — padrão de output PDF do escritório GFES
descricao: Regras de tipografia aplicadas a TODA peça processual em PDF gerada pelo escritório. Substitui o default Times New Roman 12pt + ABNT estrito. Calibrado para legibilidade humana, leitura por desembargador cansado e robustez contra "lost in the middle" quando IA faz revisão.
status: REVOGADA em 14/08/2026 — ver tipografia-vigente.json (banner posto em 02/09/2026)
criado_em: 2026-05-07
atualizado: 2026-05-07
camada_de_risco: amarela — afeta forma, não conteúdo
mantido_por: Claude (manutenção) + Gabriel (validação)
referencia_canonica: Matthew Butterick — Typography for Lawyers (typographyforlawyers.com)
tags: [padrao, tipografia, peca, redacao, pdf, butterick]
---

# 🖋️ Tipografia Jurídica

> ⛔ **REVOGADA.** Esta nota de 07/05/2026 (Butterick: Crimson Pro/Lora, Poppins, entrelinha 1,5,
> recuo 1,25, capítulo em página nova, cabeçalho e numeração de página, Pandoc/XeLaTeX) foi
> **inteiramente superada** pela canônica de 14/08/2026 e pela régua de 27/08/2026. A peça da
> casa sai pelos geradores em Times 12 / Charter 11, sem cabeçalho nem numeração, com as
> medidas de `skills/assistente-juridico/references/tipografia-vigente.json`. Mantida só como
> histórico. *(Banner posto na reanálise dos cursos, 02/09/2026 — item 4.8.)*

> **Resumo.** Toda peça processual em PDF do GFES sai na tipografia definida aqui. O default da advocacia brasileira (Times New Roman 12, espaçamento 1.5, ABNT) é tecnicamente válido, mas tipograficamente fraco — cansa o leitor, comprime hierarquia e parece máquina de escrever. Este Padrão troca o default por uma combinação serif moderna (corpo) + sans humanista (cabeçalhos), com regras explícitas de espaçamento, ênfase, citação e respiro. Aplica-se à geração automatizada de PDF via Pandoc + XeLaTeX (`.claude/agents/peca-pdf-template/`).

---

## 1. Fundamentação

Tipografia jurídica é aplicação de princípios de design tipográfico ao texto processual. A referência canônica é Matthew Butterick — advogado e tipógrafo formado em Harvard, autor de *Typography for Lawyers* — que sustenta que as quatro decisões mais importantes em qualquer documento são fonte, tamanho do corpo, entrelinhas e largura de linha, porque é isso que define a aparência do texto principal. Butterick chama Times New Roman não de "uma escolha de fonte" mas da "ausência de uma escolha de fonte" — popular por ubiquidade, não por qualidade.

A NBR 14724 da ABNT é norma acadêmica, não processual; o CNJ não fixa tipografia obrigatória em peças. O default brasileiro é convenção, não obrigação. Há liberdade técnica — e perdê-la equivale a entregar peça menos legível do que poderia ser.

Há também razão técnica menos óbvia: a peça é cada vez mais lida por **modelos de linguagem** (revisão IA, busca semântica interna, juris-search, pipeline de auditoria). Hierarquia tipográfica clara e respiros consistentes mitigam o efeito "lost in the middle" e o "positional bias" — o conteúdo que é fácil de ver é mais fácil de ser citado corretamente, tanto pelo desembargador quanto pelo modelo.

---

## 2. Regras concretas

### a) Fontes

**Corpo do texto.** Serifada moderna, com altura-x generosa e contraste moderado. Por ordem de preferência:

1. Crimson Pro — primeira escolha; sucessor do Crimson Text, otimizado pra leitura processual longa.
2. EB Garamond — alternativa clássica; ótima em texto fluido, levemente menos densa.
3. Source Serif Pro — alternativa neutra; boa em corpo + tela.
4. Equity (Butterick) — escolha do autor; comercial paga, deixar como aspiração.
5. **Lora** — fallback default do pipeline atual (Pandoc/XeLaTeX já tem instalada).
6. TeX Gyre Pagella — fallback LaTeX puro se nada acima estiver disponível.

Não usar: Times New Roman (default cansativo, padrão de máquina de escrever); Arial pra corpo (sans não-humanista, fadiga ocular em texto longo).

**Cabeçalhos.** Sans-serif humanista, peso médio-alto, contraste claro com o corpo. Por ordem de preferência:

1. Source Sans 3 — primeira escolha; humanista, ótima legibilidade em peso 600.
2. Inter — alternativa moderna; boa pra hierarquia em tela e impressão.
3. **Poppins** — fallback default do pipeline atual (instalada).
4. DejaVu Sans — fallback LaTeX puro.

**Citações em block quote.** Mesma família do corpo, 1pt menor, itálico opcional para citação literal de doutrina; redondo (sem itálico) para acórdãos transcritos — diferenciação visual entre voz autoral e voz citada.

### b) Espaçamento

Entrelinhas do corpo: **1.5** (compromisso entre densidade jurídica e respiro). Espaço antes de parágrafo: **6pt**. Indentação de primeira linha: **1.25cm** (modelo tradicional brasileiro), uniforme em todo o documento. Não usar duas formas (indentação + espaço extra) ao mesmo tempo — escolha um e seja consistente; este Padrão escolheu indentação + 6pt.

### c) Margens (folha A4)

Superior **3cm**, inferior **2.5cm**, esquerda **3cm**, direita **2.5cm**. ABNT prescreve 3/3/2/2; aqui se abre direita um pouco — peça deve ter respiro lateral suficiente pra anotação e leitura sem fadiga, o ganho de "espaço útil" comprimindo margens é miragem.

### d) Largura de linha

Alvo: **65–75 caracteres por linha**. Não passar de 80. Acima disso o olho perde a próxima linha. Margens da letra (c) entregam essa largura quando combinadas com fonte 12pt.

### e) Hierarquia visual

H1 (capítulo / "I — DA TEMPESTIVIDADE") — sans-serif peso 700, 16pt, espaço acima 18pt, espaço abaixo 6pt, alinhado à esquerda. Numeração em **algarismos romanos** (I, II, III).

H2 (seção / "III.4 — Da multa cominatória") — sans-serif peso 600, 14pt, espaço acima 12pt, espaço abaixo 4pt. Numeração **arábica composta** (3.1, 3.2 OU "III.4" no estilo já usado pelo escritório — manter consistência por peça).

H3 (subitem) — sans-serif peso 600 em itálico, 12pt, espaço acima 8pt.

Pedido final ("Pelo exposto, requer…") em parágrafo isolado, espaço duplo acima e abaixo, em peso normal — destaque vem do branco ao redor, não do negrito.

### f) Ênfase

**Negrito** — só para tese central de capítulo. Limite duro: 1 frase por capítulo, no máximo 2. Uso massivo destrói o sinal — quando tudo é negrito, nada é negrito.

*Itálico* — termos técnicos em latim (*data venia*, *in casu*, *ad cautelam*, *non reformatio in pejus*), nomes de obras, citações curtas no fluxo do parágrafo (junto com aspas).

Sublinhado — **nunca**. Resíduo de máquina de escrever; em PDF cria conflito visual com hyperlink.

LETRA MAIÚSCULA — só pra siglas (CPC, STJ, TJSC, OAB, ACP, ILPI), nome de partes em cabeçalho de peça e títulos canônicos do tipo "EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) RELATOR(A)…". Não usar maiúscula para "destacar" frases — isso é variação de negrito mal disfarçada.

### g) Citações

Citação literal **curta** (até 3 linhas): entre aspas, no fluxo do parágrafo, fonte e tamanho normais.

Citação literal **longa** (4 linhas ou mais): block quote — recuo de 4cm à esquerda, fonte 11pt (1pt menor que o corpo), sem aspas, espaço acima e abaixo de 6pt.

Toda citação leva referência ao final ou em rodapé: tribunal, número, relator, data, decisão. Para acórdãos do TJSC/STJ/STF, sempre o número do processo + ementa parcial + portal oficial.

### h) Espaço em branco (whitespace)

Cada capítulo começa em página nova (**\\newpage** automático no template) OU separado por dois espaços de entrelinha do final do capítulo anterior — escolher um modo por peça e manter. Padrão deste template: capítulos numerados em página nova; subseções no fluxo.

Não comprimir margens nem entrelinhas para "ganhar espaço". Peça compacta lê pior — desembargador cansado abandona o argumento antes de chegar ao pedido.

### i) Numeração de página + cabeçalho

Numeração no rodapé direito, fonte 9pt, sans-serif (mesma família dos cabeçalhos).

Cabeçalho (página 2 em diante): nome do processo abreviado à esquerda em fonte 9pt, sans-serif, cor cinza médio — informação contextual que orienta o leitor sem competir com o corpo.

Página 1 sem cabeçalho. Numeração na página 1: opcional, pode omitir.

### j) Anexos

Numerados em romanos (Anexo I, Anexo II, Anexo III). Cada anexo começa em página nova com título H1. Se houver mais de três anexos, somar **sumário inicial dos anexos** logo após o pedido — uma página listando "Anexo I — Procuração; Anexo II — Cálculo de preparo; …".

---

## 3. Quando aplicar / Quando NÃO aplicar

### Aplica
- Apelação, contrarrazões, recurso especial, recurso extraordinário, agravo de instrumento, embargos de declaração.
- Petição inicial, contestação, manifestação técnica de fundo.
- Mandado de segurança, ação civil pública, ação popular.
- Parecer jurídico endereçado a cliente, conselho, órgão.
- Defesa administrativa em órgão regulador (ANS, ANVISA, vigilâncias, conselhos profissionais).

### Não aplica
- Minuta administrativa interna do escritório (ofício ao cartório, comunicado, formulário).
- Contrato — tipografia própria, com cláusulas numeradas em fonte e estilo distintos; usar template de contrato do escritório, não este.
- E-mail e WhatsApp ao cliente — comunicação informal segue tipografia do canal.
- Procuração — instrumento formal, segue padrão do tribunal/cartório de destino.
- Documento que será lido apenas em tela curta (formulário, despacho de 1 página) — o ganho marginal não compensa a sobrecarga de pipeline.

Em dúvida, **aplicar**. O custo marginal de gerar PDF nesta tipografia é zero — o template já faz o trabalho.

---

## 4. Template + automação

**Pipeline.** Pandoc 2.9+ com engine XeLaTeX, template `.claude/agents/peca-pdf-template/`.

**Arquivos do template:**
- `peca.tex` — template LaTeX implementando todas as regras desta seção (margens, fontes, hierarquia, citações, cabeçalho, rodapé).
- `pandoc-config.yaml` — configuração Pandoc com metadados default (fontes, tamanhos, linha, idioma pt-BR, hyphenation pt-BR).
- `README.md` — instruções de invocação e troubleshooting.

**Como invocar (manual):**
```bash
pandoc "Apelação - Rascunho 2026-05-07.md" \
  --template=.claude/agents/peca-pdf-template/peca.tex \
  --pdf-engine=xelatex \
  --metadata-file=.claude/agents/peca-pdf-template/pandoc-config.yaml \
  -o "Apelação - Rascunho 2026-05-07.pdf"
```

**Como invocar (via bot):** TODO consolidação — bots redatores (Hermes, Astreia, Atena, Hestia, Têmis e demais do panteão jurídico) recebem instrução em sessão posterior. Linha-padrão a inserir: *"Output PDF segue [[_Sistema/Padrões de Trabalho/Tipografia Jurídica|Padrão Tipografia Jurídica]] via `.claude/agents/peca-pdf-template/`."* Ver §6 abaixo.

**Limitação atual do pipeline.** Crimson Pro, EB Garamond, Source Sans 3 e Inter não estão instaladas no ambiente Cowork por default. O template usa fallback **Lora** (corpo) + **Poppins** (cabeçalhos) — ambas Google Fonts já instaladas. Quando Gabriel rodar o pipeline localmente em ambiente com Crimson Pro instalada, o template detecta e usa automaticamente (variável `mainfont` no preâmbulo).

---

## 5. Quando consolidar nos bots

Esta seção é deliberadamente um TODO — não atualizar agora.

Razão: roda em paralelo com (a) tarefa de propagação juris-search nos bots e (b) Triador de Carteira. Editar prompts dos bots agora abriria conflito write/write com (a). Consolidação fica para sessão posterior, depois das duas tarefas paralelas terminarem. Aplicar o protocolo de Resolução de Conflitos em Tarefas Paralelas †.

**Bots a instrumentar (lista para sessão de consolidação):**
- Dra. Débora (orquestrador jurídico)
- Filipe (recursal)
- Judite (cível)
- Raquel (constitucional/MS)
- Marta (administrativo/regulatório)
- Tiago (trabalhista)
- Rebeca, Lázaro, Caleb, Maria, Lia (demais especializados conforme [[_Sistema/Repositório de Doutrina/99 - Doutrina por Bot Especializado|99 - Doutrina por Bot Especializado]])

Cada bot recebe um bloco `## TIPOGRAFIA DO OUTPUT PDF` com instrução de invocação do template.

---

## 🔗 Conexões
- 🖋️ Template Pandoc/LaTeX: peca-pdf-template †
- 📜 [[Pesquisa de Jurisprudência Obrigatória]] — pareado: conteúdo jurídico passa por juris-search; forma passa por este Padrão.
- 🛡️ Protocolo Risco Calibrado † — peça em camada amarela ou vermelha sai com tipografia própria.
- 🕒 [[Estimativa de Tempo por Tarefa]] — toda regeneração de PDF abre com estimativa.
- 🔀 Resolução de Conflitos em Tarefas Paralelas † — instruções de bot ficam para consolidação posterior.
- 🧠 [[00 - Cérebro Central|Cérebro Central]] — registro pendente até consolidação.
- 🎯 [[Active Context 2|Active Context]] — registro pendente até consolidação.
- 🧬 [[_Sistema/Persona Gabriel/00 - Persona Gabriel|Persona Gabriel]] — direto ao ponto, sem ornamento, é tipografia também.
- 🤖 [[_Sistema/Repositório de Doutrina/99 - Doutrina por Bot Especializado|99 - Doutrina por Bot Especializado]] — bots a instrumentar na consolidação.
- 📚 Referência canônica: Matthew Butterick — *Typography for Lawyers* (typographyforlawyers.com — recurso online gratuito).

#padrao #tipografia #peca #redacao #pdf #butterick
