# Esboços tipográficos das peças do escritório — com a ligação legal de cada bloco (02/09/2026)

> **Como ler.** Cada esboço fixa a **ordem dos blocos**, o **elemento visual** de cada bloco
> (no dialeto do gerador), a **origem** do elemento (`[curso]` = aula ou modelo do professor;
> `[casa]` = regra da casa) e o **dispositivo** que exige ou autoriza o bloco. O texto dos
> artigos está no arquivo `04`, conferido na cópia do CPC que a casa mantém em disco
> (`codigos/cpc-2015.txt`). O que não foi conferido está `[VERIFICAR]`. **A lei de cada peça,
> item por item, continua sendo a skill `requisitos-das-pecas`** — este arquivo diz *onde na
> página* cada exigência mora, não substitui o checklist.
>
> **Os esboços não protocolam nada.** Saem como rascunho; assinatura e protocolo são do
> Gabriel (regra comum de `tipos-de-peca.md`).

## 0. A régua comum (não se repete nos esboços)

| Item | Valor | Fonte |
|---|---|---|
| Corpo | Times New Roman 12, justificado, hifenização ligada | `tipografia-vigente.json` |
| Entrelinha | 1,35 (16,5 pt) | idem |
| Recuo de 1ª linha | 2 cm; sem espaço entre parágrafos | idem |
| Citação em bloco | Charter 11, recuo 3 cm, entrelinha 1,3, sem itálico, sem aspas | idem |
| Margens — peça forense | 3 / 3 laterais; 2,3 topo / 1,8 pé (piso: tarja do eproc) | idem |
| Margens — contrato e procuração | 3 / 3; 2,5 / 2,0 (levam logo) | idem |
| Parecer | timbre em todas as páginas; margens próprias | idem |
| Títulos | `#` negrito azul `#1F3864` com filete; `##` negrito azul `#2E5077`; respiro após o título; título nunca no pé (`break-after: avoid`) | `padrao-formatacao-peca` 5.4; ficha técnica 27/08 |
| Vocativo | `@@`, centralizado, **sem hifenização**; 72 pt de respiro até a qualificação | regra geral III.9 |
| Destaque | negrito e itálico, 1–3 pontos por página, **por último**; nunca sublinhado, caixa-alta no corpo, marca-texto | regra geral III.2 e 1-A |
| Órfãs/viúvas | 2/2; parágrafo ≤ 265 caracteres não quebra; última página ≥ 8 linhas; assinatura nunca órfã | JSON `paginacao` |
| Vão no pé | ≤ 20 % da mancha (última página isenta); bloco alto quebra entre páginas, a **linha** nunca | `vao-no-pe-da-pagina` |
| Assinatura | `@assinatura` → nome inteiro / Advogado (ou Advogado dativo) / OAB/SC 53.040, centrado, dois espaços acima | regra 24 |
| Rodapé / timbre / numeração | nenhum na peça forense | `metodo-das-pecas`, passo 5 |
| Janelas | `[!qualif]` `[!cita]` `[!tempo]` `[!calc]` `[!dout]` `[!jur]` `[!poderes]`; eixo `~ data \| evento`, `~ !data` destaca | `janelas-e-linha-do-tempo` |
| Prova visual | `[prova]` (1 imagem) · `[provapar]` (página + zoom) · etiqueta vermelha `#9E2121` com o efeito jurídico; documento íntegro no anexo | regra 26 |
| Arquivo | PDF com camada de texto, **um arquivo por documento**, ≤ 11 MB no eproc | Res. Conj. GP/CGJ 5/2018, art. 14, § 1º; FAQ eproc |
| Gates | norma culta → admissibilidade → paginação → diagramação → forense → **vista página a página** | regra 26(b) |

**Ordem de trabalho que vale para todas** `[curso]`: texto pronto → elementos visuais no topo
de cada item → capa (SÍNTESE) por último → **diagramar imagens** → **destacar** → gates → olhar.

---

## 1. PETIÇÃO INICIAL

