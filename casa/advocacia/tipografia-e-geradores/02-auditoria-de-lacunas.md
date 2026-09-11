# Auditoria de lacunas — curso × régua da casa (02/09/2026)

> Método: cada regra ensinada nos dois cursos foi procurada nos arquivos de regra da casa.
> Fonte única das medidas: `tipografia-vigente.json` (vigente desde 27/08/2026). Os demais
> arquivos são ilustração datada; onde trazem número diferente do JSON, isso é registrado no
> item 4 como contradição a corrigir.

## 1. O que coincide (nenhuma ação)

| Regra do curso | Onde está na casa |
|---|---|
| Margens laterais 3 + 3 cm (nunca menos de 5 somados) | JSON `margens_cm`; 18 dos 20 `.docx` confirmam |
| Justificado com hifenização | geradores; vocativo sem hifenização (`.center { hyphens:none }`) |
| Citação em bloco: recuo 3 cm, corpo menor, **sem itálico**, sem aspas | JSON `citacao` (Charter 11, 3,0 cm) |
| Um só marcador de parágrafo (recuo **ou** espaço) | recuo 2 cm, espaço 0 |
| Destaque por último, poucos pontos por página, só fato exclusivo do caso | regra geral 1-A e III.2; caderno II |
| Proibidos: sublinhado, caixa-alta no corpo, marca-texto | JSON `proibido` |
| Negrito e itálico "de forma estratégica" (PDF) | JSON `permitido_com_parcimonia` |
| Síntese na primeira página | SÍNTESE em 4 blocos (20/08) → em quadro (30/08) |
| Subtítulo diz a tese, não o instituto | importado 30/08 |
| Dados → tabela; datas → linha do tempo; requisitos → quadro | `[quadro]`, `[!tempo]`, janelas |
| Tabela de fato com coluna "documento" | caderno de erros, IV |
| Linha do tempo com marco destacado | `~ !data` |
| Tempestividade como seção com eixo do tempo em todo recurso | modelos 05–08 da casa |
| Dispositivo no rótulo do título | importado 30/08 |
| Impugnação especificada em quadro Alegação × Realidade | modelo 02 |
| Jurisprudência contextualizada no corpo, 2–3 por peça, supressão `[...]` | regra geral III.7; `forma-da-peticao` D |
| Nenhum tópico termina em citação; parágrafo ≤ 8 linhas | caderno II; guia Petri |
| Elemento visual no topo do item, não no fim | caderno, erro 10 |
| "Modelos nunca servem integralmente" | `00-LEIA-ME` dos modelos |
| Estilos nomeados / "manter somente texto" | marcação do gerador |
| Diagramar imagens e destacar são os dois últimos passos | regra 1-A |
| Borda cinza + sombra em imagem clara | geradores (27/08) |
| Tabela invisível para diagramar print vertical/horizontal | `[provapar]` / `[prova]` |
| Marca-texto lícito **dentro** do print, com o íntegro no anexo | `printscreens`, §5.6 |
| Captura em alta resolução; nunca a tela inteira; PDF de página web | `printscreens`, §5 |
| P.R.I.N.T. + checklist | `printscreens`, §§4 e 9 |
| Print é exceção; laudo comporta dezenas; alerta: página majoritariamente imagem | `printscreens`, §3 |
| Ata notarial/Verifact = camada extra | `printscreens`, §2 |
| Zoom-in (página + trecho ampliado) | `[provapar]`, 9-A |
| Etiqueta dizendo o efeito jurídico | regra 26, etiqueta vermelha |
| QR code e ícones "alguém testou?" → não usar | tipografia-e-design, lei 7 do professor |
| "Tamanho é resultado, não meta"; linha curta vence página a menos | JSON `desempate` |
| Branco com função ≠ branco à toa | `vao-no-pe-da-pagina` |

## 2. Divergências decididas (nenhuma ação — só manter o registro)

