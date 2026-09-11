# A casa reunida — mapa do que veio de onde (06/09/2026)

Até 05/09/2026 o trabalho da casa estava espalhado por sete branches deste mesmo repositório,
cada uma o produto de uma sessão diferente e nenhuma enxergando as outras. Em 06/09/2026 tudo o
que essas branches produziram foi copiado para cá, em duas alas separadas pelas travas.

**A reunião copiou, não moveu.** As branches de origem seguem intactas no remoto, com seu
histórico. Nada foi apagado. Quem apaga branch é o Gabriel.

---

## 1. Quatro coisas antes de qualquer trabalho

### 1.1 ⏰ O prazo do Ev. 25 venceu em 04/09/2026 — confirmar hoje se foi protocolado

O `CHECKLIST-PROTOCOLO.md` do caso ACP registra: **prazo fatal sexta-feira, 04/09/2026,
23h59min59s**, sob **pena de deserção**. As três peças e a procuração foram preparadas em
02/09/2026, com meta de protocolar no mesmo dia, e o preparo de **R$ 720,00** consta pago em
02/09/2026 (Ev. 31).

Não há neste material nenhum registro de protocolo: nem número de evento, nem comprovante. Isso
**não significa que o prazo foi perdido** — significa que a sessão da nuvem não tem como saber,
porque o eproc é inalcançável daqui. Estado do campo: **VAZIO**.

| Campo | Valor | Coordenada |
|---|---|---|
| Prazo final | 04/09/2026, 23h59min59s | `auditoria/CHECKLIST-PROTOCOLO.md`, linha 3 (Ev. 27) |
| Pena | deserção | idem (CPC art. 99, § 2º; Súmula 481/STJ) |
| Preparo | R$ 720,00, pago em 02/09/2026 | idem, seção A (Ev. 31) |
| Protocolo efetivado | **VAZIO — não apurável sem o eproc** | VAZIO |

**Próximo ato do Gabriel:** abrir o eproc 2º grau no processo 0900193-90.2016.8.24.0064 e ver se
o Ev. 27 está baixado e se há evento de protocolo posterior ao 32. Se foi protocolado, anotar o
número do evento aqui. Se não foi, o prazo é perdido e não se apaga: mede-se o dano (deserção da
apelação) e levanta-se o remédio, com a auditoria de preparo já pronta em
`casos/ACP-0900193-90.2016.8.24.0064/2026-09-02-cumprimento-ev25/auditoria/`.

### 1.2 🚩 As peças do caso ACP não estão em estado de protocolo

Conferido em 06/09/2026 abrindo os arquivos, não por leitura do checklist. São três defeitos, e
os três são do tipo que os gates da casa existem para pegar. Nenhum gate rodou, porque a
ferramenta que gerou esses arquivos não tem gate nenhum.

**a) Oito notas internas ficaram visíveis no texto entregue.** O próprio checklist manda, na
seção A: "Remover das peças, antes de assinar, todas as marcações entre colchetes [CONFERIR …]".
Elas seguem lá, e não só no markdown: vazaram para o DOCX e para o PDF.

| Arquivo | Marcações no DOCX | Marcações no PDF |
|---|---|---|
| `01-peticao-cumprimento-ev25` | 4 | 4 |
| `02-procuracao-ad-judicia` | 0 | 0 |
| `03-regularizacao-cadastro-intimacao-exclusiva` | 4 | 4 |

Uma delas, no PDF da peça principal, diz literalmente "[CONFERIR NO EPROC ANTES DE PROTOCOLAR:
meio de pagamento …]". É bastidor do escritório dentro do documento que iria aos autos.

**b) Os PDF carregam metadado que denuncia a produção automatizada.** Nenhum foi limpo:

```
title:    about:blank
creator:  Mozilla/5.0 (X11; Linux x86_64) … HeadlessChrome/141.0.0.0 Safari/537.36
producer: Skia/PDF m141
```

Um documento de escritório em São José/SC declarando-se feito em Chrome headless sobre Linux é
exatamente o rastro que a regra forense da casa (24/08/2026) manda apagar, e que o módulo
`metadados_pdf` faz nos geradores em Python — o mesmo módulo que não veio (item 5.2).