**Destinatário e vocativo.** `@@ EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO DA … VARA … DA COMARCA DE …` — o juízo, não o juiz pessoa (CPC 319, I). Sem vara conhecida: "…DA VARA CÍVEL A QUE COUBER POR DISTRIBUIÇÃO…" `[curso; pendente 3.12 do arquivo 02]`.
**Norma-mãe.** CPC 319 (sete incisos), 320, 287, 105; sanção: 321 (emenda com indicação precisa) e 330.

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | Vocativo + 72 pt de respiro | `@@` | casa | CPC 319, I |
| 2 | **Qualificação do autor e do réu** — os 8 dados: nome, prenome, estado civil, **união estável**, profissão, **CPF/CNPJ**, **e-mail**, domicílio e residência | `[!qualif]` (um por parte); faltando dado do réu, parágrafo invocando **separadamente** § 1º, § 2º ou § 3º | casa (janela) · curso (qualificação em destaque na capa) | CPC 319, II e §§ 1º–3º |
| 3 | **SÍNTESE** — o que se pede · por quê, com coordenada · o que se controverte, com valores · dispositivos | quadro de duas colunas (`[quadro] Síntese`) | curso (SÍNTESE PROCESSUAL em quadro) · casa (4 blocos) | CPC 188; Recom. CNJ 144/2023; RISTJ 343-A `[VERIFICAR fonte oficial]` |
| 4 | **Requerimentos preliminares** — gratuidade · prioridade · tutela · segredo · audiência de conciliação (sim/não) | quadro com ☑/☐ `[pendente 3.2]`; até lá, lista `-` | curso | CPC 98; 1.048 `[VERIFICAR]`; 300; 189 `[VERIFICAR]`; 319, VII c/c 334, § 5º |
| 5 | **Gratuidade** (se houver) | tabela receitas × despesas com coluna **"Documento relacionado"** | curso | CPC 98, 99 (§ 3º presunção só para pessoa natural) |
| 6 | **DOS FATOS** — narrativa cronológica, podada, cada fato com "Ev./doc." | `[!tempo]` no topo do item (≥ 3 datas); subtítulos `##` que dizem o fato-tese; `[provapar]` para o documento decisivo | curso (linha do tempo + subtítulo específico) · casa (regra 26) | CPC 319, III; 77, I; 330, § 1º, III (da narração deve decorrer a conclusão) |
| 7 | **DO DIREITO** — um bloco CREAC por tese; título com o instituto **e o dispositivo no rótulo** ("Art. 476 do CC — exceção de contrato não cumprido"); subtítulo com a tese em uma frase | `[!cita]` para texto de lei; `[!jur]` para 2–3 julgados **com a relevância dita no corpo**; `[!dout]` só em tese controvertida | curso (rótulo, subtítulo-tese, jurisprudência contextualizada) · casa (etiqueta completa) | CPC 319, III (fundamentos **jurídicos**, não legais); 489, § 1º, V (espelho); 80, I |
| 8 | **DA TUTELA DE URGÊNCIA** (se houver) — subtítulo diz o risco concreto | quadro de duas colunas "Probabilidade do direito" × "Perigo de dano", uma linha por fato com coordenada `[pendente 3.7]` | curso | CPC 300 (caput: os dois requisitos; § 3º irreversibilidade) `[texto: checklist 2.2 da casa]` |
| 9 | **DOS PEDIDOS** — principal → sucessivos/subsidiários rotulados → tutela → citação → procedência → custas e honorários → provas | lista alfabética `a)`, `b)`… | curso (lista alfabética) | CPC 319, IV; 322 (§ 1º implícitos: juros, correção, sucumbência); 324; 326; 327 |
| 10 | **Provas que pretende produzir** | parágrafo ou lista | — | CPC 319, VI |
| 11 | **Valor da causa** pelo critério legal | linha própria `**Valor da causa:** R$ …` | — | CPC 319, V; 291; 292 |
| 12 | **Opção pela audiência** (expressa) | uma linha | — | CPC 319, VII; 334, § 5º |
| 13 | Data + `@assinatura` | centrado, nunca órfão | casa | CPC 105, § 2º (nome, OAB); Lei 11.419, art. 2º (assinatura eletrônica) |
| — | **Anexos**: procuração com poderes especiais (inclusive **assinar declaração de hipossuficiência**) e endereços eletrônico e não eletrônico; documentos indispensáveis; um arquivo por documento | — | — | CPC 105, caput; 287; 320; Res. Conj. 5/2018, art. 14, § 1º |

**Conferência específica.** Os sete incisos do 319 marcados na peça; teste contra as quatro
hipóteses de inépcia do 330, § 1º; revisional de empréstimo/financiamento/alienação →
discriminar obrigações e quantificar o incontroverso (330, § 2º); `validar_admissibilidade.py`.

