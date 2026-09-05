---
tipo: canonico-operacional
predio: A — Espírito Santo Advocacia (GFES)
criado: 2026-08-27
tags: [advocacia, tipografia, janelas, peca, padrao]
---

# 🪟 Padrão visual das peças — o que estava errado e o que foi consertado (27/08/2026)

> **Ordem do Gabriel:** *"todas as peças produzidas pelo escritório de advocacia têm que usar
> a mesma tipografia, das janelas suspensas, linha do tempo etc"*.

## A causa raiz: recurso implantado e nunca documentado

As **janelas suspensas** entraram nos três geradores em **26/08/2026**, por ordem do Gabriel.
**Nunca foram documentadas** — nem na skill, nem no crachá, nem em reference. Consequência
direta e verificada: na complementação do caso 5003272, a banca converteu a **linha do tempo
em tabela comum**, supondo que a marcação `~` não fosse suportada. Era suportada desde 26/08.

**Lição para a casa: recurso não documentado é recurso que não existe.** Foi por isso que a
peça saiu fora do padrão, e não por desatenção de quem redigiu.

## O que existe (e agora está documentado)

Oito janelas, reconhecidas pelos três geradores, com sintaxe de callout
(`> [!tipo] Rótulo`): `qualif` · `cita` (rótulo vira referência no rodapé) · `tempo` ·
`calc` · `dout` e `jur` (rótulo vira "Fonte:") · `poderes`.
Linha do tempo: `~ data | evento` dentro de `[!tempo]`, com `~ !data` destacando o marco.

Sintaxe completa e regra de uso:
`skills/assistente-juridico/references/janelas-e-linha-do-tempo-2026-08-27.md`.

## A tipografia divergia em três lugares

| Onde | Estado em 27/08 antes | Canônico (ordem escrita de 20/08/2026) |
|---|---|---|
| `gerar_pdf.py` (peça) | **Times 12 / Charter 11 / recuo 2 cm** ✅ | correto |
| `gerar_pdf_relatorio.py` | Georgia 11,5 ❌ | Times 12 |
| `gerar_contrato_pdf.py` | Georgia 12, recuo 1 cm ❌ | Times 12, recuo 2 cm (citação Charter 11 a **3 cm** desde a tarde de 27/08; *corrigido em 02/09/2026*) |
| `SKILL.md` (dois pontos) | mandava **Georgia 12, recuo 1 cm** ❌ | corrigido em 27/08 |

O Georgia foi revogado em 20/08/2026 pela ordem escrita que fixou **Times New Roman 12** no
corpo e **Charter 11** na citação. A skill continuava mandando Georgia — instrução canônica
contradizendo o gerador.

## Feito em 27/08/2026
1. ✅ Reference nova com a sintaxe das oito janelas e do eixo do tempo.
2. ✅ `SKILL.md` corrigida nos dois pontos (Georgia → Times, recuo 1 cm → 2 cm, citação
   Charter 11 — a 4 cm na manhã de 27/08, **3 cm** desde a tarde; corrigido de novo em 02/09/2026).
3. ✅ Crachá da Lourdes: a entrega da peça agora exige o repertório visual, com a vedação
   expressa de desenhar linha do tempo com tabela ou hífen.
4. 🔄 Peça do 5003272 em conversão para janelas + linha do tempo (o gerador de peça **já
   estava com a tipografia certa**, então o protocolo de amanhã não foi afetado pela
   divergência).

## Pendente
✅ *(feito em 27/08 à tarde; medidas finais em `tipografia-vigente.json` — citação a 3 cm, não 4; nota corrigida em 02/09/2026)* Unificar a tipografia de `gerar_pdf_relatorio.py` e `gerar_contrato_pdf.py` (Georgia →
Times 12, recuo 2 cm, citação Charter 11). **Não executado agora para não conflitar**
com a tarefa em curso que está consertando os metadados dos mesmos três arquivos (defeito do
rastro de navegador). Fazer assim que ela fechar, com backup `.bak` datado ao lado, e conferir
gerando um PDF de teste de cada.