**c) A tipografia é a revogada.** Detalhe medido no item 5.1.

**O que não fiz, e por quê.** Não limpei as marcações nem regenerei nada. Cada `[CONFERIR …]` é
uma conferência que só se faz dentro do eproc, com a credencial do Gabriel; apagar a marca sem
fazer a conferência não conserta a peça, esconde que ela está por fazer. E se as peças já foram
protocoladas, mexer nos arquivos cria divergência com o que está nos autos.

**Próximo ato do Gabriel**, na ordem: (1) descobrir se protocolou (item 1.1); (2) se **não**
protocolou, fazer as oito conferências no eproc, apagar as marcações, regenerar e só então
assinar; (3) se **protocolou**, ver no evento juntado qual versão subiu, e avaliar se cabe
petição de substituição por erro material.

### 1.3 🔓 Este repositório é público

Conferido em 06/09/2026 na API do GitHub: `"private": false`. O repositório
`gfdoes-cyber/residencial-geriatrico-sagrada-familia` é **público**, descrito como "Website do
Residencial Geriátrico Sagrada Família". GitHub Pages está desligado (`has_pages: false`), mas
o código-fonte é legível por qualquer pessoa e indexável.

Isso já era verdade antes desta reunião: o material dos casos foi enviado para cá pelas sessões
anteriores, em branches deste mesmo repositório público. A reunião não aumentou a exposição —
apenas a tornou visível num lugar só. O que está exposto hoje:

| O que | Onde |
|---|---|
| CPF, RG, estado civil e endereço residencial do Gabriel | `casos/ACP-.../pecas/02-procuracao-ad-judicia.md` e os `.docx`/`.pdf` ao lado |
| CNPJ, NIRE e termo de autenticação na JUCESC da Antunelli e Antunelli | idem |
| Peças, dossiê de fatos e auditoria de um processo em curso | `casos/ACP-0900193-90.2016.8.24.0064/` |
| Método interno, caderno de erros e régua tipográfica do escritório | `advocacia/tipografia-e-geradores/` |

**Decisão que é do Gabriel, e só dele.** Duas saídas, não excludentes:

1. **Tornar o repositório privado** (Settings → General → Danger Zone → Change visibility). Custo:
   se um dia o site do Residencial for publicado por Pages a partir daqui, isso precisa de plano
   pago ou de outro caminho de publicação.
2. **Separar as duas empresas em dois repositórios**, que é a decisão já registrada no `CLAUDE.md`
   da raiz: o material da advocacia (`casa/advocacia/` e `projeto-claude-espirito-santo-advocacia/`)
   vai para o repositório próprio do escritório, e este fica só com o Residencial.

Enquanto isso não acontece: **nada de `casa/advocacia/` pode ir para caminho publicado** deste
repositório — nem `index.html` da raiz, nem `CNAME`, nem workflow de Pages. Site do escritório e
site da ILPI saindo do mesmo domínio é problema das travas 1 e 3, não questão de arrumação.

> Tornar privado não apaga o passado: o que já foi enviado a um repositório público pode ter sido
> copiado ou indexado. Trocar a visibilidade reduz a exposição daqui para a frente; não a desfaz.

### 1.4 📄 O parecer do 5026537 segue retido desde 04/09/2026

`casos/5026537-50.2020.8.24.0018/PARECER-RETIDO.md` está retido porque os autos nunca chegaram, e
traz um alerta que dizia "verificar hoje" — e aquele "hoje" era 04/09. Já se passaram dois dias.
Há ainda uma divergência aberta: o link informado é do processo **5026537-50.2020.8.24.0018** e a
branch de trabalho citava **5001125**. São processos distintos, e qual é o alvo continua VAZIO.

**Próximo ato do Gabriel:** confirmar o número, e no eproc fazer *Download Completo → Baixar Todas
as Partes (ZIP)* (o link expira em 72 horas), entregando o ZIP para a leitura integral.