---

## 2. CONTESTAÇÃO (com reconvenção, se houver)

**Vocativo.** Ao juízo da causa, "nos autos n. …". **Prazo.** 15 dias úteis (CPC 335 + 219); sem dobro em autos eletrônicos (229, § 2º).
**Norma-mãe.** CPC 336 (toda a matéria de defesa), 337 (preliminares), 341 (impugnação especificada).

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | Vocativo + referência aos autos + qualificação do réu | `@@`; `[!qualif]` | casa | CPC 336 |
| 2 | **SÍNTESE** — quadro "Alegações autorais × posição da defesa" | quadro de duas colunas | curso ("Alegações autorais") | CPC 188 |
| 3 | **Gratuidade** do réu / impugnação à gratuidade do autor | tabela com coluna "Documento" | curso | CPC 99; 100; 337, XIII |
| 4 | **Síntese do processo** (o que já aconteceu) | `[!tempo]` curta | curso | — |
| 5 | **PRELIMINARES** — uma `##` por inciso do 337 invocado; **arbitragem e incompetência relativa primeiro** (morrem se não alegadas); valor da causa; abusividade de foro | `##` com o inciso no rótulo ("Art. 337, IV — inépcia…") | curso (rótulo) · casa (checklist 2.3) | CPC 337, I–XIII, §§ 5º–6º; 293; 63, § 4º |
| 6 | **MÉRITO — impugnação especificada, fato a fato**, espelhando a numeração da inicial | quadro **"Alegação do autor × Realidade dos fatos (doc.)"** no topo do item; depois os blocos CREAC (defesa direta e indireta, em ordem de eventualidade explícita) | curso (quadro) · casa | CPC 341 (presunção de veracidade do não impugnado; p.u. dispensa só dativo/curador/defensor); 336; 341, III (contradição interna derruba a presunção) |
| 7 | **Documentos da inicial** — manifestação e, se for o caso, falsidade | parágrafo próprio | — | CPC 437; 430 |
| 8 | **Revogação da tutela** (se houver) | quadro de duas colunas | curso | CPC 296 `[VERIFICAR]` |
| 9 | **RECONVENÇÃO** (se houver) — na mesma peça, com requisitos de inicial e **valor da causa próprio** | `#` autônomo; pedidos em lista | casa (checklist 2.4) | CPC 343; 292 |
| 10 | **Provas** — especificar; rol de testemunhas | quadro de testemunhas (nome, CPF, endereço) | curso | CPC 336, in fine |
| 11 | **Pedidos** — acolhimento das preliminares → improcedência → ônus | lista alfabética | curso | — |
| 12 | Data + `@assinatura` | — | casa | — |

**Conferência específica.** Varredura dos 13 incisos do 337; teste de que **nenhum fato da
inicial ficou sem impugnação precisa**; a trava de admissibilidade exige tópico com a palavra
"preliminar" (PREL-01) — se a defesa for direta ao mérito, escrever "Não há preliminares" e
passar `--tipo` explícito.

---

## 3. RÉPLICA

**Gatilho e prazo.** Fato impeditivo/modificativo/extintivo (CPC 350) ou preliminar (351): 15 dias úteis, **com direito a prova**.

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | Vocativo curto + autos | `@@` | casa | — |
| 2 | **SÍNTESE** — quadro "Alegações defensivas × resposta" | quadro | curso | CPC 188 |
| 3 | **Impugnação às preliminares** — uma `##` por preliminar | `##` com o inciso no rótulo | curso | CPC 351 |
| 4 | **Impugnação ao mérito da contestação** — refutar tese, não pessoa; enunciar em uma frase, refutar em três | blocos CREAC; `[!cita]` do trecho da contestação que se refuta, com coordenada | casa (`metodo-das-pecas`, 6) | CPC 350 |
| 5 | **Documentos novos** juntados com a contestação; falsidade | parágrafo | — | CPC 437; 430 |
| 6 | **Requerimento de prova** (contraprova do fato extintivo) | lista | casa (checklist 2.5) | CPC 350 e 351 ("permitindo-lhe a produção de prova") |
| 7 | Reiteração dos pedidos iniciais | um parágrafo | curso | — |
| 8 | Data + `@assinatura` | — | — | — |

---

## 4. MANIFESTAÇÃO (impugnação a laudo, cumprimento de despacho, petição intercorrente)

