# Método das peças (redação) — reaproveitado do `redigir-peca-juridica`

> A redação só começa **depois** da análise + verificação. Peça é trabalho do advogado:
> sai como **rascunho pronto pra revisar e assinar** — a skill **NUNCA protocola**.

## Ciclo de 6
1. **Ler os autos** — cronológico, da 1ª à última página, ANTES de redigir. Sem isso, não começa.
2. **Fundamentar + verificar fontes** — hierarquia: Constituição → Lei → Súmula → Jurisprudência → Doutrina. Lei no Planalto; súmula/jurisprudência no portal oficial (1 a 1, inteiro teor). Não confirmou → `[INSERIR PRECEDENTE — VERIFICAR]`.
3. **Prescrição** (só peça **criminal**) — checklist CP arts. 109, 111, 115, 116, 117.
4. **Endereçar** ao órgão competente para **apreciar** (não onde se protocola) — vocativos corretos.
5. **Formatar (peça LIMPA — decisão Gabriel 03/06 + 05/06):**
   - **SEM logomarca e SEM rodapé.** Começa no endereçamento (EXCELENTÍSSIMO…); fecha com **nome (negrito) + OAB** (+ "Defensor Dativo" se AJG). Rodapé limpo (sem endereço/telefone/e-mail; a numeração de página o e-Proc faz).
   - Tipografia: a de `references/tipografia-vigente.json`, aplicada pelo gerador (Times 12, Charter 11 a 3 cm, entrelinha 1,35, margens 3/3 e 2,3/1,8 cm, recuo 2 cm, versalete nos títulos). Vocativo e título centralizados; seções à esquerda em negrito (numeração automática por `@numerar`); data/assinatura centralizadas. *Corrigido em 02/09/2026: dizia "margens 3/2/2/3, entrelinha 1,5, recuo 1,25", revogadas.*
   - Gerador: `assets/gerar_pdf.py` (markdown→PDF via Chrome headless; `@@`=centralizado, `#`=seção, `##`=subseção, `**Rótulo:**`=qualificação; **sem logo, sem rodapé, frontmatter removido**).
6. **Revisar antes de entregar** — gate dos 10 bloqueios abaixo + revisão gramatical (Bechara, Cunha & Cintra, Cegalla, AO 1990, VOLP). **Revisar com intervalo** (aula bônus da Masterclass, adotado em 02/09/2026): a revisão final é feita em sessão distinta da redação — quem acabou de escrever não vê o próprio erro.
   - **Gate automático (1º filtro objetivo):** rodar `python scripts/validar_norma_culta.py PECA.md` — checa AO 1990 (trema/acentos abolidos), **crase/gramática clássica** (à partir, haja visto, houveram…), anti-vazamento de PDF (frontmatter/wikilink/marcador `[VERIFICAR]`), anti-IA (Prov. 205/2021) e tipografia. `exit 1` = ainda **não** está pronta.
   - **Revisão semântica (camada 2b):** com o gate verde, revisar concordância com sujeito distante, regência, crase por gênero, colocação pronominal, pontuação de sentido e ambiguidade conforme `references/revisao-semantica.md` — feita pelo Claude na sessão, com correções pontuais justificadas (nunca reescrita silenciosa). Mérito e fidelidade aos autos seguem com o advogado.

## Gate final — 10 bloqueios (qualquer um aberto = NÃO está pronta)
1. "Prática forense" sem fundamento legal/doutrinário ao lado. 2. Trecho de terceiro sem conferir na fonte. 3. Juntada de documento que não está nos autos. 4. Jurisprudência sem conferência no portal. 5. Menção a IA/Claude/Anthropic/bot/GPT. 6. Marcadores `[VERIFICAR]`/`[INSERIR]` remanescentes. 7. Endereçamento ao órgão errado. 8. Falta de revisão gramatical (mínimo: `validar_norma_culta.py` sem erros). 9. (Penal) prescrição não verificada. 10. Autos não lidos cronologicamente.

> Entregue sinalizando o estado do gate: o que está **conferido** e o que ficou `[VERIFICAR]` aguardando você (conferir precedente, anexar documento). **Nunca** declarar "pronta pra protocolar" com bloqueio aberto.