### 1.5 📋 A carteira do eproc segue VAZIA — pedido ao cliente de 11/09/2026

Em 11/09/2026 o Gabriel pediu a análise de **todos os processos do escritório** a partir do
relatório de processos do procurador no eproc de 1º grau. A sessão da nuvem não alcança o eproc
(política de rede do ambiente e `deny` no `settings.json`), e o relatório só existe atrás da
credencial dele. O parecer ficou **retido** e saiu o primeiro artefato da regra do portador:
`advocacia/casos/2026-09-11-carteira-eproc-relatorio-retido.html`.

O que ele registra: o inventário dos quatro processos que a casa conhece (ACP 0900193-90 com o
protocolo de 04/09 ainda VAZIO; incidente 5049926-11 encerrado; 5026537-50 retido e com o número
em dúvida; 5007704-35 com o estado atualizado pelo registro do vigia que chegou no merge de
11/09), os sete números que são precedentes e não processos
da casa, os prazos como itens abertos e a lista do que entregar: os relatórios do **1º e do 2º
grau** em PDF, o vetor de cada processo, o ZIP integral de cada um, a tela de prazos e as três
respostas pendentes (protocolo da ACP, 5026537 × 5001125, o ato aguardado do 5007704).

⚠️ O registro `advocacia/rotinas/vigia-djen-5007704.md` traz dados de um processo reservado, e
este repositório é público (item 1.3). Entra na lista do que a decisão do item 1.3 precisa cobrir.
Por isso a versão atualizada do relatório de 11/09 e o parecer retido dos dois processos pedidos
no mesmo dia ficaram fora do repositório, entregues em privado ao Gabriel.

**Próximo ato do Gabriel:** anexar os arquivos do item V do relatório, ou abrir a sessão de
Remote Control no Mac, onde o eproc responde.

---

## 2. O mapa: de onde veio cada coisa

Cento e seis arquivos, de seis branches. Nenhum arquivo foi editado ao ser trazido, salvo uma
nota datada no README do caso ACP, avisando que a ferramenta de gerar DOCX e PDF mudou de pasta.

### Ala da advocacia

| Onde está agora | Arquivos | Veio de | Commit · data |
|---|---|---|---|
| `advocacia/tipografia-e-geradores/` | 33 | `claude/analise-pecas-processuais-l9f1i1` | `a7c9662` · 02/09/2026 |
| `advocacia/casos/ACP-0900193-90.2016.8.24.0064/` | 39 | `claude/auditoria-processo-judicial-tjfklb` | `0337b39` · 02/09/2026 |
| `advocacia/ferramentas-docx-pdf/` | 4 | idem (estava em `tools/`, fora de `juridico/`) | `0337b39` · 02/09/2026 |
| `advocacia/casos/5026537-50.2020.8.24.0018/` | 1 | `claude/parecer-processo-5001125-l87z4z` | `ef1ea4d` · 04/09/2026 |
| `advocacia/paginas/formacao-acp.html` | 1 | `claude/acp-especializacao-mestrado-doutorado-vyjt3n` | `9771c40` · 28/08/2026 |
| `advocacia/paginas/` (site e teleprompter) | 2 | `claude/gfes-skills-audit-13jul-ka2vbo` | `03eb3b5` · 30/07/2026 |
| `advocacia/acervo-2026-07-30/` | 5 | idem | `03eb3b5` · 30/07/2026 |

### Ala do Residencial

| Onde está agora | Arquivos | Veio de | Commit · data |
|---|---|---|---|
| `residencial/site/index.html` | 1 | `claude/oi-gmeoip` | `10d7c35` · 05/09/2026 |
| `residencial/app-ios/` | 13 | idem | `10d7c35` · 05/09/2026 |
| `residencial/documentos/` | 7 | `claude/gfes-skills-audit-13jul-ka2vbo` | `03eb3b5` · 30/07/2026 |

O `index.html` de 1 byte que cada branch carregava não foi trazido: é arquivo vazio, resíduo do
repositório original. O da branch `oi-gmeoip` é o único de verdade, com 67 KB, e está em
`residencial/site/`.