| Ponto | Curso | Casa | Onde está o motivo |
|---|---|---|---|
| Fonte | Segoe UI (v1), Sitka Text (v2), Georgia citada | Times New Roman 12 / Charter 11 | ordem escrita de 20/08; `padrao-formatacao-peca` 5.3 |
| Entrelinha | 1,1–1,2 | 1,35 | princípio dele, valor medido para Times (caderno, erro 6) |
| Recuo × espaço | espaço 10 pt (v1) / recuo 1 cm + 8 pt (v2) | recuo 2 cm, espaço 0 | decisão de 20/08 |
| Corpo da citação | 10 pt (Segoe) / 11 pt (Sitka) | Charter 11 | amostra renderizada de 20/08 |
| Margens verticais | 3 / 2,5 | 2,3 / 1,8 (peça); 2,5 / 2,0 (contrato) | tarja do eproc; JSON `_margens_verticais` |
| Timbre na peça forense | timbrado, 1ª página diferente | peça limpa | 03/06, 14/08, 20/08 |
| Numeração de página | `PAGE`/`NUMPAGES` em caixa, "Pg. 2 - 7" | nenhuma (o eproc numera) | `metodo-das-pecas`, passo 5 |
| Link na jurisprudência | hiperlink no PDF | caminho de consulta em texto | `forma-da-peticao`, D.0 |
| Endereçamento | "AO JUÍZO" (Petri) | "Excelentíssimo Senhor Doutor Juiz…" + veto a "Meritíssimo/Douto Juízo" | `redacao-objetiva`, §2 |
| Ícone de exclamação na capa | usa | não usa | aula 1 do próprio professor: ícone é pouco testado |
| Art. dos meios de prova | "396" | **369** | caderno, 5 e 9.1 |
| "87 % dos juízes" | cita | não cita em peça (sem fonte) | caderno, 9.2 |

## 3. Lacunas reais — o curso ensina, a casa não tem posição escrita ou ferramenta

> ✅ **Decidido em 02/09/2026 (ordem do Gabriel: "adote os 14 itens").** As propostas abaixo
> foram adotadas como escritas — 3.3 e 3.4 na forma de recusa registrada — e implementadas em
> `instalar/` (regra: `adendo-2026-09-02-adocao-dos-14-itens.md`). Pendente só o traço
> tracejado do `recorte` (Swift, compila no Mac).

Cada item traz **proposta** e **quem decide**.

| # | O que o curso faz | Estado na casa | Proposta | Decide |
|---|---|---|---|---|
| 3.1 | **Versalete** (`smallCaps`, *tracking* 0,7 pt) nos títulos e na qualificação | sem posição escrita; a régua proíbe **caixa-alta**, que não é a mesma coisa (pendente desde 30/08) | Adotar versalete **só no vocativo e nos títulos de seção** (`@@` e `#`), com `font-variant: small-caps` e `letter-spacing: 0,5 pt`; manter o corpo em caixa mista. Ganho: hierarquia sem gritar. Custo: zero — Times tem versalete sintético no Chrome | Gabriel |
| 3.2 | **Quadro "Requerimentos preliminares"** com caixas ☑/☐ na capa (gratuidade, prioridade, tutela, segredo, audiência) | pendência desde 29/08; único elemento "com ganho real" ainda não adotado | Janela nova `[!requerimentos]` (ou tabela de duas colunas com "☑"), **logo abaixo da SÍNTESE**, listando os pedidos que o art. 319, VII, o art. 98, o art. 1.048 e o art. 300 obrigam a formular expressamente. Serve de checklist para o gabinete e para a casa | Gabriel (canônica) + andar 40 (gerador) |
| 3.3 | **Capitular** na abertura da qualificação | não usa; sem posição | **Não adotar.** Capitular é ornamento; a aula 1 manda testar antes de adotar e não há dado. Registrar a recusa para fechar a ponta | Gabriel |
| 3.4 | **Etiqueta lateral de lei** ("Lei 8.213/91" na margem, ao lado do trecho) | só janelas em bloco (`[!jur]`, `[!dout]`); nada lateral | **Não adotar como caixa lateral** (margem de 3 cm não comporta e quebra a mancha). Cumprir a função pelo **dispositivo no rótulo do título** (já importado) e pela `[!cita]` com o texto de lei | Gabriel |
| 3.5 | **Numeração automática de seções** (2. Título, 3.1 Subtítulo) | gerador não numera; casa numera à mão ("I —", "II —"); padrão nunca escrito | Escrever o padrão: seções em romanos ("I —"), subseções em "I.1", sub-subseções "I.1.a"; o gerador pode numerar sozinho (`counter-reset`) — decidir se automático ou manual | Gabriel + andar 40 |
| 3.6 | **Título um ponto maior que o corpo** (13 sobre 11; v2: 12 sobre 12) | título 12 = corpo 12, negrito azul | Manter 12/12 (a v2 do próprio autor faz assim) **ou** subir o `#` para 13 pt. Recomendação: manter — o azul e o negrito já marcam; medir antes de mudar | Gabriel |
| 3.7 | **Quadro de tutela de urgência em duas colunas** (verossimilhança × perigo na demora, com ✓) | a regra geral cita "tutela" entre as janelas, mas não há janela nem modelo | Padronizar como tabela `[quadro]` de duas colunas com cabeçalho "Probabilidade do direito" · "Perigo de dano" (as palavras do art. 300, não as do CPC/73), uma linha por fato com coordenada. Colocar no topo do item de tutela | Gabriel (canônica) |
| 3.8 | **Série de três imagens com legenda única** (fotos, prints de conversa em datas distintas) | só `[prova]` (1) e `[provapar]` (2) | Sintaxe `[provatrio] a.png \| b.png \| c.png \| Rótulo \| Legenda` — três colunas, legenda mesclada, retângulos de destaque copiados | andar 40 |
| 3.9 | **Quadro de apoio ao lado do documento** (contratante, objeto, cláusula, teor; ou data do óbito, requerimento, filhos) | registrado como "a técnica mais forte" (§8), sem sintaxe; hoje sai como tabela abaixo | Sintaxe `[provaquadro] doc.png \| campo=valor (coord.) \| campo=valor (coord.) …` — documento reduzido à esquerda, tabela de campos à direita, **cada valor com coordenada** (regra do portador) | andar 40 |
| 3.10 | **Seta ligando página inteira ao zoom**; retângulo de destaque **tracejado fino** | par sem seta; retângulo contínuo de 3 px | (a) seta fina cinza entre os dois painéis do `[provapar]`; (b) opção `--tracejado` no `recorte --box`. Estilo, não função — baixa prioridade | andar 40 |
| 3.11 | **Marca reduzida (só o símbolo) e menos informação nas páginas seguintes** do documento timbrado | parecer e contrato repetem o timbre inteiro em toda página | No `gerar_pdf_relatorio.py` e `gerar_contrato_pdf.py`: primeira página com marca completa e rodapé em faixa; seguintes só com o símbolo e a numeração. É o item 10 da aula 2 aplicado ao único documento da casa que leva timbre | Gabriel + andar 40 |
| 3.12 | **Fórmula "competente por distribuição"** no endereçamento quando o juízo ainda não existe | `[VERIFICAR — juízo competente]` | Aceitar "…da Vara Cível **a que couber por distribuição** da Comarca de …" como texto final da inicial (o art. 319, I, exige o juízo, não a vara). O `[VERIFICAR]` continua para peça em processo já distribuído | Gabriel |
| 3.13 | **Revisar com intervalo** (Petri) | não consta do método | Acrescentar ao passo 6 de `metodo-das-pecas.md`: a revisão final é feita **em sessão distinta** da redação | Gabriel |
| 3.14 | **Fundamento no CPC 425, VI e § 1º** para o print (reprodução digitalizada juntada por advogado = mesma prova que o original; original preservado até o prazo da rescisória) | a casa só cita a Lei 11.419, art. 11, §§ 1º e 3º | Citar os dois: o CPC repete a regra e é lei posterior e geral do processo | banca (é acréscimo, não mudança) |