## Versão única (regra Gabriel 05/06 — evita confusão no protocolo)
- Só a **última versão** da peça fica na pasta do caso. Ao revisar, **sobrescrever** a anterior — não criar `peca_v1`, `_FINAL`, `_rev2`.
- Precisou guardar histórico? A versão antiga vai para `_versoes-antigas/` (fora da linha de protocolo), nunca ao lado da boa.

---

# Técnica de redação forense persuasiva (craft — não substitui a verificação)

> Esta seção é **só técnica de escrita/estrutura/persuasão** — estável, não-fabricável. Nenhum
> exemplo abaixo afirma lei, súmula, prazo ou jurisprudência: onde caberia um dado concreto há
> um placeholder. **O conteúdo jurídico continua subordinado à verificação** (ciclo de 6, passos
> 2 e 4) e ao gate dos 10. Craft bom com fato errado = peça reprovada. Verifique primeiro; escreva
> bem depois.

## 1. O silogismo é o esqueleto invisível de toda peça
A peça persuade porque é um **silogismo jurídico** vestido de prosa: **premissa maior** (a regra de
direito), **premissa menor** (o fato concreto do caso), **conclusão** (o pedido como consequência
lógica inevitável). Tudo o que você escreve serve a uma dessas três funções. Antes de redigir,
escreva o silogismo do caso em três linhas cruas; se ele não fecha, a peça não vai fechar — falta
regra, falta fato provado ou falta o elo entre os dois.

- **Premissa maior** = o passo 2 do ciclo (fundamentar + verificar). Vem da hierarquia
  Constituição → Lei → Súmula → Jurisprudência → Doutrina, cada elo conferido na fonte. O que não
  conferir entra como `[VERIFICAR]`, nunca como afirmação.
- **Premissa menor** = o fato dos autos, ancorado em "Ev. N". Nunca um fato de cabeça.
- **Conclusão** = o pedido. Se a conclusão não decorre necessariamente das duas premissas, o juiz
  sente o salto lógico — e é exatamente nesse salto que a parte contrária ataca.

## 2. Abrir pela questão profunda (*Deep Issue*) — bloco "Síntese da controvérsia"
Toda peça (inicial, contestação, recurso, parecer) abre com um bloco curto de até **75 palavras**
que entrega a controvérsia ao julgador em **90 segundos**. Ele é o silogismo comprimido, na ordem
**regra → fato → pergunta**, em **três frases separadas** (não uma frase-monstro):

1. **Regra** (premissa maior, em linguagem própria — sem citar número de artigo aqui).
2. **Fato** (premissa menor, como mini-história concreta, **não** conclusiva).
3. **Pergunta direta**, terminada em ponto de interrogação, que é a verdadeira decisão do caso.

Como achar a pergunta certa — técnica do **"e isso depende de quê?"**: pegue a questão aparente e
pergunte repetidamente "e isso depende de quê?" até chegar ao ponto concreto que ninguém mais
consegue desdobrar. A abstração é inimiga: quanto mais abstrata a pergunta, mais superficial a peça
e mais o juiz precisa "aprender" para entendê-la.

- **Errado (abstrato):** "Houve nulidade?"
- **Certo (concreto):** "O ato [X] é nulo porque a notificação [Y] não ocorreu no prazo [VERIFICAR]?"

**Armadilhas a rejeitar na revisão** (Garner adaptado):
- Abertura que começa por "Trata-se de saber se…" empilhando tudo numa só frase → reescrever
  **contexto-primeiro, pergunta-depois**, em frases separadas.
- **Citação de lei dentro da pergunta** → tira-se o número/artigo da frase-questão (vai na
  fundamentação); a síntese fala da regra em linguagem comum.
- Mais de 75 palavras → ainda não é síntese, é fundamentação disfarçada.

> O bloco "Síntese da controvérsia" vira **gabarito de qualidade**: se você não consegue escrevê-lo
> em 75 palavras, você ainda não entendeu o próprio caso bem o bastante para redigi-lo.

## 3. Cada tópico do mérito em IRAC / CREAC
Dentro da fundamentação, **cada tese** é um sub-silogismo com esqueleto fixo. Em prova de concurso
usa-se **IRAC**; em **peça de advocacia, prefira CREAC** (começa pela conclusão — você está
advogando, não testando hipótese):

- **C — Conclusão/tese:** enuncie de saída o que aquele tópico prova ("O ato [X] deve ser anulado").
- **R — Regra:** a norma como princípio geral, **decomposta em elementos** (fato gerador, definições,
  exceções, limites, defesas). Decompor é o que permite a subsunção peça por peça.