A peça mais curta do repertório (o modelo do curso tem 12 parágrafos). **Sem SÍNTESE quando
couber em uma página**; com SÍNTESE quando passar de duas.

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | Vocativo + autos | `@@` | — | — |
| 2 | **O ato a que responde**, com data e evento | `[!cita]` do despacho/laudo, rótulo com a coordenada | casa | regra do portador |
| 3 | **Um `#` por ponto**, com o dispositivo no rótulo (ex.: "Art. 477, § 2º — esclarecimentos do perito") | `##`; `[provapar]` quando impugnar trecho de laudo | curso (rótulo) | CPC 477 `[VERIFICAR]` (laudo); prazo do despacho |
| 4 | **Pedidos** (ex.: nova perícia, esclarecimentos) | lista | curso | — |
| 5 | Data + `@assinatura` | — | — | — |

---

## 5. EMBARGOS DE DECLARAÇÃO

**Destinatário.** O próprio órgão prolator (juiz, relator ou colegiado). **Prazo.** **5 dias úteis** no cível (CPC 1.023; 219) — **2 dias corridos no penal** (CPP 619 e 798; caderno IV-bis). Sem preparo.

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | Vocativo + autos + decisão embargada (evento) | `@@` | — | CPC 1.023, caput ("petição dirigida ao juiz") |
| 2 | **SÍNTESE DO RECURSO** — quadro "Vício constatado × ponto da decisão × o que se pede" | quadro | curso ("Vício constatado") | CPC 1.023 ("com indicação do erro, obscuridade, contradição ou omissão") |
| 3 | **TEMPESTIVIDADE** — seção autônoma | `[!tempo]`: disponibilização no DJe → publicação (1º dia útil seguinte) → início do prazo → **✔ protocolo** → último dia; **regime de contagem escrito no topo** | curso (eixo do prazo em todo recurso) · casa (caderno IV-bis) | CPC 224, §§ 2º–3º; 219; 1.023; Lei 11.419, art. 4º, §§ 3º–4º, e art. 5º, § 3º (intimação tácita no 10º dia corrido) |
| 4 | **CABIMENTO** — o inciso do 1.022 nomeado; se omissão qualificada, **o inciso do 489, § 1º** nomeado | `##` com o inciso no rótulo | curso · casa (checklist 2.13) | CPC 1.022, I–III e p.u.; 489, § 1º |
| 5 | **Pontos a serem esclarecidos** — um `##` por vício; **o trecho da decisão em imagem** quando o vício for de leitura | `[!cita]` do trecho com coordenada; `[provapar]` da folha da decisão com etiqueta "aqui a decisão não enfrenta o argumento X" | curso (print em ED "revela a omissão") · casa | CPC 1.022; 489, § 1º, IV |
| 6 | **Prequestionamento** (se houver recurso posterior) — nomear artigo e questão | parágrafo | casa | CPC 1.025 (condicionado) |
| 7 | **Pedidos** — sanar o vício; efeitos infringentes só se decorrerem do saneamento; contraditório do 1.023, § 2º | lista | — | CPC 1.023, § 2º; 1.026 (interrompe) |
| 8 | Data + `@assinatura` | — | — | — |

**Conferência específica.** Contar quantos ED já houve (1.026, §§ 2º–4º); contradição tem de ser
**interna** à decisão (Súmula 56/TJSC).

---

## 6. APELAÇÃO — duas peças em um arquivo

**Destinatário.** A petição de interposição ao **juízo de primeiro grau** (CPC 1.010, caput; § 3º: sem juízo de admissibilidade); as razões ao **Tribunal de Justiça** (Câmara). A bipartição é praxe — o art. 1.010 fala em petição única (checklist 2.10).
**Prazo.** 15 dias úteis (1.003, § 5º; 219). **Preparo no ato** (1.007); porte dispensado em autos eletrônicos (§ 3º); **no TJSC, gratuidade e preparo não se cumulam** (Súmula 51/TJSC).

**Peça 1 — Interposição (1 página)**

| # | Bloco | Elemento | Fundamento |
|---|---|---|---|
| 1 | Vocativo ao juízo de 1º grau + autos | `@@` | CPC 1.010, caput |
| 2 | Interposição, **tempestividade** (eixo curto), **preparo** (guia e valor) ou gratuidade | `[!tempo]`; `[!calc]` com o preparo | CPC 1.003, § 5º; 1.007; 1.003, § 6º (feriado local comprovado no ato) |
| 3 | Pedido de intimação do apelado e remessa | parágrafo | CPC 1.010, §§ 1º e 3º |
| 4 | Data + `@assinatura` | — | — |

