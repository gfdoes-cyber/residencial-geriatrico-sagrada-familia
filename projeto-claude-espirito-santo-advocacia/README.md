# Projeto "Espírito Santo Advocacia" no app do Claude

Material de configuração do projeto no app (claude.ai → Projetos → Novo projeto →
"Espírito Santo Advocacia").

> Desde 05/09/2026 a casa roda no app pelo plugin **gfes 1.4.0** (pacote em
> `~/Documents/Claude outputs/gfes-1.4.0.plugin`, fonte única em
> `Advocacia/02 - SKILLS E AGENTES/` no vault). Este material continua valendo para o projeto do
> app sem plugin. A montagem do mesmo ecossistema no Claude Code do Mac está em
> [`montagem-claude-code/`](montagem-claude-code/LEIA-ME.md).

## 1. Instruções do projeto

Cole o conteúdo integral de [`instrucoes-do-projeto.md`](instrucoes-do-projeto.md) na caixa
**Instruções do projeto**. O arquivo já reúne, numa única caixa, as regras da casa (travas,
método, prazos, direito, entrega) e a tipografia vigente desde 27/08/2026 com o `<style>`
completo.

## 2. Modelo do artefato

[`modelo-artefato.html`](modelo-artefato.html) é o esqueleto de peça com o CSS da casa e a
assinatura padrão. Serve para conferir o resultado do app e como base local: abrir no
navegador e salvar em PDF.

## 3. O que subir em "Conhecimento do projeto"

Estes arquivos vivem na fonte única do plugin, no vault do Mac —
`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/02 - SKILLS E AGENTES/`
(desde 05/09/2026; o caminho antigo `~/.claude-gfdoes/skills/` é resíduo) — e **não estão neste
repositório**. Arraste-os para a base de conhecimento do projeto (caminhos relativos à fonte):

```
skills/forma-da-peca/SKILL.md                                              (regra 35, 05/09/2026)
skills/assistente-juridico/references/tipografia-vigente.json
skills/assistente-juridico/references/regra-geral-de-formatacao-2026-08-27.md
skills/assistente-juridico/references/caderno-de-erros-da-casa-2026-08-27.md
skills/assistente-juridico/references/janelas-e-linha-do-tempo-2026-08-27.md
skills/assistente-juridico/references/regra-do-portador-2026-08-19.md
skills/assistente-juridico/references/prova-visual-automatica-2026-09-05.md (regra 34, 05/09/2026)
skills/requisitos-das-pecas/SKILL.md
skills/tjsc/SKILL.md
skills/recursos-e-tribunais/SKILL.md
skills/execucao-penal/SKILL.md
skills/eproc-tjsc/SKILL.md
```

**O caderno de erros é o mais importante da lista.** É o único arquivo que ensina a não
repetir erro que a casa já cometeu.

Se o projeto for de ILPI, suba em vez das jurídicas `skills/ilpi-conformidade/SKILL.md` e
`skills/registro-assistencial-e-sistema/SKILL.md`. **Nunca no mesmo projeto que advocacia**
(travas 1 e 2).

## 4. O que não atravessa para o app

| Fica na máquina local | Por quê |
|---|---|
| Os gates (`validar_paginacao`, `validar_diagramacao`, `forense_documento`) | são Python; no app ninguém mede o PDF — a conferência é do olho |
| O radar de prazos | é único desde 04/09/2026: vive na Sede do vault (`00 - SEDE/02 - RADAR DO ADVOGADO`), a dona é a Lourdes; o app não lê o vault |
| O vault Obsidian | o app não escreve no disco |
| O eproc, o DJEN e o navegador | o app não tem o Chrome pareado |
| OCR de PDF escaneado | é o binário Vision local; o app lê PDF nativo |
| Prova etiquetada (`recorte`, `etiqueta_prova.py`) | são scripts; no app a imagem vai pronta |
| Leitura de WhatsApp e transcrição de áudio | banco local e Speech on-device |

**Divisão recomendada:** o app para pensar, redigir e conversar; a máquina local para
prazos, autos, eproc, gates e registro. O que o app produzir volta para a máquina quando
tiver de virar PDF definitivo e passar pelos gates.