### ⚠️ O acervo de 30/07/2026 está superado — não é fonte

`advocacia/acervo-2026-07-30/` guarda o `CLAUDE.md`, o `STATUS.md` e a skill `assistente-juridico`
como estavam em 30/07/2026. Fica aqui como **história, não como regra**. Aquele texto é anterior
ao prédio único (28/08/2026), ao RADAR ÚNICO (04/09/2026) e à raiz permanente (05/09/2026); fala
em coisas que a casa revogou. Regra vigente é a do `CLAUDE.md` da raiz e a das skills em
`.claude/skills/`. Em caso de divergência, **vence o mais novo**, sempre.

---

## 3. O que continua só no Mac — e não veio

O que chegou é uma fatia do que a casa tem. A fonte única do plugin `gfes` 1.4.0 vive no vault do
Obsidian, em `Advocacia/02 - SKILLS E AGENTES/`, e a sessão da nuvem não alcança o disco do Mac.

| Não veio | Onde está |
|---|---|
| As 21 skills e os 6 agentes do plugin `gfes` 1.4.0 | fonte única no vault do Mac |
| Os 8 gates (aqui só chegaram 2: paginação e diagramação) | idem |
| O terceiro gerador na versão da regra 35, com a janela `[!linha]` | idem |
| Os 64 códigos do Planalto de `direito-civil-avancado` | idem |
| O vault inteiro: Sede, radar, índice de clientes, os outros casos | vault do Obsidian |
| A esteira de PDF e a rotina de WhatsApp | `03 - ESTEIRA/` e `rotinas/` no Mac |

**Como trazer o que falta, se for a vontade do Gabriel:** só uma sessão com mãos na máquina pode
ler o vault e enviar para cá. É a sessão de Remote Control, aberta no Mac conforme o `CLAUDE.md`
da raiz. Uma sessão da nuvem, como a que escreveu este mapa, nunca terá esse alcance.

Antes de trazer, porém, resolva o item 1.3: **enquanto este repositório for público, trazer o
vault para cá é ampliar a exposição**, não organizá-la.

---

## 4. As travas aplicadas a esta pasta

| Trava | Como ela vive aqui |
|---|---|
| ⛔ 1 — publicidade não se mistura | `advocacia/paginas/` e `residencial/site/` são alas separadas e **nenhuma das duas está publicada**. Não junte as duas num mesmo domínio, conta de anúncio ou landing. |
| 🔒 2 — dado de saúde de residente | Não há dado de saúde de residente neste material. O caso ACP tem a Antunelli como parte, não os residentes. Modelos em `residencial/documentos/` são formulários em branco: mantenha-os assim, sem preencher com pessoa real. |
| 💰 3 — contas e CNPJ não se misturam | As duas empresas aparecem aqui porque a ILPI é cliente do escritório neste processo. Isso é lícito e está declarado na procuração. O que não pode é conta, contrato, nota ou domínio comum — e é por isso que a separação em dois repositórios está no item 1.3. |

## 5. Pendências técnicas apuradas em 06/09/2026

Conferidas rodando o código e lendo a fonte, não por leitura de documentação.

### 5.1 ⚠️ Os DOCX e PDF do caso ACP saíram com medidas revogadas

A ferramenta em `advocacia/ferramentas-docx-pdf/` foi escrita com a tipografia antiga. Os `.md`
das três peças estão corretos: o problema é só a renderização. Comparando o código da ferramenta
com `tipografia-vigente.json` (que se declara vigente desde 02/09/2026):

| Medida | Ferramenta que gerou o caso | Régua vigente | Situação |
|---|---|---|---|
| Entrelinha | 1,5 | 1,35 | **revogada em 27/08/2026** |
| Margem direita | 2 cm | 3 cm | **revogada em 27/08/2026** |
| Citação em bloco | recuo 4 cm, 11 pt | recuo 3 cm, Charter 11 | **revogada em 27/08/2026** |
| Margem superior / inferior | 3 / 2,5 cm | 2,3 / 1,8 cm | divergente |
| Recuo de 1ª linha | 1,25 cm | 2 cm | divergente |
| Espaço entre parágrafos | 6 pt | nenhum | divergente |
| Sublinhado | suportado (`__texto__`) | **proibido** | contra a regra |