**Peça 2 — Razões (página nova)**

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | `@@ EGRÉGIO TRIBUNAL DE JUSTIÇA DE SANTA CATARINA` · `@@ Colenda … Câmara de Direito Civil` | `@@` | — | — |
| 2 | **Apelante / Apelado** com **qualificação** | `[!qualif]` | curso | CPC 1.010, I ("nomes **e qualificação**") |
| 3 | **SÍNTESE** — quadro "Capítulo da sentença × fundamento × por que reformar" | quadro; **um item por fundamento suficiente da sentença** | curso · casa (dialeticidade) | CPC 1.010, II–IV; 932, III; Súmula 283/STF por analogia |
| 4 | **Preliminares recursais** — interlocutórias não agraváveis (1.009, § 1º); nulidade da sentença (489, § 1º); efeito suspensivo nas exceções do 1.012, § 1º | `##` com o inciso no rótulo | casa (checklist 2.10) | CPC 1.009, § 1º; 1.012; 1.013, § 5º |
| 5 | **Fundamentos para reforma** — um `#` por capítulo atacado, título com o instituto, subtítulo com a tese; erro de valoração de prova → `[provapar]` da prova mal lida com etiqueta | `[!cita]` do trecho da sentença atacado (coordenada); `[provapar]`; `[!jur]` 2–3 | curso (erro na valoração da prova, omissão, erro de interpretação) | CPC 1.010, III; 1.013 |
| 6 | **Pedidos** — conhecimento → reforma/anulação, capítulo a capítulo → honorários recursais | lista alfabética | curso | CPC 1.010, IV; 85, § 11 `[VERIFICAR]` |
| 7 | Data + `@assinatura` | — | — | — |

**Conferência específica.** Lista dos fundamentos da sentença com "✔ atacado" ao lado de cada
um (fundamento autônomo não impugnado = recurso inteiro inadmitido).

---

## 7. CONTRARRAZÕES (de apelação ou de agravo)

**Prazo.** 15 dias úteis (1.010, § 1º; 1.019, II). Espelham o recurso.

| # | Bloco | Elemento visual | Fundamento |
|---|---|---|---|
| 1 | Vocativo (juízo de 1º grau, que remete) + autos | `@@` | CPC 1.010, § 1º |
| 2 | **SÍNTESE** — quadro "Razão do apelante × resposta × onde a sentença acertou" | quadro | CPC 188 |
| 3 | **Preliminares de não conhecimento** — intempestividade (eixo do prazo do adversário), deserção (1.007), falta de dialeticidade (932, III), inovação (1.014), **precedente inexistente na peça adversa** (má-fé + ofício à OAB) | `[!tempo]`; `[!jur]` com os dois acórdãos da 8ª CDCiv do TJSC | CPC 1.003, § 5º; 1.007; 932, III; 80–81; TJSC AC 5052490-98.2020 e 5010774-94.2022 |
| 4 | **Questões do 1.009, § 1º** que a parte quer devolver | `##` | CPC 1.009, §§ 1º–2º |
| 5 | **Mérito recursal** — defender a sentença capítulo a capítulo, na ordem das razões | `[!cita]` da sentença; `[provapar]` | CPC 1.013 |
| 6 | **Pedidos** — não conhecimento → desprovimento → majoração dos honorários | lista | CPC 85, § 11 `[VERIFICAR]`; Súmula 52/TJSC |
| 7 | Data + `@assinatura` | — | — |

---

## 8. AGRAVO DE INSTRUMENTO