## 4. Contradições internas do acervo — arquivos que ainda ensinam medida revogada

> ✅ **Corrigidos em 02/09/2026** — versões completas em `instalar/skills/...` e
> `instalar/vault/Advocacia/`, cada correção datada no próprio texto.

O JSON revoga: entrelinha 1,5 · citação a 4 cm · margem direita 2 cm · "só negrito" · Georgia ·
órfãs/viúvas 3/3. Estes arquivos ainda trazem uma ou mais dessas medidas **sem aviso de
revogação**. A regra 25 diz: "achou divergência, corrija o arquivo na hora". Como são
canônicos, a correção é ato de quem os editou — fica aqui a lista.

| # | Arquivo | O que diz | O que vale |
|---|---|---|---|
| 4.1 | `janelas-e-linha-do-tempo-2026-08-27.md`, seção "Tipografia" | Charter 11 a **4 cm**; entrelinha **1,5**; destaque **só negrito** | 3 cm; 1,35; negrito e itálico (pendente desde 30/08, erro 11) |
| 4.2 | `forma-da-peticao-2026-08-26.md`, E.1.5 | "gerador da casa (**Georgia 12, entrelinha 1,25**, recuo 2 cm)" | Times 12; 1,35 |
| 4.3 | `checklist-universal.md` (skill `requisitos-das-pecas`), 1.10 | "Tipografia canônica da casa aplicada (**Georgia 12, entrelinha 1,25, recuo 1 cm**, citação **11 pt/2 cm**)" | Times 12; 1,35; 2 cm; Charter 11 a 3 cm |
| 4.4 | `metodo-das-pecas.md`, passo 5 | "margens **3/2/2/3** cm, entrelinha **1,5**, recuo **1,25 cm**" | 3/3 e 2,3/1,8; 1,35; 2 cm |
| 4.5 | `tipografia-e-design-da-informacao-2026-08-24.md`, cabeçalho | "Entrelinha **1,5**"; "Charter 11, recuo **4 cm**, entrelinha 1,5"; "Destaque: **só negrito**" (o adendo 7-A corrige só a paginação) | 1,35; 3 cm; negrito e itálico |
| 4.6 | Nota Notion "00 - CLÁUSULA PÉTREA — a marca do advogado e a tipografia única (27-08-2026)", item (b) | "recuada **4 cm** · entrelinha **1,5** · destaque **só por negrito**" | idem |
| 4.7 | Nota Notion "2026-08-27 — PADRÃO VISUAL das peças", tabela e item "Pendente" | "citação Charter 11 a **4 cm**" | 3 cm |
| 4.8 | `Tipografia Jurídica.md` (07/05/2026, Butterick), status "vigente" | Crimson Pro/Lora 12, Poppins nos títulos, 1,5, recuo 1,25, margens 3/2,5/3/2,5, capítulo em página nova, numeração e cabeçalho de página, Pandoc/XeLaTeX | **Inteiramente superada** desde 14/08; precisa de banner "REVOGADA — ver `tipografia-vigente.json`" para não ser lida como vigente |
| 4.9 | `padrao-formatacao-peca-2026-08-20.md`, 5.3-A, e `tipografia-pecas-2026-08-14.md` | 1,5; 3/2/2/3; citação 4 cm | mantidos "por histórico" (índice de 29/08) — merecem o mesmo banner no topo |

