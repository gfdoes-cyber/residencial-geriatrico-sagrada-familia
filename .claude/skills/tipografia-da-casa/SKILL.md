---
name: tipografia-da-casa
description: Tipografia e estrutura HTML obrigatórias de toda peça, parecer, relatório e auditoria da casa GFES (vigente desde 27/08/2026). Use sempre que for produzir um documento jurídico ou de conformidade para entrega.
---

# Tipografia da casa

O CSS completo e o esqueleto de peça estão em `modelo-artefato.html`, nesta pasta. Copie o
`<style>` inteiro, sem alterar nada. Grave o HTML no scratchpad e envie com SendUserFile
(display render). O Gabriel abre no navegador e salva em PDF.

## TIPOGRAFIA DA CASA — vigente desde 27/08/2026. Não altere nada disto.

| | |
|---|---|
| Corpo | **Times New Roman 12 pt**, justificado |
| Entrelinha | **1,35** (nunca 1,5 — é entrelinhamento demais) |
| Recuo de 1ª linha | **2 cm** |
| Citação em bloco | **Charter 11 pt**, recuo **3 cm**, entrelinha 1,3 — sem itálico e sem aspas |
| Margens | **superior 2,3 · direita 3 · inferior 1,8 · esquerda 3** (cm) |
| Órfãs / viúvas | **2 / 2** — 3/3 é defeito, não solução: torna a restrição impossível em parágrafo de 4 linhas e o Chrome descarta a viúva |
| Destaque | **negrito e itálico**, com parcimônia |
| Proibido | sublinhado, caixa-alta no corpo, marca-texto |
| Endereçamento ao juízo | **nunca se separa nem se hifeniza**; **quatro linhas** entre ele e a qualificação |
| Última página | nunca só com fecho ou só com assinatura — **mínimo 8 linhas** |

**Assinatura — sempre exatamente assim, centralizada, três linhas:**

```html
<div class="assin">
  <p><b>Gabriel Fabrízio do Espírito Santo</b></p>
  <p>Advogado</p>
  <p>OAB/SC 53.040</p>
</div>
```

**Regras de uso das janelas:** `qualif` para qualificação da parte · `cita` para dispositivo ou
documento dos autos · `tempo` para linha do tempo · `calc` para conta ou ordem de atos ·
`dout` para doutrina. **Linha do tempo é sempre janela — nunca tabela, hífen ou seta.**
Cada janela leva rótulo em `<span class="jrot">`.

**Prova visual:** afirmou o que um documento diz → **entra o recorte**, com o trecho decisivo
transcrito na legenda. Imagem nunca vem sozinha, e a etiqueta diz **o efeito jurídico**, não o
nome do campo.

**Os dois últimos passos, nesta ordem, nunca invertidos:** (1) diagramar as imagens;
(2) destacar em negrito/itálico.

## Conferência antes de entregar (não há gate automático aqui)

Página em branco · linha órfã ou viúva · título no pé da página · última página só com fecho
ou assinatura · página com menos de 70% de ocupação · sublinhado, caixa-alta no corpo ou
marca-texto.

**Para fechar um buraco, nesta ordem:** (1) tire linhas antes do bloco indivisível;
(2) enxugue a redação sem perda jurídica; (3) nunca mexa em fonte, corpo, entrelinha, margem
ou recuo. Encurtar a linha vence economizar página. O tamanho da peça é resultado, não meta.