- **E — Elaboração:** o que cada elemento significa (aqui entram, **depois** do raciocínio próprio,
  os reforços de doutrina/jurisprudência — ver item 7).
- **A — Aplicação/Subsunção (o coração):** conecte **cada** elemento da regra a **um** fato dos
  autos, com a palavra-chave **"porque"**: "incide porque o fato [Ev. N] corresponde ao elemento
  [Y]". Elemento sem fato pareado = buraco na tese, e o adversário entra por ele.
- **C — Conclusão (reafirmação):** feche reafirmando a tese como consequência lógica.

A subsunção é onde a peça ganha ou perde. Ela cruza diretamente com a **matriz de provas** do caso:
cada "porque" precisa de um "Ev. N" atrás. Se não há prova para um elemento, ou se prova, ou o
elemento vira `[VERIFICAR]` — nunca se afirma o elo sem lastro.

## 4. *Topic sentences* e sinalização (*signposting*)
O juiz lê rápido e em diagonal. Faça a estrutura **visível**:

- **Frase-tópico (topic sentence):** o **primeiro período de cada parágrafo** já diz a conclusão
  daquele parágrafo. Quem ler só a primeira frase de cada parágrafo deve entender a peça inteira.
  Parágrafo que só "conclui no fim" obriga o leitor a guardar tensão à toa — e ele não vai.