Coordenadas: `ferramentas-docx-pdf/md2pdf.js`, linhas 39, 40, 41 e 46; `gen_docx.js`, linhas 1,
26 e 117; a lista do que foi revogado está no campo `revoga` de
`advocacia/tipografia-e-geradores/instalar/skills/assistente-juridico/references/tipografia-vigente.json`.

É exatamente o erro que fez a casa criar aquele JSON: uma peça declarada conforme a regra, medindo
valores já revogados, porque a conferência foi contra a memória e não contra a camada mais nova.

Isto é **forma, não mérito**: nada aqui invalida juridicamente as peças. Mas se elas foram
protocoladas, foi nessa forma. **Próximo ato:** decidir se regenera. Os `.md` do caso já usam
`@@`, `#`, `##` e `**Rótulo:**`, que é a marcação que o gerador da casa entende; a adaptação é
pequena, e passa por tirar o sublinhado e converter as transcrições `>` para janela `[!cita]`.

### 5.2 Os geradores em Python não rodam a partir do que veio

Os três importam `metadados_pdf`, o módulo forense que limpa o rastro do PDF, e ele **não veio em
nenhuma branch**. É `import` de topo: aborta antes de qualquer coisa. Testado aqui em 06/09/2026.

Faltam também três dos gates que os geradores chamam:

| Gate | Chegou? |
|---|---|
| `validar_diagramacao.py` · `validar_paginacao.py` | sim |
| `validar_norma_culta.py` · `validar_ficha_de_fatos.py` · `validar_admissibilidade.py` | **não** |

**A armadilha:** os gates que faltam degradam com um simples `[aviso] ... não encontrado; gerando
sem gate` e o PDF sai assim mesmo (`gerar_pdf.py`, linhas 886, 899 e 931). Ou seja: basta alguém
copiar um `metadados_pdf.py` qualquer para o lugar e o gerador passa a produzir PDF que parece
pronto tendo passado por dois gates dos cinco. Quem trouxer os arquivos que faltam, traga todos.

### 5.3 A skill de tipografia desta sessão está uma camada atrás

`.claude/skills/tipografia-da-casa/SKILL.md` diz "vigente desde 27/08/2026". O JSON diz
`vigente_desde: 2026-09-02` e traz o adendo dos 14 itens (versalete em títulos, numeração
automática por `@numerar`, quadro `[!requerimentos]`, quadro de tutela em duas colunas,
`[provatrio]`, `[provaquadro]`, seta no `[provapar]`, CPC art. 425, VI como fundamento do print).
**As medidas batem** — Times 12, entrelinha 1,35, recuo 2 cm, citação Charter 11 a 3 cm, margens
2,3/3/1,8/3, órfãs e viúvas 2/2. O que falta na skill são os 14 itens novos, não a régua.

## 6. Como regenerar uma peça

Os `.md` são a fonte; `.docx` e `.pdf` são derivados. Hoje há **dois caminhos, e nenhum dos dois
está pronto para fechar peça** — leia o item 5 antes de usar qualquer um.

**Caminho A, a ferramenta em Node** (`advocacia/ferramentas-docx-pdf/`, Node mais `docx` e
Playwright; `build.sh` gera ainda os PNG de conferência com PyMuPDF). Roda, mas **com a
tipografia revogada do item 5.1**. Serve para rascunho e conferência de conteúdo, não para a peça
que vai ao processo, enquanto as medidas não forem corrigidas.

```bash
node advocacia/ferramentas-docx-pdf/gen_docx.js <peça>.md <peça>.docx
node advocacia/ferramentas-docx-pdf/md2pdf.js   <peça>.md <peça>.pdf
```

**Caminho B, os geradores da casa em Python**
(`advocacia/tipografia-e-geradores/instalar/skills/assistente-juridico/`). Leem a régua do JSON e
rodam os gates, que é o certo — mas **não iniciam**, por falta do módulo `metadados_pdf` (item
5.2). E mesmo completos, dependem do Chrome e das fontes do macOS: nesta nuvem só existe
Liberation Serif, e o PDF sairia com fonte substituta, reprovado no gate de paginação.