**Destinatário.** **Diretamente ao tribunal** (1.016, caput). **Prazo.** 15 dias úteis. **Custas** acompanham a petição (1.017, § 1º). **Autos eletrônicos dispensam as peças do 1.017, I e II** (§ 5º) — mas juntar a decisão agravada e a certidão de intimação continua sendo o que prova a tempestividade.

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | `@@ EGRÉGIO TRIBUNAL…` + Câmara | `@@` | — | CPC 1.016, caput |
| 2 | **Agravante / Agravado** — nomes; **nome e endereço completo dos advogados de ambas as partes** | `[!qualif]` (incluindo o bloco dos advogados) | casa (checklist 2.11) | CPC 1.016, I e IV (sem eles não há como intimar o agravado — 1.019, II) |
| 3 | **SÍNTESE** — quadro "Decisão proferida × o que se ataca × o que se pede" | quadro | curso ("Decisão proferida") | CPC 1.016, II–III |
| 4 | **TEMPESTIVIDADE** — seção autônoma com eixo | `[!tempo]`: publicação → início → ✔ protocolo → último dia | curso | CPC 1.003, § 5º; 224; Lei 11.419, art. 5º, § 3º |
| 5 | **CABIMENTO** — o inciso do 1.015 (ou p.u., ou Tema 988/STJ com a urgência demonstrada) | `##` com o inciso no rótulo | curso ("Do cabimento" como subitem próprio) | CPC 1.015 `[texto: checklist 2.11]`; Tema 988 `[VERIFICAR]`; Súmula 62/TJSC (emenda da inicial não é agravável) |
| 6 | **Síntese do processo** | `[!tempo]` curta ou parágrafo | curso | — |
| 7 | **A decisão agravada** — o trecho, em imagem com etiqueta, e a transcrição | `[provapar]` + `[!cita]` com coordenada | casa (regra 26) · curso (print em agravo) | CPC 1.017, I (decisão e certidão) |
| 8 | **Fundamentos** — um `#` por razão de reforma/invalidação | blocos CREAC; `[!jur]` | curso | CPC 1.016, III |
| 9 | **Efeito suspensivo / tutela recursal** — subtítulo diz o risco concreto | quadro de duas colunas (probabilidade × dano) | curso | CPC 1.019, I; 995, p.u. `[VERIFICAR]` |
| 10 | **Pedidos** — efeito suspensivo → intimação do agravado → provimento | lista | curso | CPC 1.019 |
| 11 | Data + `@assinatura` | — | — | — |
| — | **Anexos**: decisão agravada, certidão de intimação, procurações; custas | — | — | CPC 1.017, I, § 1º e § 5º; 1.017, § 3º (relator **deve** abrir 5 dias para sanar) |

---

## 9. AGRAVO INTERNO

**Destinatário.** O relator, para o colegiado (1.021, § 2º). **Prazo.** 15 dias úteis (1.070; 1.003, § 5º).

| # | Bloco | Elemento visual | Fundamento |
|---|---|---|---|
| 1 | Vocativo ao relator + autos | `@@` | CPC 1.021, § 2º |
| 2 | **SÍNTESE** — quadro "Fundamento da decisão monocrática × impugnação **especificada**" — um por fundamento, sem exceção | quadro | CPC 1.021, § 1º; 932, III |
| 3 | Tempestividade | `[!tempo]` | CPC 1.070 |
| 4 | **Impugnação especificada** — um `##` por fundamento da decisão; se ela só reproduziu a decisão anterior, atacar por 1.021, § 3º e 489, § 1º | `[!cita]` de cada fundamento, com coordenada | CPC 1.021, §§ 1º e 3º |
| 5 | Pedidos — retratação ou provimento; risco de multa avaliado antes | lista | CPC 1.021, §§ 2º, 4º e 5º |
| 6 | Data + `@assinatura` | — | — |

---

## 10. EMBARGOS À EXECUÇÃO (e, com as diferenças anotadas, impugnação ao cumprimento de sentença)