- **Sinalização explícita:** numere e nomeie as teses ("Primeiro…", "Segundo…", "Resta a questão
  de…", "Disso decorre que…"). Os títulos de seção (I —, II —) e as frases-ponte são o mapa: o
  leitor nunca deve se perguntar "onde estou e por que estou lendo isto?".
- **Um parágrafo, uma ideia.** Parágrafo que vira duas ideias vira duas teses mal provadas.
- **Coerência de catraca:** cada parágrafo retoma o anterior (referência para trás) e prepara o
  próximo (gancho para frente). É isso que faz a peça "andar" em vez de listar pontos soltos.

## 5. Hierarquia de argumentos — do mais forte ao mais fraco
Argumentos não são uma lista democrática; são uma **ordem de combate**:

- **Abra pelo mais forte.** A atenção e a credibilidade do leitor são máximas no início. O argumento
  decisivo vem primeiro, não guardado para o "grand finale" — peça não é romance de suspense.
- **Cuidado com o argumento fraco junto do forte:** um fundamento ruim **contamina** os bons (o juiz
  generaliza o desleixo). Se um argumento é frágil, ou se reforça até ficar de pé, ou se corta. Na
  dúvida entre incluir e omitir um argumento fraco, **omita** — a peça enxuta é mais forte que a peça
  longa.
- **Subsidiariedade honesta:** pedidos alternativos/sucessivos ("caso não se entenda assim…") vêm
  **depois** e claramente rotulados como subsidiários — nunca embaralhados com a tese principal, sob
  pena de o juiz achar que nem você acredita na principal.
- **Não dilua:** três fundamentos sólidos batem dez fundamentos médios. Quantidade lida como
  insegurança.

## 6. Técnica de refutação (atacar a tese contrária sem fortalecê-la)
Refutar bem é antecipar e desarmar — não é xingar a parte contrária:

- **Refute o argumento, não a pessoa.** Tom institucional. Adjetivo contra o adversário ("temerária
  a tese", "absurda a pretensão") enfraquece quem escreve, não quem é atacado.
- **Enuncie o contra-argumento com justiça, então derrube-o.** Apresentar a tese adversária na sua
  forma mais forte e ainda assim refutá-la convence muito mais que atacar um espantalho. Mas
  **não dê palco**: enuncie em uma frase, refute em três.
- **Ataque o elo mais fraco do silogismo do adversário** — em geral a subsunção ("o fato deles não
  preenche o elemento [Y] porque [Ev. N]") ou a premissa fática (prova ausente), não a regra
  abstrata.
- **Concessão estratégica:** conceda o ponto irrelevante para concentrar fogo no decisivo. Brigar com
  tudo dilui; conceder o que não importa dá credibilidade ao que importa.
- **Não invente a tese do outro.** Refutar argumento que a parte contrária não fez é desperdício e
  pode plantar a ideia na cabeça do juiz.

## 7. Economia e clareza (Garner/Pinker adaptados ao foro brasileiro)
Clareza **não** é informalidade — é precisão. Convive integralmente com a norma culta
(Bechara/Cunha & Cintra/Cegalla). Regras de craft que entram no checklist de revisão:

- **Voz ativa, sujeito explícito.** "O réu descumpriu o contrato" vence "Foi descumprido o contrato".
  A passiva esconde o agente e enfraquece a imputação. Marque passivas e reescreva em ativa onde a
  ênfase é em quem agiu.
- **Frases curtas, um verbo forte por frase.** Período que passa de ~3 linhas costuma esconder duas
  ideias — quebre. O verbo carrega o argumento; não o sepulte em nominalização ("proceder à análise"
  → "analisar").
- **Corte a pilha de preposições.** Três ou mais "de/para/com/em" encadeados ("a análise da questão
  da nulidade do ato da autoridade") sinalizam frase a reescrever.
- **Mate os intensificadores opinativos:** "claramente", "obviamente", "evidentemente",
  "indubitavelmente", "por óbvio". Eles **aparentam viés** e enfraquecem a credibilidade — se o
  ponto fosse óbvio, não precisaria do advérbio. A força vem do fato + regra + prova, não do
  adjetivo. **Caça obrigatória na revisão.**
- **Doutrina e jurisprudência reforçam, não carregam.** Posicione a citação **depois** do seu
  raciocínio próprio, como confirmação ("nesse sentido, [VERIFICAR]"), nunca como muleta que sustenta
  sozinha a tese. Peça que só empilha ementa lê como panfleto.
- **Termo técnico só quando é o termo certo.** Juridiquês por status é ruído; jargão preciso é
  economia. Na dúvida, a palavra que o juiz entende sem reler.

## 8. Narrativa dos fatos que já prepara a subsunção
A seção "Dos Fatos" não é depósito cronológico — é a **construção das premissas menores**:

- **Ordem cronológica**, do fato gerador ao dano/pedido.
- **Poda:** só os fatos **juridicamente relevantes**. Fato periférico obscurece o núcleo e dá flanco
  ("se isso importasse, por que não provou?"). Cada fato narrado deve apontar para um elemento da
  tese que ele sustenta — a narrativa já é meia-subsunção.
- **Humanizar dentro do dever de verdade.** Pode-se dar à situação da parte (residente, idoso,
  consumidor) peso humano e concreto **sem distorcer** um milímetro. A anti-fabricação é absoluta:
  fato não comprovado não entra, nem "arredondado". Empatia honesta persuade; exagero detectável
  destrói a credibilidade da peça inteira.
- **Cada fato com seu "Ev. N".** Narrativa fática sem âncora nos autos é alegação, e alegação não
  prova premissa.

## 9. Microchecklist de craft (roda na revisão, ao lado do gate dos 10)
Aplicar **depois** que o gate automático (`validar_norma_culta.py`) está verde — craft é a camada de
persuasão, não substitui a de norma culta nem a de verificação:

1. Existe bloco "Síntese da controvérsia" ≤ 75 palavras, ordem regra→fato→pergunta, sem citar artigo?
2. Cada tese do mérito fecha em CREAC, com a subsunção amarrando **cada** elemento a um "Ev. N" por
   "porque"?
3. A primeira frase de cada parágrafo entrega a conclusão do parágrafo (topic sentence)?
4. O argumento mais forte abre a fundamentação? Todo argumento fraco foi reforçado ou cortado?
5. Zero "claramente/obviamente/evidentemente/por óbvio" e mínimo de passivas/pilhas de preposição?
6. Citação de doutrina/jurisprudência vem **depois** do raciocínio próprio (e está `[VERIFICADO]` ou
   `[VERIFICAR]`, nunca nua)?
7. Refutação ataca tese, não pessoa, e mira o elo fraco do silogismo adversário?
8. "Dos Fatos" está podado, cronológico e cada fato aponta para um elemento da tese — tudo com
   âncora nos autos e dentro do dever de verdade?

> Esta camada melhora **como** a peça convence; ela **não** afrouxa a trava suprema. Qualquer lei,
> súmula, prazo, número de processo ou tese de tribunal continua valendo só se conferido 1 a 1 na
> fonte oficial — caso contrário, `[VERIFICAR]`. Craft impecável jamais autoriza um fato jurídico não
> verificado.