**A peça definitiva fecha no Mac.** Daqui saem rascunho e conferência de conteúdo, nada que se
assine ou protocole. E vale a regra da casa: PDF reprovado não se entrega, e conserta-se a peça,
nunca o gate.

## 7. O que foi conferido em 06/09/2026, e o que não foi

Registro para ninguém refazer o que já se fez, nem confiar no que não se conferiu.

### Conferido e limpo

| O que | Como | Resultado |
|---|---|---|
| Site do Residencial x trava 1 | busca por "advocacia", "OAB", CNPJ e nome do escritório no HTML | **nenhuma menção**: as duas empresas não se cruzam ali |
| Site do Residencial x rastreamento | busca por Analytics, Tag Manager, pixel da Meta, Hotjar, fonte de CDN | **nenhum**; só dois links externos, WhatsApp e Google Maps; nenhum formulário |
| Site da advocacia x Provimento CFOAB 205/2021 | busca por preço, honorário, desconto, promessa de resultado, captação | **nada de irregular**. "100%" é CSS, "garantias" é termo da LGPD, e "IA" aparece como área de atuação, não como autoria da página |
| As três páginas x envio de dados | busca por `action`, `fetch`, `XMLHttpRequest`, Formspree, Netlify | o formulário do site da advocacia **não envia a lugar nenhum**; as outras duas não têm formulário |
| `calcular_prazo.py` do acervo de julho | rodado em quatro cenários e conferido dia a dia à mão | **acerta**: DJEN com publicação no dia útil seguinte, dias úteis do CPC 219, dias corridos do CPP 798 e prorrogação do vencimento em dia não útil |
| Régua tipográfica | `tipografia-vigente.json` contra a skill da casa | **as medidas batem**: Times 12, entrelinha 1,35, recuo 2 cm, citação Charter 11 a 3 cm, margens 2,3/3/1,8/3, órfãs e viúvas 2/2 |
| Integridade da reunião | contagem arquivo a arquivo contra `git diff` de cada branch | 106 de 106; o `tools/` da branch da auditoria quase ficou para trás e foi recuperado |

### Conferido e com defeito

Estão nos itens 1.2, 5.1, 5.2 e 5.3. Em resumo: as peças do caso ACP não estão em estado de
protocolo, a ferramenta que as gerou usa medidas revogadas, os geradores em Python não iniciam,
e a skill de tipografia desta sessão está uma camada atrás do JSON.

Dois defeitos foram criados pela própria reunião e já corrigidos no mesmo dia: o README do caso
apontava para `tools/` na raiz, e o projeto Xcode apontava para o `index.html` da raiz. Ambos
agora apontam para o lugar novo.

### Não conferido — e por que fica VAZIO

| O que | Por quê |
|---|---|
| Se as peças do ACP foram protocoladas | o eproc é inalcançável daqui, e a credencial é do Gabriel |
| O teor dos Eventos 18, 23, 25, 27, 31 e 32 | idem; a própria auditoria de 02/09 já dizia não ter visto |
| Se as citações legais das peças conferem com o Planalto | não rodei o gate de citações; a auditoria de 02/09 registrou que Planalto, ALESC e TJSC estavam bloqueados para ela também |
| Se o app iOS compila | exige Xcode e macOS; aqui só se conferiu que a referência do recurso voltou a apontar para um arquivo existente |
| Se os dados de contato do site do Residencial estão certos | são **placeholders fictícios** (`(00) 0000-0000`, `contato@exemplo.com.br`, "Rua Exemplo, 123"), e o próprio README do app lista o que preencher |

E fica o alerta que o calculador de prazos não resolve sozinho: **ele não tem feriado embutido**.
Sem passar `--feriados`, ele conta feriado como dia útil. Antes de confiar num vencimento, os
feriados nacionais, estaduais, municipais e o recesso forense entram na mão.
