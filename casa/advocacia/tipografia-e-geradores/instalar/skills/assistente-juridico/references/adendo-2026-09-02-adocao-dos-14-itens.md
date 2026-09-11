# 📐 ADENDO DE 02/09/2026 À REGRA GERAL DE FORMATAÇÃO — a adoção dos 14 itens do curso

> **Ordem do Gabriel, 02/09/2026:** *"adote os 14 itens e corrija os arquivos revogados"*, depois
> da reanálise integral dos dois cursos (Masterclass "Formatando Petições com Excelência" e
> Intensivo "Printscreens de Impacto") registrada no repositório
> `tipografia-juridica/` (arquivos 00 a 04) e no vault. **Este adendo é parte da regra 27**
> (`regra-geral-de-formatacao-2026-08-27.md`) e prevalece sobre o que a contrariar. As medidas
> continuam morando só em `tipografia-vigente.json` (vigente desde 02/09/2026).

## I. O que passa a valer (item por item, com o número do arquivo `02-auditoria-de-lacunas`)

| # | Regra adotada | Como se escreve | Onde está implementado |
|---|---|---|---|
| 3.1 | **Versalete** nos títulos de seção (`#`) e no cabeçalho da peça (vocativo e título, linhas `@@` antes do respiro). Corpo do título continua 12. Caixa-alta no corpo continua proibida. | Pode escrever em caixa alta ou mista: o gerador normaliza para caixa mista e aplica `small-caps`; siglas, romanos e números ficam como estão | `gerar_pdf.py` (CSS `h1.sec`, `p.center.voc`; função `versalete_txt`) |
| 3.2 | **Quadro de requerimentos preliminares** na capa, logo abaixo da SÍNTESE: gratuidade, tutela, prioridade, audiência (CPC 319, VII), segredo. Marcado = pedido; vazio = não pedido. Serve de checklist ao gabinete e à casa. | `> [!requerimentos] Requerimentos preliminares` + linhas `> [x] …` / `> [ ] …` | `gerar_pdf.py` (janela `req`, `requerimentos_html`) |
| 3.3 | **Capitular: recusada.** Ornamento; a aula 1 manda testar antes de adotar e não há dado. | — | `tipografia-vigente.json`, `recusados_2026-09-02` |
| 3.4 | **Etiqueta lateral de lei: recusada.** A margem de 3 cm não comporta; a função é cumprida pelo **dispositivo no rótulo do título** e pela janela `[!cita]`. | — | idem |
| 3.5 | **Numeração automática de seções**: romanos nas seções ("I —"), "I.1 —" nas subseções. Título já numerado à mão não recebe contador. | linha `@numerar` no topo do `.md` | `gerar_pdf.py` (contadores CSS, `ja_numerado`) |
| 3.6 | **Título fica em 12 pt**, igual ao corpo (a v2 do próprio autor faz assim); o azul, o negrito e o versalete já marcam. | — | JSON `titulos.corpo_pt` |
| 3.7 | **Quadro de tutela em duas colunas** ("Probabilidade do direito" × "Perigo de dano", as palavras do art. 300), uma linha por fato com coordenada, **no topo do item** de tutela. | `[quadro] Requisitos do art. 300 do CPC` + tabela de duas colunas | regra; sem sintaxe nova |
| 3.8 | **Série de três imagens** com legenda única (fotos, prints em datas distintas). | `[provatrio] a.png \| b.png \| c.png \| Rótulo A ; Rótulo B ; Rótulo C \| Legenda` | `gerar_pdf.py` (`provatrio_html`) |
| 3.9 | **Quadro de apoio ao lado do documento** reduzido, com os campos que o julgador procura. **Cada teor leva coordenada** — dado ao lado do print é lido como verdadeiro pelo assessor (aula 5), e dado falso ali é má-fé (CPC 77, I; 80, II). | `[provaquadro] doc.png \| Rótulo \| Legenda` seguido de `- Campo: teor (coordenada)` | `gerar_pdf.py` (`provaquadro_html`) |
| 3.10 | **Seta** entre a página inteira e o zoom no `[provapar]` (efeito de ampliação). Traço tracejado no `recorte`: **pendente** — o `recorte` é Swift e só compila no Mac. | automático | `gerar_pdf.py` (CSS `.seta`) |
| 3.11 | **Marca reduzida nas páginas seguintes** do parecer e do contrato: primeira página com timbre completo (e, no parecer, o rodapé com os dados); da segunda em diante só "ESPÍRITO SANTO ADVOCACIA", OAB e "Pg. n". A peça forense continua limpa. | automático | `gerar_pdf_relatorio.py`, `gerar_contrato_pdf.py` (caixas de margem `@page`) |
| 3.12 | **Fórmula "a que couber por distribuição"** no vocativo da inicial sem vara conhecida: "…DA VARA CÍVEL A QUE COUBER POR DISTRIBUIÇÃO DA COMARCA DE …". O `[VERIFICAR — juízo competente]` continua para processo já distribuído. | texto | JSON `capa.vocativo_sem_vara` |
| 3.13 | **Revisar com intervalo**: a revisão final é feita em sessão distinta da redação. | passo 6 do método | `metodo-das-pecas.md` |
| 3.14 | **CPC 425, VI e § 1º** entram como fundamento da prova visual ao lado da Lei 11.419, art. 11, e do CPC 369. | citar os dois | JSON `prova_visual.fundamento`; `04-ligacao-legal.md` |

