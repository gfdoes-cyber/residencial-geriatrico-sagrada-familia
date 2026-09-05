---
tipo: clausula-petrea
predio: A — Espírito Santo Advocacia (GFES)
criado: 2026-08-27
tags: [advocacia, canonico, clausula-petrea, tipografia, assinatura, regra-24]
---

# 🖋️📐 CLÁUSULA PÉTREA — a marca do advogado e a tipografia única das peças

> **Ordem do Gabriel, 27/08/2026:** *"sempre coloque meu nome inteiro, [e] abaixo Advogado, e
> logo abaixo OAB/SC 53.040, como uma marca registrada do advogado, sempre com dois espaços
> abaixo do texto final para não ficar misturado. (...) qualquer peça produzida tanto pelo
> escritório de advocacia, para a advocacia ativa como para os clientes particulares, tem que
> sempre seguir esse padrão. Anote isso como cláusula canônica, não deixa de forma alguma
> passar qualquer peça que não seja nessa tipografia."*
> É a **regra 24** do CLAUDE.md.

## (a) A assinatura — marca registrada do advogado

Três linhas centradas, com **dois espaços de respiro acima** para não se misturar ao texto:

| Linha | Conteúdo |
|---|---|
| 1 | **Gabriel Fabrízio do Espírito Santo** (nome inteiro) |
| 2 | **Advogado** — ou **Advogado dativo**, quando a atuação for por nomeação |
| 3 | **OAB/SC 53.040** |

**No markdown escreve-se apenas `@assinatura`** (ou `@assinatura Advogado dativo`), e os três
geradores montam o bloco. **É impossível uma peça sair com assinatura fora do padrão** — a
regra deixou de depender de quem redige e passou a ser garantida pela ferramenta.
⚠️ A regra antiga continua: na assinatura vai **"Advogado dativo"**, nunca "Curador especial";
o encargo vai no corpo da peça.

## (b) A tipografia — a mesma nos três geradores (unificada em 27/08/2026)

**Times New Roman 12** no corpo, títulos e quadros · **Charter 11** na citação em bloco,
recuada **3 cm** · entrelinha **1,35** · recuo de primeira linha **2 cm** · destaque por
**negrito e itálico**, com parcimônia · versalete nos títulos (02/09) · nunca sublinhar, nunca
caixa-alta no corpo. *(Corrigido em 02/09/2026: esta nota trazia 4 cm, 1,5 e "só negrito",
medidas revogadas na tarde de 27/08. Fonte única: `tipografia-vigente.json`.)*

Antes de hoje os geradores divergiam: o de peça já estava correto, mas o de **relatório**
estava em Georgia 11,5 e o de **contrato** em Georgia 12 com recuo de 1 cm — os dois ficaram
para trás quando o Georgia foi revogado em 20/08. A própria `SKILL.md` ainda mandava Georgia.
Tudo corrigido.

## (c) O repertório visual — o mesmo nos três

As sete **janelas suspensas** (`[!qualif]`, `[!cita]`, `[!tempo]`, `[!calc]`, `[!dout]`,
`[!jur]`, `[!poderes]`) e a **linha do tempo** (`~ data | evento`; `~ !data` destaca o marco).
⚠️ **Nunca** desenhar linha do tempo com tabela, hífen ou seta.
Sintaxe: `skills/assistente-juridico/references/janelas-e-linha-do-tempo-2026-08-27.md`.

Estado antes de hoje: só o gerador de peça tinha as sete. O **relatório não tinha nenhuma**
(usava um vocabulário próprio: destaque/favoravel/atencao/processo) e o **contrato tinha três**.
Hoje os três aceitam o repertório completo, e o relatório manteve os tipos antigos para não
quebrar documentos já feitos.

## (d) Respiro depois do título
Todo título ganha um espaço antes de o texto começar a discorrer. Aplicado nos três geradores.

## (e) Referência de qualidade
As **peças do caso David Vargas Carrion** (26/08/2026) são o padrão aprovado pelo Gabriel.

## Defeito antigo descoberto e corrigido no mesmo ato
O **gerador de contrato nunca teve suporte a tabela** — qualquer contrato com tabela saía com
a marcação crua (`|---|`) no PDF. A memória da casa afirmava que ele tratava tabela, e estava
errada. Suporte portado do gerador de peça em 27/08/2026.

Backups datados ao lado de cada gerador: `*_pre-times-20260827.py.bak`.
Ver [[2026-08-27 — PADRÃO VISUAL das peças · janelas, linha do tempo e a tipografia que divergia]].