Também: `regra-geral-de-formatacao`, III.9, fala em **quatro linhas** (72 pt) de respiro entre
vocativo e qualificação; `padrao-formatacao-peca`, 5.4, fala em **3 linhas (54 pt)**. Vale 72 pt
(27/08); o de 20/08 é histórico.

## 5. Contradições da própria régua e pontas de verificação

| # | Ponto | Estado | Proposta |
|---|---|---|---|
| 5.1 ✅ | **Ocupação mínima da página**: JSON `paginacao.ocupacao_minima_pct = 70` (vão de até 30 %) × regra 1-B e `validar_diagramacao.py`: **vão ≤ 20 %** | dois limiares para o mesmo defeito | Fixar **20 %** no JSON (é o gate que roda) ou explicar no JSON que 70 % é o piso do `validar_paginacao` e 80 % o do `validar_diagramacao`. Um número só é melhor |
| 5.2 | **RISTJ, art. 343-A** (resumo obrigatório no STJ) | citado como fundamento da SÍNTESE desde 20/08; a própria nota de 20/08 marca `[VERIFICAR — RISTJ oficial retornou 404]`; a regra geral de 27/08 já o cita sem ressalva | Antes de citar **em peça dirigida ao STJ**, abrir o PDF do RISTJ no portal do STJ e conferir número, redação e a Emenda Regimental 53. Para os demais juízos a SÍNTESE se sustenta no CPC 188 e na Recomendação CNJ 144/2023 sem precisar do 343-A |
| 5.3 | **"Só negrito" × "negrito e itálico"** dentro do próprio curso: a aula 2 (vídeo) diz "negrito e só ele"; o PDF da aula 1 diz "negrito, itálico… de forma estratégica" | a casa seguiu o PDF (27/08) | Manter. Registrar em `masterclass-transcrita…`, III.12, que a escolha foi consciente entre as duas falas do autor |
| 5.4 | **EOAB, art. 34, XIV** (deturpar o teor de documento) como fundamento do "dado falso ao lado do print" | não lido na íntegra nesta sessão (só o índice do art. 34) | `[VERIFICAR]` antes de citar |
| 5.5 | **Res. CNJ 469/2022, art. 4º, IV** (PDF pesquisável como "preferência") | citado no `checklist-universal` como V-dossiê; não reaberto aqui | manter como está |

## 6. O que NÃO é lacuna (para ninguém reabrir)

- **Fonte, entrelinha, recuo, citação e margens verticais**: decididos e fundamentados
  (item 2). O curso não prescreve fonte; prescreve legibilidade.
- **Peça sem timbre**: decisão de 03/06 reafirmada em 14/08 e 20/08; o eproc identifica o
  subscritor e o registro no sistema é o protocolo (Res. Conj. GP/CGJ 5/2018, art. 16, § 1º).
- **Numeração de página**: idem.
- **Gráficos (organograma, fluxograma)**: "só entra quando houver série numérica que o quadro
  não resolva" (20/08). O curso concorda: elemento visual só com função.
- **Cor**: a paleta da casa está fixada (20/08) e é sóbria — atende ao "cinza sempre
  funciona" e à extração de cor da marca.