Também: **um número só para o vão** — `vao_maximo_pct: 20` no JSON substitui "ocupação mínima
70 %", que contradizia o gate (`validar_diagramacao.py` e `validar_paginacao.py` leem o mesmo
número, e o gate de diagramação passou a medir com as margens do JSON, não com 3,0/2,0).

## II. O que continua como estava

Fonte, corpo, entrelinha, recuo, citação, margens, peça sem timbre, sem numeração de página na
peça forense, "Excelentíssimo" no vocativo, caminho de consulta em texto (não URL), 1–3
destaques por página, negrito e itálico. Nenhuma dessas medidas foi reaberta.

## III. A ordem de trabalho (inalterada, com os elementos novos no lugar certo)

texto pronto → elementos visuais no **topo** de cada item (quadro de tutela, `[provaquadro]`,
`[provatrio]`, `[!tempo]`) → capa por último (SÍNTESE em quadro + `[!requerimentos]`) →
diagramar imagens → destacar → gates → **renderizar e olhar página a página**.

## IV. Conferência desta implementação (02/09/2026, regra 26)

Os três geradores foram rodados com fixtures sintéticas (regra 31 — nenhum dado real) em
Chromium 131, e as páginas foram **renderizadas e olhadas**: versalete no vocativo e nos
títulos, numeração "I — / I.1 —", quadro de requerimentos com caixas, seta no par, série de
três, quadro de apoio, e no parecer a primeira página com timbre e rodapé completos e a
segunda só com a marca reduzida e "Pg. 2". Os gates rodaram por inteiro; o único erro
apontado foi de ambiente (a máquina de teste não tem Times New Roman, e o gate acusou
Liberation Serif — no Mac isso não ocorre). **Nada foi instalado no Mac por este ato**: o
instalador copia com backup datado e o primeiro PDF gerado depois dele deve ser olhado.

## V. Fundamento (arquivo `04-ligacao-legal.md`)

Forma livre com finalidade (CPC 188); expressões ofensivas riscadas (78); verdade dos fatos
(77, I; 80, II); prova por qualquer meio (369) e força da reprodução digitalizada (425, VI e
§ 1º; Lei 11.419, art. 11); opção pela audiência expressa (319, VII); tutela (300);
fundamentos determinantes do precedente (489, § 1º, V); nome e OAB (105, § 2º; EOAB 4).
