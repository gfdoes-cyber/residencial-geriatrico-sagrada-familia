# 🪟 JANELAS SUSPENSAS E LINHA DO TEMPO — a sintaxe (27/08/2026)

> **Ordem do Gabriel (27/08/2026):** *"todas as peças produzidas pelo escritório de advocacia
> têm que usar a mesma tipografia, das janelas suspensas, linha do tempo etc"*.
> **Por que este arquivo existe:** as janelas foram implantadas nos geradores em **26/08/2026**,
> por ordem dele, e **nunca foram documentadas**. Resultado: a banca não sabia que existiam. Na
> complementação do caso 5003272 a linha do tempo foi convertida em tabela comum porque a
> redatora supôs que a marcação não era suportada. Era. **Recurso não documentado é recurso
> que não existe.**

## A sintaxe (padrão de callout, igual ao Obsidian)

```
> [!tipo] Rótulo da janela
> Primeira linha do conteúdo.
> Segunda linha do conteúdo.
```

A janela abre com `> [!tipo]` e continua enquanto as linhas começarem com `>`. Uma linha em
branco sem `>` fecha a janela. O rótulo é opcional em algumas, obrigatório nas de fonte.

## As oito janelas (nove desde 02/09/2026 — ver adendo abaixo)

| Escreva | Cor / uso | Comportamento do rótulo |
|---|---|---|
| `[!qualificacao]` ou `[!qualif]` | azul-marinho — qualificação das partes | rótulo no topo |
| `[!citacao]` ou `[!cita]` | cinza-oliva — transcrição de documento ou decisão | **rótulo vai para o rodapé da janela**, como referência |
| `[!linhadotempo]` ou `[!tempo]` | azul — cronologia dos fatos | rótulo no topo; conteúdo em eixo (ver abaixo) |
| `[!calculo]` ou `[!calc]` | bege-dourado — demonstrativo, conta, teto | rótulo no topo |
| `[!doutrina]` ou `[!dout]` | verde — doutrina, poucas linhas | rótulo vira **"Fonte: ..."** no rodapé |
| `[!sumula]`, `[!jurisprudencia]` ou `[!jur]` | roxo — súmula, tese, ementa | rótulo vira **"Fonte: ..."** no rodapé |
| `[!poderes]` ou `[!objeto]` | azul — poderes da procuração, objeto do contrato | rótulo no topo |

## A linha do tempo

Dentro da janela `[!tempo]`, cada evento é uma linha com `~`:

```
> [!tempo] As diligências de citação
> ~ 12/08/2024 | carta ao endereço de Salvador, devolvida
> ~ !16/09/2025 | carta ENTREGUE na Rua Mariano Borges, assinada por terceiro
> ~ 25/02/2026 | juízo declara a ré em local incerto e não sabido
```

- Formato: `~ data | descrição do evento`.
- **`~ !data | ...`** (com exclamação antes da data) **destaca o marco** — use no fato que
  ganha o caso, e só nele. Quem destaca tudo não destaca nada.
- O gerador desenha o trilho e os marcos. Não desenhe linha do tempo com tabela, hífen ou
  seta: sai sem o eixo e quebra o padrão da casa.

## Regra de uso (o que evita virar enfeite)

1. **Janela tem função, não decoração.** Ela existe para o leitor achar em dois segundos o que
   decide: a data que ganha o caso, o valor, o dispositivo transcrito, a fonte da tese.
2. **Uma janela por ideia.** Peça com janela em todo parágrafo tem o mesmo efeito de peça sem
   janela nenhuma (Von Restorff — canônica do design da informação, 24/08/2026).
3. **Transcrição de decisão ou documento vai em `[!cita]`**, com o rótulo trazendo a coordenada
   (evento, página). A citação em bloco simples (`> ` sem `[!tipo]`) continua existindo para o
   texto de lei corrido.
4. **Súmula, tese e ementa vão em `[!jur]`**, com a referência completa no rótulo — que o
   gerador imprime como "Fonte:". Vale a regra de ouro: só entra o que foi lido, com link
   estável.
5. **Conta e demonstrativo vão em `[!calc]`.**
6. As janelas valem para **peça, parecer, relatório, contrato e procuração** — os três
   geradores as reconhecem.

## Tipografia (a mesma em todo documento do escritório)

**Nenhuma medida mora neste arquivo.** A fonte única das medidas é
`references/tipografia-vigente.json` (regra 25): é lá que estão fonte, corpo, entrelinha,
recuo, margens e destaque, e é contra ele que `validar_paginacao.py` mede o PDF. Este arquivo
só diz **o que existe** e **quando usar**. *(Corrigido em 02/09/2026: a versão anterior repetia
aqui três medidas já revogadas em 27/08 — citação a 4 cm, entrelinha 1,5 e "só negrito" —, erro
11 do caderno de erros.)*

## Adendo de 02/09/2026 — a nona janela e as três provas novas

| Escreva | Uso | Como |
|---|---|---|
| `[!requerimentos]` ou `[!req]` | **quadro de requerimentos preliminares** na capa, logo abaixo da SÍNTESE (gratuidade, tutela, prioridade, audiência, segredo) | cada linha `> [x] texto` (pedido) ou `> [ ] texto` (não pedido); o gerador desenha as caixas |
| `[provatrio] a.png \| b.png \| c.png \| Rótulo A ; Rótulo B ; Rótulo C \| Legenda` | **série de três imagens** com legenda única (fotos, prints em datas distintas) | três colunas, borda e sombra em cada imagem |
| `[provaquadro] doc.png \| Rótulo \| Legenda` seguido de linhas `- Campo: teor (coordenada)` | **quadro de apoio** ao lado do documento reduzido: os campos que o julgador procura | documento à esquerda, seta, tabela à direita; **cada teor leva coordenada** |
| `@numerar` (linha própria no topo) | liga a **numeração automática** de seções (I —, I.1 —) | título já numerado não recebe contador |

Versalete: títulos `#` e as linhas `@@` do cabeçalho (vocativo, título da peça) saem em
**versalete**; podem ser escritos em caixa alta ou em caixa mista, o gerador normaliza.
O `[provapar]` ganhou uma **seta** entre a página inteira e o zoom. Regra completa:
`regra-geral-de-formatacao-2026-08-27.md`, adendo de 02/09/2026.

## O endereçamento ao juízo (ordem do Gabriel, 27/08/2026)

**O vocativo NUNCA se separa.** Não se hifeniza nem se parte no meio de palavra: a quebra só
acontece entre palavras inteiras. `... DA VARA ES-TADUAL` é erro de acabamento e fica amador
no primeiro olhar do juiz.

Corrigido na raiz: o bloco centralizado (`@@`, classe `p.center`) recebeu `hyphens: none` e
`word-break: keep-all` nos três geradores. Quem escreve não precisa fazer nada.

**Quatro linhas de respiro** separam o endereçamento da qualificação (`.vocgap`, 72pt).
O gerador insere sozinho, inclusive quando a qualificação vem em janela `[!qualif]` — antes
de 27/08/2026 o gatilho só reconhecia a qualificação escrita em negrito, e por isso o
vocativo saía grudado na janela.

⚠️ Confirmar **na vista** (regra 26): renderizar a página 1 e olhar o cabeçalho antes de entregar.
