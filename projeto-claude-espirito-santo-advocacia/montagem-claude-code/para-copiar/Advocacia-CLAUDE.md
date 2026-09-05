---
tags: [canonico, escritorio, claude-code, raiz-permanente]
criado: 2026-09-05
atualizado: 2026-09-05
---
# CLAUDE.md — Espírito Santo Advocacia (GFES): a sessão do escritório no Claude Code
Gabriel Fabrízio do Espírito Santo, OAB/SC 53.040 (Espírito Santo Sociedade Individual de Advocacia,
CNPJ 50.411.747/0001-00). Esta pasta, `Advocacia/`, é a **raiz permanente do escritório** (05/09/2026).
A técnica da casa está no plugin **gfes** (fonte única: `02 - SKILLS E AGENTES/`) — as regras longas
se leem nas skills, nunca de memória. Este arquivo é o mínimo que vale em toda sessão.
## 1. Abrir o escritório
1. Ler `00 - SEDE/00 - LEIA-ME — como abrir o escritório.md` e o `00 - SEDE/02 - RADAR DO ADVOGADO`;
   dizer em uma linha se há prazo correndo. O radar é ÚNICO (04/09/2026): vive na Sede, a dona é a Lourdes.
2. Assunto jurídico → agente `gfes:lourdes` (todo trabalho jurídico é **entregue por ela**). Sistema,
   automação, esteira, skill → `gfes:teo`. Marca da advocacia → `gfes:bia`. Residencial (ILPI) → Dora,
   Ciro e Nina, **em sessão aberta em `Residencial/`**, nunca aqui.
3. Caso novo → `/gfes:portaria` → pasta `01 - CLIENTES/<cliente>/<CNJ - apelido>/` a partir de
   `00 - SEDE/modelos/` (00 - CLIENTE, 00 - CASO, PECA, PARECER); índice e radar atualizados.
## 2. As três travas do cofre (lei, não preferência)
⛔ Publicidade da ILPI nunca se mistura à advocacia (Prov. CFOAB 205/2021). 🔒 Dado de saúde de
residente não entra em peça, parecer ou registro jurídico — nem anonimizado (LGPD arts. 7º e 11; EOAB
art. 34, VII): **`Residencial/` não se lê desta sessão.** 💰 Conta, contrato, nota, domínio e CNPJ das
duas empresas não se misturam (CC art. 50).
## 3. O que a IA nunca faz
Não assina, não protocola, não envia, não publica, não paga, não digita senha/PIN/token/2FA, não cria
conta, não aceita termo — monta até a última tela e para. Não abre intimação pendente (abrir dá
ciência) nem clica "Abrir Prazo". Nada que vá a cliente, tribunal ou terceiro menciona IA. Não pede
sustentação oral nem faz inscrição para ela (05/09/2026), salvo ordem expressa naquele caso. Download
só com autorização expressa. Nunca apaga em definitivo (`_to_delete/`, `.trash/`, `.bak`).
WhatsApp (skill `whatsapp`): **a casa lê e escreve, o Gabriel envia** — nada sai sem ordem dele, uma a uma.
## 4. O método de um caso (o resumo; o inteiro está em `assistente-juridico`)
0. **Leitura integral, cláusula pétrea (14/08/2026):** o processo se lê da primeira à última página
   antes de qualquer parecer, caçando defeitos, nulidades, brechas e jurisprudência favorável. Cópia
   integral do eproc ("Download Completo → Baixar Todas as Partes") em `01-autos/`. Não leu tudo?
   parecer retido. Consulta pedida pelo Gabriel = papel de relator: relatório completo para ele redigir.
1. **Prazo primeiro**, recontado na fonte (CPC 219 e 224; JEC dias úteis; CLT 8 dias úteis); não
   apurável = VAZIO com a pendência escrita, nunca chutado.
2. **Regra do portador — o bolso antes da pá (19/08/2026):** primeiro artefato é a ficha de fatos +
   pedido de documentos ao cliente. Fato = valor + coordenada (`Ev. N, fl. X`) + status (DOC · OFC ·
   REL · VAZIO) + caminho crítico. VAZIO REBAIXA: não vai ao topo, não vai ao cliente, não vira marco.
3. **Antifabricação:** lei só do Planalto (`grep` nos códigos em
   `skills/direito-civil-avancado/references/codigos/`), súmula e acórdão só no sítio do tribunal, ementa
   lida; não conferiu → argumento sem a citação. **A Lourdes é sempre consultada** (27/08/2026).
4. **Sigilo defensivo (24/08/2026):** do relato do cliente só o que beneficia; a defesa se constrói
   pelos autos; nunca afirmar fato sabidamente inverídico.
5. TJSC → skill `tjsc` (órgão, súmula, precedente, pesquisa filtrada, prazo e feriado); recurso →
   `recursos-e-tribunais` (quem julga, quem admite, os dois prazos); peça → `requisitos-das-pecas`.
6. Assuma e resolva: perguntar ao Gabriel é último recurso — só credencial, assinatura, dinheiro,
   decisão de negócio, ato do mundo real e mudança de regra. Looping: nada fecha sem conferir o escopo.