**Distribuição.** Por dependência, autuados em apartado, com cópias que o advogado pode autenticar (914, § 1º). **Prazo.** 15 dias úteis (915); **sem dobro** (915, § 3º) — na impugnação do 525 o dobro se aplica (§ 3º), mas não em autos eletrônicos.

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | Vocativo + execução de origem | `@@` | — | CPC 914, § 1º |
| 2 | **Embargante / Embargado** | `[!qualif]` | — | CPC 319, II (embargos são ação) |
| 3 | **SÍNTESE** — quadro "Alegação × valor × documento" | quadro | curso | CPC 917 |
| 4 | **TEMPESTIVIDADE** — eixo desde a juntada do comprovante de citação | `[!tempo]` | curso | CPC 915, caput e § 1º; 231 `[VERIFICAR]` |
| 5 | **GARANTIA DO JUÍZO** — só para efeito suspensivo (embargos independem de penhora) | `[!calc]` com o bem/valor | curso ("Garantia do juízo") | CPC 914, caput; 919, § 1º |
| 6 | **Síntese da execução** | `[!tempo]` | curso | — |
| 7 | **Fundamentos** — um `#` por inciso do 917 invocado, no rótulo (iliquidez, excesso, prescrição, invalidade da penhora…) | `##` com inciso | curso | CPC 917, I–VI |
| 8 | **EXCESSO DE EXECUÇÃO — regra de ouro**: **valor correto declarado** + **demonstrativo discriminado e atualizado** | `[!calc]` com a planilha (rubrica, valor do exequente, valor correto, diferença, documento) | curso (tabela) · casa (checklist 2.7) | CPC 917, §§ 2º–4º (sem isso: rejeição liminar ou não exame); 525, §§ 4º–5º |
| 9 | **Necessidade de perícia contábil** (se houver) | parágrafo | curso | CPC 464 `[VERIFICAR]` |
| 10 | **Pedidos** — efeito suspensivo → procedência → honorários | lista | curso | CPC 919; 85, § 13 `[VERIFICAR]` |
| 11 | Data + `@assinatura` | — | — | — |

---

## 11. MEMORIAIS / RAZÕES FINAIS

**Cabimento.** Substituem o debate oral quando a causa tem questões complexas; prazos **sucessivos** de 15 dias (CPC 364, § 2º). No penal, prazo sucessivo do CPP 403, § 3º `[VERIFICAR]`. É a peça do **efeito de recência** (`tipografia-e-design`, lei 6).

| # | Bloco | Elemento visual | Fundamento |
|---|---|---|---|
| 1 | Vocativo + autos | `@@` | CPC 364, § 2º |
| 2 | **SÍNTESE** — quadro "Questão × prova que a resolve (coordenada) × conclusão" | quadro | CPC 188 |
| 3 | **Linha do tempo do processo** (instrução) | `[!tempo]` | — |
| 4 | **Matriz de provas** — um `#` por questão de fato; em cada um, o quadro "elemento da regra × prova × coordenada" e o `[provapar]` da prova decisiva | quadro; `[provapar]` | CPC 369; 371 `[VERIFICAR]` |
| 5 | **Direito** — só o que a instrução mudou | `[!jur]` | — |
| 6 | **Conclusão e pedido** | lista curta | — |
| 7 | Data + `@assinatura` | — | — |

---

## 12. PROCURAÇÃO *ad judicia*

**Documento de uma folha** (assinatura na mesma página do texto — flanco jurídico se separar; `tipografia-e-design`, §7). Margens 2,5/2,0 (leva logo). Modelo do curso: título, quadro Outorgante, quadro Outorgado, poderes, data e assinatura — **copiar a estrutura da v2**, não da v1 (a v1 é arquivo sem estilo).

| # | Bloco | Elemento visual | Origem | Fundamento |
|---|---|---|---|---|
| 1 | `@@ PROCURAÇÃO` | `@@` | curso | — |
| 2 | **Outorgante** — os 8 dados do 319, II (para a inicial não faltar) | `[!qualif] Outorgante` | curso (quadro) | CPC 319, II; 105, caput ("assinado pela parte") |
| 3 | **Outorgado** — nome, **OAB**, **endereço completo, eletrônico e não eletrônico**; **sociedade**, registro na OAB e endereço | `[!qualif] Outorgado` | curso (quadro) | CPC 105, §§ 2º–3º; 287 |
| 4 | **Poderes** — cláusula *ad judicia* (EOAB 5, § 2º) + **poderes especiais em cláusula específica**: receber citação, confessar, reconhecer a procedência, transigir, desistir, renunciar, receber, dar quitação, firmar compromisso, **assinar declaração de hipossuficiência** | `[!poderes]`; a lista pode ser período corrido se estourar a folha (conferir que nenhum poder sumiu) | casa (janela) · curso (poderes em bloco) | CPC 105, caput e § 4º; EOAB 5, § 2º |
| 5 | Objeto/finalidade (processo ou causa) | uma linha | — | — |
| 6 | Data + assinatura do outorgante (+ assinatura eletrônica quando for o caso) | `@@` | — | CPC 105, § 1º; Lei 11.419, art. 1º, § 2º, III |

---

## 13. SUBSTABELECIMENTO

