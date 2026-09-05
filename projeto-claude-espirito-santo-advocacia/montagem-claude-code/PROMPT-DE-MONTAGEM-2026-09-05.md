---
tipo: prompt-de-montagem
setor: advocacia
criado: 2026-09-05
atualizado: 2026-09-05
tags: [claude-code, ecossistema, plugin-gfes, raiz-permanente, montagem, prompt]
---
# PROMPT DE MONTAGEM — o ecossistema da casa dentro do Claude Code (05/09/2026)
> **Para o Gabriel — como usar este arquivo (3 passos):**
> 1. No Terminal do Mac: `cd "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia"` e depois `claude` (o perfil que roda a casa é o de sempre; se você usa o alias, use o alias).
> 2. Cole **a PARTE 1 inteira** (do título "PROMPT" até "FIM DO PROMPT") como primeira mensagem. As PARTES 2, 3 e 4 são os arquivos que o Claude Code vai gravar — ele lê daqui, você não precisa colar.
> 3. Quando ele terminar, leia o relatório final (seção 8 da Parte 1) e faça só os atos que são seus: conceder Acesso Total ao Disco ao `/usr/bin/python3` e ao `/bin/zsh` se a esteira pedir, e responder às duas perguntas que ele pode fazer.
>
> Tudo o que este prompt manda montar **já existe no disco** — nada é inventado. O plugin, os agentes, as skills, os geradores, os gates, os modelos, a esteira e os registros foram construídos entre 13/08 e 05/09/2026 e moram na fonte única `Advocacia/02 - SKILLS E AGENTES/`. O Claude Code só precisa **ligar** tudo isso a ele mesmo.
---
## PARTE 1 — O PROMPT (colar no Claude Code)
PROMPT — MONTAR O ECOSSISTEMA DA CASA NO CLAUDE CODE (ordem do Gabriel, 05/09/2026)
Você está no Mac do Gabriel Fabrízio do Espírito Santo, advogado (OAB/SC 53.040), titular da Espírito Santo Advocacia (GFES, CNPJ 50.411.747/0001-00) e sócio administrador do Residencial Sagrada Família (ILPI · Antunelli e Antunelli Instituição de Idosos Ltda., CNPJ 02.145.891/0001-08). Você vai montar, dentro do Claude Code, o ecossistema de trabalho que a casa construiu entre 13/08 e 05/09/2026 e que hoje roda no app do Claude (Cowork) pelo plugin `gfes` 1.4.0. **Nada aqui é para ser criado do zero: é para ser ligado.** A fonte de tudo é a pasta `Advocacia/02 - SKILLS E AGENTES/` do vault do Obsidian.
Trabalhe em português, na norma culta. Registre cada passo concluído numa nota datada do vault (seção 7). Não pergunte ao Gabriel o que puder apurar no disco; pergunte só o que está na seção 8.
### 0. As regras que valem antes de qualquer comando
1. **Você não assina, não protocola, não envia mensagem, não publica, não paga, não digita senha, PIN, token ou 2FA, não cria conta, não aceita termo.** Monta tudo até a última tela e para. Nada que vá a cliente, tribunal ou terceiro menciona IA.
2. **As três travas do cofre (lei, não preferência):** publicidade da ILPI nunca se mistura à advocacia (Prov. CFOAB 205/2021); dado de saúde de residente **não entra** em peça, parecer, campanha ou registro jurídico, nem anonimizado (LGPD arts. 7º e 11; EOAB art. 34, VII); conta, contrato, nota, domínio e CNPJ das duas empresas não se misturam (CC art. 50). Nesta montagem isso significa: **a pasta `Residencial/` do vault não é lida nem adicionada à sessão do escritório.**
3. **Nunca apague nada em definitivo.** Arquivo que sai vai para `_to_delete/`, `.trash/` ou ganha sufixo `.bak-<AAAAMMDD>-<motivo>`. Antes de editar qualquer arquivo de configuração (`CLAUDE.md`, `AGENTS.md`, `settings.json`, `.plist`, skill ou agente) faça o backup datado ao lado — regra 33 da casa (uma sessão por vez sobre a configuração; backup antes da primeira escrita).
4. **Regra nova só existe na fonte.** Mudança de skill, agente, gerador ou gate é feita em `02 - SKILLS E AGENTES/` e vira versão do plugin (`empacotar.py`). Memória de sessão, resposta de chat ou arquivo solto não é lugar de regra.
5. **Looping:** nenhuma entrega fecha sem conferir o resultado contra o escopo deste prompt, seção a seção; o que faltou volta para execução até 100 % ou até um ato que só o Gabriel pode praticar.
6. **Assuma e resolva:** perguntar ao Gabriel é último recurso. Esgote: o disco → o vault → a fonte primária. Divergência entre fontes não para o trabalho: decida pela mais forte (a nota mais nova, o JSON de medidas, o código que roda) e diga qual.
### 1. Reconheça a máquina antes de mexer (só leitura)
Rode e anote no relatório:
```
whoami; sw_vers; uname -a
which claude; claude --version
echo "CLAUDE_CONFIG_DIR=$CLAUDE_CONFIG_DIR"; alias | grep -i claude
ls -la ~/.claude ~/.claude-gfdoes 2>/dev/null | head -40
which python3; /usr/bin/python3 --version; which node npm            # não há Node nem npm: é decisão da casa, não falta
ls "/Applications/Google Chrome.app" && fc-list 2>/dev/null | grep -i "times new roman" | head -2 || system_profiler SPFontsDataType 2>/dev/null | grep -i "Times New Roman" | head -2
ls "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia"
cat "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/02 - SKILLS E AGENTES/.claude-plugin/plugin.json"
launchctl list | grep -i gfes
ls ~/Library/LaunchAgents | grep -i gfes
ls "$HOME/Documents/Claude outputs" | grep plugin
git -C "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone" status --short | head; git -C "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone" log --oneline -3
```
Fatos conhecidos, para confrontar com o que você achar: MacBook Air M5, macOS 26; usuário `gabriel`; **Python do sistema é 3.9.6** (`/usr/bin/python3`) — nada de `match/case`, `X | Y`, `tomllib`, `datetime.UTC` em código que vá para rotina; **não há Node/npm** e não se instala; o perfil do Claude Code que roda a casa esteve em `~/.claude-gfdoes/` (`~/.claude` era o alias `claude-max`) — **descubra qual perfil está ativo agora** (`CLAUDE_CONFIG_DIR`, alias, `/status`) e instale o plugin **nesse** perfil; **iCloud faz eviction**: `cat` vazio em arquivo com tamanho > 0 pede `brctl download <arquivo>` antes de qualquer conclusão; a pasta é `iPhone` com P maiúsculo (glob e permissão diferenciam caixa); `launchd` não lê `~/.zshrc` (binário absoluto sempre); `LC_ALL=en_US.UTF-8` para acento em `pbcopy`/`rsync`.
Se o que você achar contrariar um fato desta lista, **vale o disco** — e registre a divergência.
### 2. O que já existe (o mapa que você vai ligar — não recrie nada disto)
**A raiz permanente do escritório** (05/09/2026) é `Advocacia/` dentro do vault (`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/`):
```
Advocacia/
  00 - SEDE/                         entrada única: 00 - LEIA-ME — como abrir o escritório.md (o protocolo de sessão),
                                     01 - ÍNDICE DE CLIENTES E CASOS, 02 - RADAR DO ADVOGADO (espelho do painel web),
                                     modelos/ (00 - CLIENTE, 00 - CASO, PECA, PARECER), 03 - Auditorias e protocolos do escritório/
  01 - CLIENTES/<cliente>/<CNJ - apelido>/
      00 - CASO.md                   ficha viva: identificação, síntese, FICHA DE FATOS (valor + coordenada + status + caminho crítico),
                                     pedido de documentos, linha do tempo, registro
      01-autos/  02-pecas/  03-parecer-e-analise/  04-provas-e-comunicacoes/{documentos,provas/<AAAA-MM-DD>,whatsapp}
  02 - SKILLS E AGENTES/             A FONTE ÚNICA do plugin gfes: .claude-plugin/plugin.json (1.4.0), skills/ (21), agents/ (6),
                                     rotinas/ (conectoma, saneamento-vault, whatsapp-intake, ios, patches), README.md, empacotar.py
  03 - ESTEIRA/vigia-pdf-pecas/      o vigia de PDF do Mac: vigia_pdf.py, com.gfes.vigia-pdf-pecas.plist, INSTALAR-ESTEIRA.command, LEIA-ME.md
  (demais pastas)                    administrativo, financeiro, equipe, notas datadas — não são de caso
```
**O plugin `gfes` 1.4.0** (fonte única acima; pacotes em `~/Documents/Claude outputs/gfes-1.4.0.plugin`, 1.3.0 e 1.2.0 ao lado):
| | |
|---|---|
| **6 agentes** (`agents/*.md`) | `lourdes` (120 · Jurídico — a porta da banca e o radar de prazos; **todo trabalho jurídico é entregue por ela**), `teo` (40 · Engenharia do escritório: esteira, scripts, skills, plugin), `ciro` (40 · Engenharia do Residencial), `bia` (80 · marca da advocacia, Google Ads), `nina` (80 · captação do Residencial), `dora` (100 · conformidade da ILPI). Referência própria da Lourdes em `agents/references/`. |
| **21 skills** (`skills/*/SKILL.md`) | `assistente-juridico` (o MÉTODO e as MEDIDAS: `references/tipografia-vigente.json` é a fonte única das medidas; geradores em `assets/`, gates em `scripts/`, 30 referências), **`forma-da-peca`** (regra 35: o que vai onde — síntese com quadro + linha do tempo horizontal na primeira página; fatos da ficha ao eixo; ordem de leitura de 8 itens), `requisitos-das-pecas` (checklist legal + 10 modelos com o eixo), `direito-br`, `direito-civil-avancado` (64 códigos do Planalto em `references/codigos/`, enunciados do CJF), `recursos-e-tribunais`, `tjsc`, `eproc-tjsc`, `pje-trt12`, `execucao-penal`, `engenharia-de-sistemas`, `engenharia-de-ia`, `trafego-pago`, `google-ads`, `ilpi-conformidade`, `registro-assistencial-e-sistema`, `portaria`, `predio-unico`, `looping`, `whatsapp`, `mapa-da-casa`. |
| **3 geradores** (`assistente-juridico/assets/`) | `gerar_pdf.py` (peça forense, limpa), `gerar_pdf_relatorio.py` (parecer/relatório, timbrado), `gerar_contrato_pdf.py` (contrato, com logo). Markdown da casa → HTML → Chrome headless → PDF. Sem o Chrome do Mac: `GFES_CHROME=<caminho do chromium>`. Documento que emana da parte: `--emitente "NOME - CNPJ/CPF"`. |
| **8 gates** (`assistente-juridico/scripts/`) | tag crua · norma culta · ficha de fatos · admissibilidade (CONF-01..08 em `<peça>.conferencia.md`) · **prova visual** (`validar_prova_visual.py`, PV-01..09) · forense · diagramação (vão ≤ 20 %) · paginação (mede contra o JSON). Rodam sozinhos dentro dos geradores. PDF reprovado não se entrega; conserta-se a peça, nunca o gate. |
| **A marcação da casa** | `@@` centralizado · `#`/`##` títulos · `[quadro] Legenda` + tabela · janelas `> [!qualif]` `[!cita]` `[!tempo]` **`[!linha]`** `[!calc]` `[!dout]` `[!jur]` `[!poderes]` · marcos `~ DD/MM/AAAA \| evento (Ev. N)` e `~ !data` no marco decisivo · `[prova] img \| Legenda` · `[provapar] pag \| zoom \| Rótulo \| Legenda` · `@assinatura`. Tag HTML crua aborta o PDF. |
| **Ferramentas** | `scripts/etiqueta_prova.py` (etiqueta vermelha #9E2121 na prova), `scripts/recorte` e `paginas_pdf` (recorte e renderização), `scripts/extrair_texto_pdf.py`, `direito-br/scripts/calcular_prazo.py`, `eproc-tjsc/scripts/comunica.py` (DJEN, API pública). |
**Registros e memória da casa:** o vault é o cérebro (`00 - REGISTRO É NO VAULT (canônico).md` na raiz). Regras canônicas numeradas 1–35 (índice na PARTE 5 deste arquivo; texto integral em `skills/predio-unico/references/CLAUDE-md-INTEGRAL-2026-08-31.md`). Notas do dia em `00 - SEDE/03 - Auditorias e protocolos do escritório/REGISTRO-DO-DIA-2026-09-05 — ….md`. O curso Tipografia Jurídica, lido inteiro, em `~/Documents/Cursos-tipografia-juridica/` e espelhado em `<vault>/Tipografia Jurídica/`. Git local do vault em `~/Backups/vault-git` (commit automático às 20h; commite ao terminar).
**O que está desatualizado e você vai consertar (seção 3.3):** o `CLAUDE.md` e o `AGENTS.md` da **raiz do vault** (17/08 e 15/08/2026) ainda falam em "dois prédios", "declare o prédio", advogado "Rui", skill `dois-predias` e agente `vigia` — tudo revogado (prédio único 28/08; RADAR ÚNICO 04/09; raiz permanente 05/09). Eles são carregados como pais de `Advocacia/` e contradiriam esta montagem.
### 3. A montagem, nesta ordem
#### 3.1 Instalar o plugin `gfes` a partir da fonte única (persistente)
1. Grave `Advocacia/.claude-plugin/marketplace.json` com o conteúdo da **PARTE 4** (marketplace local `gfes-casa`, com `"source": "./02 - SKILLS E AGENTES"` — caminho relativo, que é a forma documentada).
2. Na sessão: `/plugin marketplace add "<caminho absoluto de Advocacia>"` e depois `/plugin install gfes@gfes-casa`. Confira com `/plugin` que o `gfes` 1.4.0 aparece, e com `/context` (ou `/agents`) que os agentes vêm como `gfes:lourdes`, `gfes:teo`, `gfes:ciro`, `gfes:bia`, `gfes:nina`, `gfes:dora`, e as skills como `/gfes:assistente-juridico`, `/gfes:forma-da-peca` etc.
3. Se o marketplace local não funcionar nesta versão do Claude Code, use o caminho documentado alternativo: `claude --plugin-dir "<caminho absoluto de 02 - SKILLS E AGENTES>"` (vale por sessão; ponha no alias da seção 3.6). Registre qual dos dois ficou.
4. Regra de atualização: editou a fonte → `/reload-plugins` (ou desinstale e reinstale) → e **sempre** suba a versão em `plugin.json` e gere o pacote com `python3 empacotar.py --saida "$HOME/Documents/Claude outputs"`, porque o app do Claude instala pelo `.plugin`. A `description` do `plugin.json` tem teto de **500 caracteres** no app; o `empacotar.py` já confere.
5. Confira que o plugin carregado é o da fonte: `grep -c '"linha": ("linha"' "<fonte>/skills/assistente-juridico/assets/gerar_pdf.py"` deve dar 1 (a janela `[!linha]` da regra 35).
#### 3.2 O `CLAUDE.md` do escritório e as permissões
1. Grave `Advocacia/CLAUDE.md` **exatamente** com o conteúdo da **PARTE 2**. Ele é o mínimo que vale em toda sessão aberta em `Advocacia/`; o resto mora nas skills e é lido de lá.
2. Grave `Advocacia/.claude/settings.json` com a **PARTE 3** (permissões: leitura e edição no vault e em `~/Documents`, `python3`, `git`, `open`, `brctl`, `launchctl` de leitura; negativas: `Residencial/**`, o `data.json` da API REST do Obsidian, `*.pfx`, `*.p12`). Se já existir um `settings.json` ali, faça backup e **mescle** — não sobrescreva permissões que o Gabriel tenha concedido.
3. Não grave nada em `~/.claude/CLAUDE.md` (perfil global) sem ordem: o escritório é projeto, não perfil.
#### 3.3 Atualizar os arquivos da raiz do vault que contradizem a casa
Com backup datado de cada um (`CLAUDE.md.bak-20260905-montagem`, `AGENTS.md.bak-20260905-montagem`):
- `CLAUDE.md` da raiz: **mantenha** o que é do vault e continua verdadeiro (nunca renomear/mover/apagar nota sem ordem; Git local em `~/Backups/vault-git` e o commit ao terminar; espelho no Google Drive; iCloud eviction e `brctl download`; `LC_ALL` no `pbcopy`; MCP `obsidian` em `http://127.0.0.1:27123/mcp` com o app aberto, disco com o app fechado; a chave do plugin REST é segredo; `iPhone` com P maiúsculo; frontmatter e datas absolutas; LOOPING; registrar no vault). **Retire** a "regra dos dois prédios", "declare o prédio", a skill `dois-predios` e o `@AGENTS.md`. **Acrescente** a tarja: prédio único e fio neural (28/08/2026, skill `predio-unico`), as três travas do cofre, RADAR ÚNICO (04/09/2026 — o agente `vigia` e a skill `vigia-de-prazos` foram extintos; o radar é a Sede e a dona é a Lourdes), e o ponteiro: "sessão do escritório abre em `Advocacia/` e lê `Advocacia/CLAUDE.md`; sessão do Residencial abre em `Residencial/`". Nada de reescrever a história: o que saiu ganha uma linha de "revogado em <data>, ver <nota>".
- `AGENTS.md` da raiz: reduza a um briefing de uma página coerente com o acima (quem é o Gabriel, as duas empresas, os seis agentes de hoje — Lourdes, Téo, Ciro, Bia, Nina, Dora —, onde cada coisa mora, as três travas, o ponteiro para o plugin `gfes` e para `Advocacia/CLAUDE.md`). O texto antigo (Windows, Rui, dois prédios) já está preservado em `_Sistema/`; confira e aponte.
- Varra `Advocacia/` e a raiz por resíduo que mande "chamar o vigia", "atravessar a rua", "contratação entre prédios", `~/Documents/casos/`, `~/.claude-gfdoes/skills/`, `<vault>/skills/`: **não corrija nota histórica**, só as vivas (LEIA-ME, índices, modelos, skills, agentes) — e liste as demais no relatório.
#### 3.4 A esteira de PDF (o vigia do Mac)
1. Leia `03 - ESTEIRA/vigia-pdf-pecas/LEIA-ME.md` e `INSTALAR-ESTEIRA.command`. O instalador confere o parque, instala o PyMuPDF se faltar, copia `com.gfes.vigia-pdf-pecas.plist` para `~/Library/LaunchAgents/` e carrega o agente. Rode-o (`zsh "…/INSTALAR-ESTEIRA.command"`) ou faça os mesmos passos à mão; confira o `.plist` (binário absoluto `/usr/bin/python3`, caminho da fonte única, `Label`), `launchctl list | grep vigia-pdf` e o log.
2. A primeira rodada não gera nada (grava a linha de base). Teste com a peça de teste da regra 35: copie `02 - SKILLS E AGENTES/skills/forma-da-peca/references/testes/teste-linha-sintese-7-marcos.md` **e** o `.conferencia.md` ao lado para uma pasta de teste com `.vigia` dentro (ou gere direto: `python3 "<fonte>/skills/assistente-juridico/assets/gerar_pdf.py" "<cópia>.md" --tipo generico`). O veredito esperado no Mac é **LIBERADO** com Times New Roman; na nuvem sairia Liberation Serif.
3. Se aparecer "Operation not permitted" num arquivo que existe, **não é bug**: é Acesso Total ao Disco para `/usr/bin/python3` e `/bin/zsh` (Ajustes → Privacidade e Segurança) — ato do Gabriel; pare e peça (seção 8).
#### 3.5 O WhatsApp da casa (rotina `whatsapp-intake`)
1. Leia `02 - SKILLS E AGENTES/rotinas/whatsapp-intake/README.md` e `skills/whatsapp/SKILL.md`. A arquitetura escolhida pelo Gabriel (30/08/2026) é Mac ligado, sem conta nova: `escutar.py` a cada 60 s lê **cópia** do `ChatStorage.sqlite` do WhatsApp Business, cada mensagem nova da conversa de comando vira `claude -p`, a resposta volta **só** àquela conversa (`enviar.py` recusa outro JID). Pelo WhatsApp o Claude lê, pesquisa, redige — **não envia a terceiro, não mexe em conta, não protocola**.
2. Confira o estado: `launchctl list | grep whatsapp-intake`, `config.json`, `estado/heartbeat`, `logs/escutar.log`. Se o laço estiver apontando para a antiga "pasta do radar" (extinta com o RADAR ÚNICO), **repare**: o `claude -p` deve rodar com `cwd` = `Advocacia/`, para herdar o `CLAUDE.md` novo e o plugin. Backup antes; teste com uma mensagem sua para você mesmo; **nenhuma mensagem sai sem ordem do Gabriel, uma a uma**.
3. Registre no relatório se o serviço estava ligado, e o que mudou.
#### 3.6 O atalho de abrir o escritório
Acrescente ao `~/.zshrc` (com backup) um alias — ajuste ao perfil/alias que a seção 1 revelou:
```
alias escritorio='cd "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia" && claude --add-dir "$HOME/Documents/Cursos-tipografia-juridica" --add-dir "$HOME/Documents/Claude outputs"'
```
Se o plugin só carregar por `--plugin-dir`, inclua `--plugin-dir "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/02 - SKILLS E AGENTES"` no alias. O modo de permissão é decisão do Gabriel (ele prefere trabalhar sem aprovação a cada passo — `--permission-mode acceptEdits` cobre edição e leitura; o que passa disso é ele quem liga).
#### 3.7 Testes de aceitação (todos devem passar antes do relatório)
```
cd "<fonte>"                                   # 02 - SKILLS E AGENTES
/usr/bin/python3 empacotar.py --verificar      # 21 skills, 6 agentes, plugin.json ≤ 500 car.
/usr/bin/python3 skills/assistente-juridico/scripts/validar_prova_visual.py --autoteste
# a peça de teste da regra 35, com o gerador da fonte, no Mac (Times):
cp skills/forma-da-peca/references/testes/teste-linha-sintese-7-marcos.* /tmp/t35/ && cd /tmp/t35 && /usr/bin/python3 "<fonte>/skills/assistente-juridico/assets/gerar_pdf.py" teste-linha-sintese-7-marcos.md --tipo generico
```
Esperado: gates aprovados, veredito **LIBERADO**, 2 páginas, e na primeira página a SÍNTESE com o quadro e a linha do tempo **horizontal, da esquerda para a direita, com seta**, 7 marcos em duas linhas, o marco `!` em vermelho. Renderize a p. 1 (`scripts/paginas_pdf` ou PyMuPDF) e **olhe** — medir não é ver. Depois, numa sessão limpa em `Advocacia/`: peça "@\"gfes:lourdes (agent)\" leia a ficha do caso X e diga qual é o próximo ato" e confira que ela abre o LEIA-ME, carrega `forma-da-peca` e responde em norma culta, sem bastidor. Não gere peça real nem toque em caso de cliente neste teste.
#### 3.8 Registro e commit
1. Nota nova em `Advocacia/00 - SEDE/03 - Auditorias e protocolos do escritório/REGISTRO-DO-DIA-<AAAA-MM-DD> — o ecossistema montado no Claude Code.md` (frontmatter `tipo: registro`, `criado`, `atualizado`, `tags`), com: o que foi ligado, os caminhos, as versões, os testes e seus resultados, o que ficou pendente do Gabriel, e links `[[...]]` para o LEIA-ME e para o registro de 05/09.
2. Acrescente ao `00 - SEDE/00 - LEIA-ME — como abrir o escritório.md` a seção "Abrir o escritório no Claude Code" (o alias, o marketplace, a esteira, o WhatsApp) e uma linha no histórico.
3. `git -C "<raiz do vault>" add -A && git commit -m "Montagem do ecossistema no Claude Code (<data>)"`.
### 4. O protocolo de toda sessão do escritório (o que você faz sempre que abrir em `Advocacia/`)
1. Ler `00 - SEDE/00 - LEIA-ME — como abrir o escritório.md`; abrir o `02 - RADAR DO ADVOGADO` e dizer, em uma linha, se há prazo correndo.
2. Assunto jurídico → **Lourdes** (`gfes:lourdes`): ela lê o processo inteiro (cláusula pétrea da análise integral), monta a ficha de fatos, apura o prazo na fonte e **entrega**. Sistema/automação → Téo; ILPI → Dora/Ciro/Nina (na pasta `Residencial/`, em outra sessão); marca da advocacia → Bia.
3. Antes de escrever ou regenerar peça, parecer ou memorial: **`/gfes:forma-da-peca`** e a ordem de leitura de 8 itens (regra 35); `tipografia-vigente.json` lido do arquivo, nunca da memória.
4. Peça nasce em `02-pecas/`, parecer em `03-parecer-e-analise/`, nome `<TIPO>-<processo curto>-<AAAA-MM-DD>.md`; a esteira gera o PDF; os 8 gates rodam; a vista página a página; **o PDF abre** (`open "<pdf>"` e `open "<pasta>"`). Entrega: conclusão, prazo e data-limite, órgão julgador, o que foi verificado e onde, a ficha de fatos com os VAZIOS visíveis, pendências, próximo ato do Gabriel.
5. Registro na `00 - CASO.md` (seção Registro) e, no fim do trabalho, `git commit` do vault.
6. WhatsApp: a casa lê e escreve; **o Gabriel envia**. eproc: consulta com o navegador logado por ele; credencial, assinatura e protocolo são atos dele. Sustentação oral: nunca de ofício. Nada que sai menciona IA.
### 5. O que você NÃO faz nesta montagem
Não instala Node, npm, Homebrew, MCP server por npm ou qualquer runtime novo. Não cria conta em serviço nenhum. Não altera `Residencial/`. Não mexe em `01-autos/` nem em `04-provas-e-comunicacoes/` de caso algum. Não edita skill, agente ou gerador (eles estão prontos; defeito achado vira pendência no relatório, para o Téo consertar na fonte e subir versão). Não apaga backups antigos. Não envia mensagem por WhatsApp, e-mail ou qualquer canal. Não "resume" a régua de memória: quando precisar de medida, abre o JSON.
### 6. Como pedir ajuda ao Gabriel (só isto)
Pare e pergunte apenas: (a) se for preciso conceder Acesso Total ao Disco ou outra permissão do macOS; (b) se o perfil do Claude Code em uso não for o que a seção 1 indica e houver dois candidatos; (c) se algum arquivo de configuração tiver sido alterado por outra sessão nos últimos minutos (regra 33). Tudo o mais, resolva e registre.
### 7. Ordem de execução resumida
1 reconhecer a máquina → 2 ler o LEIA-ME da Sede e o README da fonte → 3.1 plugin → 3.2 CLAUDE.md + settings → 3.3 raiz do vault → 3.4 esteira → 3.5 WhatsApp → 3.6 alias → 3.7 testes → 3.8 registro e commit → 8 relatório.
### 8. O relatório final (formato)
Numerado, curto, para ler no celular: (1) a máquina e o perfil do Claude Code em uso; (2) como o plugin ficou instalado (marketplace ou `--plugin-dir`) e a prova de que `gfes:lourdes` e `/gfes:forma-da-peca` aparecem; (3) os arquivos gravados e os backups feitos, com caminhos; (4) a esteira: instalada ou bloqueada por permissão; (5) o WhatsApp: estado e o que mudou; (6) os testes, um a um, com o veredito; (7) o que ficou pendente **do Gabriel**, um ato por linha; (8) pendências técnicas para o Téo (defeitos achados na fonte); (9) o link da nota de registro e o hash do commit.
FIM DO PROMPT
---
## PARTE 2 — `Advocacia/CLAUDE.md` (o Claude Code grava este conteúdo, integral)
```markdown
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
```
---
## PARTE 3 — `Advocacia/.claude/settings.json` (mesclar com o que já existir)
```json
{
  "permissions": {
    "allow": [
      "Read(//Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/**)",
      "Edit(//Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/**)",
      "Write(//Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia/**)",
      "Read(//Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Tipografia Jurídica/**)",
      "Read(//Users/gabriel/Documents/**)",
      "Edit(//Users/gabriel/Documents/Claude outputs/**)",
      "Write(//Users/gabriel/Documents/Claude outputs/**)",
      "Read(//tmp/**)",
      "Write(//tmp/**)",
      "Bash(ls:*)", "Bash(cat:*)", "Bash(head:*)", "Bash(tail:*)", "Bash(wc:*)", "Bash(grep:*)", "Bash(rg:*)",
      "Bash(find:*)", "Bash(cp:*)", "Bash(mkdir:*)", "Bash(mv:*)", "Bash(stat:*)", "Bash(diff:*)", "Bash(md5:*)",
      "Bash(python3:*)", "Bash(/usr/bin/python3:*)",
      "Bash(git status *)", "Bash(git log *)", "Bash(git diff *)", "Bash(git add *)", "Bash(git commit *)",
      "Bash(open:*)", "Bash(brctl download:*)", "Bash(launchctl list*)", "Bash(launchctl print*)",
      "Bash(zsh:*)", "Bash(sw_vers)", "Bash(uname:*)", "Bash(whoami)", "Bash(which:*)", "Bash(alias)",
      "Bash(pbcopy:*)", "Bash(pbpaste)", "Bash(defaults read:*)",
      "mcp__obsidian"
    ],
    "deny": [
      "Read(//Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Residencial/**)",
      "Read(//Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/.obsidian/plugins/obsidian-local-rest-api/data.json)",
      "Read(//Users/gabriel/Documents/**/*.pfx)",
      "Read(//Users/gabriel/Documents/**/*.p12)",
      "Read(//Users/gabriel/Documents/residencial-documentos/**)",
      "Read(//Users/gabriel/Documents/sistema-sagrada-familia/**)",
      "Bash(rm:*)", "Bash(rmdir:*)", "Bash(git push*)", "Bash(git reset --hard*)", "Bash(launchctl unload*)", "Bash(launchctl bootout*)"
    ]
  }
}
```
*(As negativas de `Residencial/`, `residencial-documentos/` e `sistema-sagrada-familia/` são a trava 2 do cofre aplicada à sessão do escritório; `.pfx`/`.p12` são o certificado — segredo do Gabriel; `rm` está negado porque a casa não apaga em definitivo. `launchctl load`/`bootstrap` para instalar a esteira pedem confirmação, como devem.)*
---
## PARTE 4 — `Advocacia/.claude-plugin/marketplace.json` (o marketplace local da casa)
```json
{
  "name": "gfes-casa",
  "owner": { "name": "Gabriel Fabrízio do Espírito Santo — OAB/SC 53.040" },
  "metadata": { "description": "A casa do Gabriel: o plugin gfes servido direto da fonte única do vault (Advocacia/02 - SKILLS E AGENTES)." },
  "plugins": [
    {
      "name": "gfes",
      "source": "./02 - SKILLS E AGENTES",
      "description": "Os seis agentes e as vinte e uma skills do escritório Espírito Santo Advocacia e do Residencial Sagrada Família, com os códigos do Planalto, os geradores de PDF e os oito gates.",
      "version": "1.4.0"
    }
  ]
}
```
Depois: `/plugin marketplace add "/Users/gabriel/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia"` → `/plugin install gfes@gfes-casa` → `/plugin` para conferir. Ao mudar a fonte: `/reload-plugins` (e suba a versão nos dois `json`).
---
## PARTE 5 — As regras canônicas da casa, em uma linha cada (índice para o Claude Code achar o texto)
Texto integral das 1–33: `02 - SKILLS E AGENTES/skills/predio-unico/references/CLAUDE-md-INTEGRAL-2026-08-31.md`; 34 e 35: `skills/assistente-juridico/references/prova-visual-automatica-2026-09-05.md` e `skills/forma-da-peca/SKILL.md`. Onde uma regra foi revogada, está dito.
| # | Data | A regra, em uma linha | Onde |
|---|---|---|---|
| 1–7 | 28/08 | **Prédio único e fio neural**: um prédio por andares (120 Jurídico · 100 Cuidado · 80 Marca · 40 Engenharia · 164 Cérebro Central); circulação livre; as três travas do cofre; registro no vault | `predio-unico` |
| 8 | 13/08 | **Looping**: nada fecha sem conferir contra o escopo | `looping` |
| 8b | 15/08 | **Assumir e resolver**: perguntar ao Gabriel é último recurso; pedir documento ao cliente é trabalho, não pergunta | `predio-unico` |
| 9 | 14/08 | **Especialidade TJSC**: os cinco atos (órgão, súmula, precedente, pesquisa filtrada, prazo/feriado) | `tjsc` |
| 10 | 14/08 | **Análise integral na entrada** (cláusula pétrea): lê-se tudo antes de qualquer parecer | `assistente-juridico` |
| 11 | 14/08 | **Especialidade recursal**: quem julga, quem admite, os dois prazos, o motivo de não conhecimento | `recursos-e-tribunais` |
| 12 | 15/08 | **Checklist legal da peça** antes, durante e antes de protocolar | `requisitos-das-pecas` |
| 13 | 16/08 | **O navegador é ferramenta da casa** (Chrome integrado; comando pelo terminal com a integração ligada) | `predio-unico` refs |
| 14 | 16/08 | **Tela de login não encerra trabalho**: deixa a aba e chama o Gabriel | idem |
| 15 | 19/08 | **Execução penal é especialidade** (LEP, restritivas, SEEU) | `execucao-penal` |
| 16 | 19/08 | **Regra do portador**: o bolso antes da pá; fato = valor + coordenada; VAZIO rebaixa; pior valor plausível | `assistente-juridico/references/regra-do-portador…` |
| 17 | 24/08 | **Sigilo defensivo**: do relato do cliente só o que beneficia; a defesa se constrói pelos autos | `…/regra-sigilo-defensivo…` |
| 18 | 24/08 | **Estudo por cópia integral + autonomia da banca** | `eproc-tjsc` |
| 19 | 24/08 | **Forense documental + zero rastro de IA** (metadados da casa; gate forense) | `scripts/forense_documento.py` |
| 20 | 25/08 | **Fonte da lei é o Planalto** — `grep` no arquivo do código, nunca memória | `direito-civil-avancado/references/codigos/` |
| 21 | 25/08 | **A porta da banca**: todo processo passa primeiro pela Lourdes | `agents/lourdes.md` |
| 22 | 25/08 | **Conhecimento com as horas + auditoria de honestidade** (formação da Lourdes) | `direito-civil-avancado` |
| 23 | 27/08 | **A Lourdes é sempre consultada** nas questões do escritório | cláusula pétrea, Sede |
| 24 | 27/08 | **A marca do advogado e a tipografia única** (Times 12, Charter 11, peça limpa) | `assistente-juridico` |
| 25 | 27/08 | **Nenhuma peça sai com órfã, viúva ou página em branco**; tipografia medida contra o JSON | `scripts/validar_paginacao.py` |
| 26 | 27/08 | **A prova se mostra e a peça se olha antes de sair** (etiqueta vermelha; a vista) | `…/prova-visual-e-conferencia…` |
| 27 | 27/08 | **Regra geral de formatação** — a constituição da forma; `tipografia-vigente.json` é a fonte única das medidas | `…/regra-geral-de-formatacao…` |
| 28 | 28/08 | ~~Agente vigia — campainha de prazo~~ **revogada em 04/09/2026 pelo RADAR ÚNICO** (o radar é a Sede; a dona é a Lourdes) | `00 - CLÁUSULA PÉTREA — RADAR ÚNICO` |
| 29 | 28/08 | **Peça não se corrige no processo** — corrige-se antes de peticionar (gate de admissibilidade, CONF-01..08) | `scripts/validar_admissibilidade.py` |
| 30 | 30/08 | **Citação só com fonte conferida** — vale para nota, alerta e conversa, não só para a peça | `…/trava-de-fonte-oficial…` |
| 31 | 31/08 | **O teste cobre o caminho que carrega o risco**, nunca só o recém-exercitado | `engenharia-de-ia/references/regra-31…` |
| 32 | 31/08 | **Parecer sai em PDF e a pasta abre** (`open`); entrega que só existe na resposta é perdida | `assistente-juridico` |
| 33 | 31/08 | **Uma sessão por vez sobre a configuração**, com backup datado; sessão ociosa se encerra; (e) 02/09: **abrir o PDF e a pasta na entrega, sem esperar que ele peça** | CLAUDE-md integral |
| — | 02/09 | **Assinatura de documento da parte** (ICP-Brasil ou papel assinado digitalizado; `--emitente` nos geradores) | `…/assinatura-de-documento-da-parte…` |
| — | 03/09 | **Documento que sai é do escritório, não da casa** (sem bastidor; gate `validar_saida_cliente.py`) · **parecer ao cliente em duas folhas, língua simples, logo GFES** · **WhatsApp na casa** (a casa escreve, o Gabriel envia) | `assistente-juridico`, `whatsapp` |
| — | 04/09 | **RADAR ÚNICO** · **cláusula constitucional da forma** (ler a régua antes de escrever) · **papel de relator** (consulta = relatório completo) | Sede |
| — | 05/09 | **Raiz permanente** (`Advocacia/` = escritório; fonte única = plugin) · **sustentação oral só a pedido** · **regra 34** prova visual automática · **regra 35** a forma da peça (SÍNTESE = quadro + `[!linha]` horizontal com seta; fatos da ficha ao eixo) | LEIA-ME da Sede, `forma-da-peca` |
---
## PARTE 6 — O que ficou construído até 05/09/2026 (o inventário que este prompt liga)
1. **Escritório permanente no vault** (05/09, manhã): 12 clientes, 18 casos e 996 arquivos migrados de `~/Documents/casos/` para `01 - CLIENTES/`, conferidos byte a byte; Sede com LEIA-ME, índice, radar-espelho, modelos e auditorias; esteira reescrita em `03 - ESTEIRA/`; fonte única em `02 - SKILLS E AGENTES/`; plugin 1.2.0.
2. **Curso Tipografia Jurídica lido por inteiro** (05/09, tarde): 16 páginas da plataforma, 1.953 comentários (976 respostas do professor → 348 regras com fonte), 3 docx de exemplos baixados com autorização; inventário "o que tem × o que falta"; tudo em `~/Documents/Cursos-tipografia-juridica/` e em `<vault>/Tipografia Jurídica/`.
3. **Regra 34 — prova visual automática** (05/09): gate `validar_prova_visual.py` (PV-01..09) embutido nos geradores; `etiqueta_prova.py`; referências `prova-visual-automatica…` e `perguntas-e-respostas-do-professor…`; plugin 1.3.0; contestação do David (5021012) e memorial do Yagho (5026537) regenerados sob a regra (PDFs definitivos em Times dependem da esteira).
4. **Regra 35 — a forma da peça** (05/09, noite): skill `forma-da-peca`; janela `[!linha]` nos três geradores; auditoria de 34 notas da régua com 17 conflitos resolvidos por tarja (o JSON vence em medida); modelos da Sede e de `requisitos-das-pecas` com o eixo na síntese; `00 - CASO` com a ficha de fatos em cinco colunas; plugin **1.4.0** (`description` ≤ 500 caracteres; `empacotar.py` confere).
5. **Pendente do Gabriel** (atos dele): instalar o `gfes-1.4.0.plugin` no app; esteira (Acesso Total ao Disco); esvaziar `~/Documents/_to_delete/` e `<vault>/.trash/`; descartar os `.com.google.Chrome.*` de `~/Downloads`; salvar o cartão da skill de conta `escritorio-gfes`.
6. **Pendências de engenharia** (Téo): `validar_diagramacao.py` lendo as margens do JSON; margens de parecer e contrato no JSON; `VAZIO` barrado no PDF de peça; peças antigas do David (5001554, 5013466) com `provas/*.png` inexistentes — regenerar sob ordem.