## 5. A forma — cláusula constitucional (04/09/2026), unificada pela regra 35 (05/09/2026)
Antes de escrever ou regenerar peça, parecer ou memorial, ler nesta ordem: (1) skill `forma-da-peca`;
(2) `assistente-juridico/references/tipografia-vigente.json` — as medidas, do arquivo, nunca da
memória; (3) `regra-geral-de-formatacao-2026-08-27.md`; (4) `janelas-e-linha-do-tempo-2026-08-27.md`;
(5) `regra-do-portador-2026-08-19.md` + a `00 - CASO.md`; (6) `prova-visual-automatica-2026-09-05.md`;
(7) `caderno-de-erros-da-casa-2026-08-27.md` (reabre antes de entregar); (8) o modelo da Sede.
- **Regra 35:** a primeira página é capa — `@@` vocativo → `[!qualif]` → abertura → `# SÍNTESE` =
  `[quadro] O que esta peça sustenta` + `> [!linha]` (linha do tempo **horizontal, esquerda → direita,
  com seta**; 4 a 8 marcos que decidem; um só `!`; todo marco com `(Ev. N)`; ≤ 70 caracteres;
  DD/MM/AAAA) → `# I — DOS FATOS` com o `[!tempo]` completo. Recurso: TEMPESTIVIDADE com `[!linha]`.
- **Regra 34:** print + marcação (etiqueta vermelha #9E2121, `scripts/etiqueta_prova.py`) +
  explicação (`[!cita]` literal acima; legenda com documento + coordenada + o que prova) em toda peça
  argumentativa — `[provapar] pag | zoom | Rótulo | Legenda`; gate `validar_prova_visual.py`.
- Markdown puro; tag HTML crua aborta. Jurisprudência em texto, nunca em print (CPC art. 369, não 396).
- Parecer ao cliente (03/09/2026): logo GFES, no máximo duas folhas, língua simples, sem histórico
  interno, sem agente/andar/regra/VAZIO/gerador no documento (gate `validar_saida_cliente.py`).
## 6. Gerar, conferir, entregar
- `.md` em `02-pecas/` (peça) ou `03-parecer-e-analise/` (parecer): `<TIPO>-<processo curto>-<AAAA-MM-DD>.md`.
- A esteira (`03 - ESTEIRA/`) gera o PDF com Chrome e Times em até 2 min e roda os 8 gates; à mão:
  `python3 "02 - SKILLS E AGENTES/skills/assistente-juridico/assets/gerar_pdf.py" "<peça>.md" --tipo <tipo>`
  (`gerar_pdf_relatorio.py` parecer · `gerar_contrato_pdf.py` contrato · `--emitente` em documento da parte).
- Veredito **LIBERADO** ou a peça volta: para fechar vão, tirar linhas antes do bloco indivisível ou
  enxugar; **nunca** mexer em fonte, corpo, entrelinha, margem ou recuo. Conserta-se a peça, não o gate.
- **A vista:** renderizar e olhar a primeira, a última e toda página com janela, eixo, tabela ou prova.
- Entrega: `open "<pdf>"` e `open "<pasta do caso>"`; conclusão, prazo e data-limite, órgão julgador,
  o que foi verificado e onde, a ficha de fatos com os VAZIOS visíveis, pendências, próximo ato do
  Gabriel. Registro na `00 - CASO.md`; ao terminar, `git commit` do vault (histórico em `~/Backups/vault-git`).
- Entrega que só existe na resposta é entrega perdida: grave antes de responder.
## 7. A técnica muda só na fonte
Regra, skill, agente, gerador ou gate mudam em `02 - SKILLS E AGENTES/` → sobe a versão em
`.claude-plugin/plugin.json` (description ≤ 500 caracteres) → `python3 empacotar.py --saida
"$HOME/Documents/Claude outputs"` → instalar o `.plugin` no app; aqui, `/reload-plugins`. Uma sessão por
vez sobre a configuração, com backup datado antes da primeira escrita (regra 33). Revogado ganha tarja
datada; quem apaga é o Gabriel.
## 8. A máquina
Mac do usuário `gabriel`; `/usr/bin/python3` é 3.9.6 (código de rotina sem `match`, `X | Y`, `tomllib`,
`datetime.UTC`); sem Node/npm, por decisão; `launchd` com binário absoluto; `LC_ALL=en_US.UTF-8` em
`pbcopy`/`rsync`; iCloud faz eviction (`brctl download`); a pasta é `iPhone` com P maiúsculo. Chrome
e Times New Roman existem aqui — a peça definitiva fecha aqui. Resíduo de Windows, de `~/Documents/casos/`
ou de `~/.claude-gfdoes/skills/` em nota viva é erro a corrigir, não caminho a seguir.
Registro da montagem e mapa completo: `00 - SEDE/00 - LEIA-ME — como abrir o escritório.md` ·
skill `mapa-da-casa` · `00 - SEDE/03 - Auditorias e protocolos do escritório/`.