Uma folha. Quadros **Substabelecente / Substabelecido** (curso), cláusula **com ou sem reserva de poderes — expressa**, poderes substabelecidos (todos ou quais), data e assinatura.
**Fundamento.** EOAB 26 (com reserva, o substabelecido não cobra honorários sem intervenção do substabelecente; p.u. incluído pela Lei 14.365/2022) `[conferido: acervo da casa]`; CC 667, § 2º e 3º `[VERIFICAR]`; CPC 105, §§ 2º–3º (dados do substabelecido, para intimação).

---

## 14. PARECER

**Único documento da casa que leva timbre em todas as páginas.** Primeira página com marca completa e rodapé em faixa; páginas seguintes **com marca reduzida** `[curso; pendente 3.11]`. Numeração "Pg. n de N" cabe aqui (não vai ao eproc). Se entregue a terceiro, sai limpo de rastro técnico.

| # | Bloco | Elemento visual | Fundamento |
|---|---|---|---|
| 1 | Ementa/consulta — a pergunta objetiva do cliente | quadro "Consulta × resposta curta" | — |
| 2 | Premissas — fatos e documentos considerados | `[!tempo]`; tabela de documentos | — |
| 3 | Fundamentação — blocos CREAC; doutrina só em tese controvertida | `[!cita]`, `[!jur]`, `[!dout]` com etiqueta completa | EOAB 2, § 3º (inviolabilidade nas manifestações) |
| 4 | Conclusão objetiva + ressalvas + o que depende de verificação | lista | — |
| 5 | Data + `@assinatura` | — | — |
| — | Sigilo: dados do cliente e de terceiros só o necessário | — | EOAB 34, VII |

---

## 15. CONTRATO (honorários, prestação de serviços, institucional)

Gerador próprio (`gerar_contrato_pdf.py`), Times 12, recuo 2 cm, margens 2,5/2,0 com logo. Cláusulas numeradas; **tabelas suportadas desde 27/08**.

| # | Bloco | Elemento visual | Fundamento |
|---|---|---|---|
| 1 | Título + partes | `[!qualif]` por parte (CENTRAL DE DADOS) | CC 104 `[VERIFICAR]` |
| 2 | **Objeto** | `[!objeto]` | — |
| 3 | Obrigações · preço · prazo · rescisão · **foro (com pertinência)** | cláusulas numeradas; tabela de valores | CPC 63, § 1º (foro de eleição exige pertinência — red. Lei 14.879/2024) `[texto: checklist universal]` |
| 4 | Honorários: contratados × sucumbenciais; substabelecimento | cláusula | EOAB 22; 26 |
| 5 | Assinaturas na mesma folha do fecho | `@@` | — |

---

## 16. NOTIFICAÇÃO EXTRAJUDICIAL

Timbre é decisão do Gabriel (reconfirmar). Esqueleto: notificante/notificado (`[!qualif]`) → **fatos** (`[!tempo]`) → **fundamento e exigência** (o que se requer, prazo) → **consequência** do não atendimento → fecho. Tom firme, sem ameaça vazia; sem expressão ofensiva (o CPC 78 é do processo, mas o EOAB 34 vale fora dele `[VERIFICAR inciso]`). Prova visual do documento que fundamenta a exigência: `[provapar]`.

---

## Apêndice — o que muda de peça para peça e o que não muda

| | Inicial | Contestação | Réplica | ED | Apelação | Agravo | Emb. exec. |
|---|---|---|---|---|---|---|---|
| Vocativo | juízo (319, I) | juízo | juízo | prolator (1.023) | 1º grau + tribunal | tribunal (1.016) | juízo da execução |
| Qualificação | 8 dados (319, II) | réu | — | — | **com qualificação** (1.010, I) | **só nomes** + advogados (1.016, I e IV) | 8 dados |
| Síntese em quadro | sim | sim | sim | sim ("vício") | sim (capítulos) | sim ("decisão") | sim |
| Tempestividade com eixo | — | prazo no topo | prazo no topo | **sim** | **sim** | **sim** | **sim** |
| Quadro Alegação × Realidade | — | **sim** (341) | espelho | — | — | — | — |
| `[!calc]` obrigatório | valor da causa | — | — | — | preparo | custas | **demonstrativo** (917, § 3º) |
| Prova visual típica | documento decisivo | documento que desmente | documento novo | trecho da decisão | prova mal valorada | decisão agravada | título/planilha |
| Requerimentos preliminares (☑) | **sim** | gratuidade | — | — | gratuidade/efeito | efeito suspensivo | efeito suspensivo |
