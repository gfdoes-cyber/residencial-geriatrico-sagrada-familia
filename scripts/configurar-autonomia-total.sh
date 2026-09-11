#!/bin/bash
# Casa GFES — autonomia total do Claude Code neste Mac.
# Faz: backup + merge em ~/.claude/settings.json · alias no ~/.zshrc ·
#      diagnóstico real das 4 permissões do macOS · claude doctor · relatório.
#
# RODE ESTE SCRIPT NO MESMO APLICATIVO DE TERMINAL EM QUE VOCÊ USA O 'claude'.
# O diagnóstico de permissão mede o TCC do terminal que executa — medir no
# Terminal.app e usar o claude no iTerm dá resposta errada. Por isso: não
# abra com duplo clique; abra o seu terminal e cole o comando.
#
# Não usa sudo, não usa tccutil, não toca em SIP nem em ajuste de segurança.

set -uo pipefail

if [ "$(uname -s)" != "Darwin" ]; then
  echo "ERRO: este script é do macOS e esta máquina é $(uname -s). Nada foi alterado." >&2
  exit 1
fi

PY="$(command -v python3 || true)"
if [ -z "$PY" ]; then
  echo "ERRO: python3 não encontrado. Instale com: xcode-select --install" >&2
  exit 1
fi

CFG="$HOME/.claude/settings.json"
CARIMBO="$(date +%Y%m%d-%H%M%S)"
BACKUP="$HOME/.claude/settings.json.backup-$CARIMBO"
mkdir -p "$HOME/.claude"

# ─────────────────────────── 1. backup ───────────────────────────
if [ -f "$CFG" ]; then
  cp -p "$CFG" "$BACKUP" || { echo "ERRO: falhou o backup. Nada foi alterado." >&2; exit 1; }
  BACKUP_FEITO="$BACKUP"
else
  BACKUP_FEITO="(não havia settings.json — nada a salvar)"
fi

# ──────────────────── 2. merge preservando o que existe ────────────────────
SAIDA_MERGE="$("$PY" - "$CFG" <<'FIM_PYTHON'
import json, os, sys

caminho = sys.argv[1]
home = os.path.expanduser("~")

ALLOW = ["Bash", "Read", "Edit", "Write", "WebFetch", "WebSearch"]
DIRS  = ["/", home]
ASK = [
    "Bash(sudo *)", "Bash(sh)", "Bash(bash)", "Bash(dd *)", "Bash(diskutil *)",
    "Bash(csrutil *)", "Bash(spctl *)", "Bash(shutdown *)", "Bash(reboot *)",
    "Bash(killall *)", "Bash(chown -R *)", "Bash(chmod -R *)",
    "Bash(git push --force *)", "Bash(git push -f *)", "Bash(git push * --force*)",
    "Bash(git reset --hard *)", "Bash(defaults delete *)", "Bash(launchctl *)",
    "Bash(brew uninstall *)", "Bash(npm publish *)",
]
DENY = [
    "Read(~/.ssh/**)", "Read(~/.gnupg/**)", "Read(~/.aws/**)",
    "Read(~/.config/gcloud/**)", "Read(~/Library/Keychains/**)",
    "Read(~/.claude/.credentials.json)",
    "Edit(~/.ssh/**)", "Edit(~/.gnupg/**)", "Edit(~/Library/Keychains/**)",
    "Bash(security dump-keychain *)", "Bash(security find-generic-password *)",
    "Bash(security find-internet-password *)",
    "Bash(rm -rf /)", "Bash(rm -rf /*)", "Bash(rm -rf ~)", "Bash(rm -rf ~/*)",
    "Bash(sudo rm *)",
]

existia = os.path.exists(caminho)
dados = {}
if existia:
    bruto = open(caminho, encoding="utf-8").read().strip()
    if bruto:
        try:
            dados = json.loads(bruto)
        except json.JSONDecodeError as e:
            print("ABORTOU=json inválido no settings.json atual: %s" % e)
            sys.exit(3)
if not isinstance(dados, dict):
    print("ABORTOU=settings.json atual não é um objeto JSON")
    sys.exit(3)

perms = dados.get("permissions")
if not isinstance(perms, dict):
    perms = {}

def uniao(atual, novos):
    saida, vistos = [], set()
    base = atual if isinstance(atual, list) else []
    for v in list(base) + novos:
        if isinstance(v, str) and v not in vistos:
            vistos.add(v); saida.append(v)
    return saida

modo_antes = perms.get("defaultMode", "(não definido)")
perms["defaultMode"] = "bypassPermissions"
perms["additionalDirectories"] = uniao(perms.get("additionalDirectories"), DIRS)
perms["allow"] = uniao(perms.get("allow"), ALLOW)
perms["ask"]   = uniao(perms.get("ask"),   ASK)
perms["deny"]  = uniao(perms.get("deny"),  DENY)
removeu = perms.pop("disableBypassPermissionsMode", None) is not None

dados["permissions"] = perms

tmp = caminho + ".tmp"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)
    f.write("\n")
os.replace(tmp, caminho)

preservadas = sorted(k for k in dados if k != "permissions")
print("EXISTIA=%s" % ("sim" if existia else "nao"))
print("MODO_ANTES=%s" % modo_antes)
print("PRESERVADAS=%s" % (", ".join(preservadas) if preservadas else "(nenhuma outra chave)"))
print("NALLOW=%d" % len(perms["allow"]))
print("NASK=%d"   % len(perms["ask"]))
print("NDENY=%d"  % len(perms["deny"]))
print("REMOVEU_DISABLE=%s" % ("sim" if removeu else "nao"))
FIM_PYTHON
)"
COD_MERGE=$?

if [ $COD_MERGE -ne 0 ]; then
  echo "ERRO no merge — settings.json NÃO foi alterado:" >&2
  echo "$SAIDA_MERGE" >&2
  exit 1
fi
eval "$(echo "$SAIDA_MERGE" | sed 's/^\([A-Z_]*\)=\(.*\)$/\1="\2"/')"

# ─────────────────────── 3. alias no ~/.zshrc ───────────────────────
LINHA_ALIAS="alias claude-cauteloso='claude --permission-mode default'"
if [ -f "$HOME/.zshrc" ] && grep -qF "claude-cauteloso" "$HOME/.zshrc"; then
  ALIAS_ST="já existia — não duplicado"
else
  printf '\n# Casa GFES — volta ao modo que pergunta antes de agir\n%s\n' "$LINHA_ALIAS" >> "$HOME/.zshrc"
  ALIAS_ST="acrescentado"
fi

# ─────────────── 4. diagnóstico real das permissões do macOS ───────────────
APP_TERMINAL="${TERM_PROGRAM:-desconhecido}"

testar() { if out="$("$@" 2>&1)"; then echo "OK"; else
    case "$out" in *"not permitted"*|*"Operation not permitted"*|*"-1743"*|*"not authorized"*|*"1743"*) echo "FALTA";; *) echo "FALHOU: $(echo "$out" | head -1)";; esac
  fi; }

DISCO_DOCS="$(testar ls "$HOME/Documents")"
DISCO_OUTR="$(testar ls "$HOME/Desktop" "$HOME/Downloads")"
AUTOMACAO="$(testar osascript -e 'tell app "Finder" to get name')"
rm -f /tmp/gfes-tela.png 2>/dev/null
TELA="$(testar screencapture -x /tmp/gfes-tela.png)"
if [ "$TELA" = "OK" ] && [ ! -s /tmp/gfes-tela.png ]; then TELA="FALTA"; fi
rm -f /tmp/gfes-tela.png 2>/dev/null

if [ "$DISCO_DOCS" = "OK" ] && [ "$DISCO_OUTR" = "OK" ]; then DISCO="OK"; else DISCO="FALTA"; fi

# ───────────────────────── 5. claude doctor ─────────────────────────
DOCTOR_OUT="$HOME/.claude/doctor-$CARIMBO.txt"
if command -v claude >/dev/null 2>&1; then
  claude doctor </dev/null >"$DOCTOR_OUT" 2>&1 &
  pid=$!; i=0
  while kill -0 "$pid" 2>/dev/null && [ $i -lt 60 ]; do sleep 1; i=$((i+1)); done
  if kill -0 "$pid" 2>/dev/null; then kill -TERM "$pid" 2>/dev/null; DOCTOR="não terminou em 60s — rode 'claude doctor' à mão"; else
    wait "$pid" 2>/dev/null
    if grep -qiE "invalid|inválid|error|erro" "$DOCTOR_OUT"; then
      DOCTOR="ACUSOU ALGO — veja $DOCTOR_OUT"
    else
      DOCTOR="limpo (saída em $DOCTOR_OUT)"
    fi
  fi
else
  DOCTOR="comando 'claude' não encontrado no PATH"
fi

# ───────────────────────── 6. relatório ─────────────────────────
cat <<FIM_RELATORIO

════════════════ RELATÓRIO — autonomia total ════════════════

1. BACKUP
   $BACKUP_FEITO

2. SETTINGS.JSON  ($CFG)
   arquivo já existia ......... $EXISTIA
   defaultMode antes .......... $MODO_ANTES   →  agora: bypassPermissions
   chaves preservadas ......... $PRESERVADAS
   disableBypassPermissionsMode removido: $REMOVEU_DISABLE

3. REGRAS VALENDO
   deny .... $NDENY   (bloqueiam em TODOS os modos, inclusive bypass)
   ask ..... $NASK    (continuam parando para perguntar)
   allow ... $NALLOW  (sem efeito no bypass; servem no modo cauteloso)

4. PERMISSÕES DO macOS — teste real, feito de dentro de: $APP_TERMINAL
   Acesso Total ao Disco ...... $DISCO
     ~/Documents .............. $DISCO_DOCS
     ~/Desktop e ~/Downloads .. $DISCO_OUTR
   Automação (Finder) ......... $AUTOMACAO
   Gravação de Tela ........... $TELA

5. ALIAS DE VOLTA
   claude-cauteloso ........... $ALIAS_ST  (vale no próximo terminal, ou: source ~/.zshrc)

6. CLAUDE DOCTOR
   $DOCTOR

FIM_RELATORIO

# abre só o painel do que faltou — é clique seu, não meu
FALTOU=0
if [ "$DISCO" != "OK" ]; then
  echo "→ falta Acesso Total ao Disco para $APP_TERMINAL. Abrindo o painel…"
  open "x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles"; FALTOU=1; sleep 1
fi
if [ "$AUTOMACAO" != "OK" ]; then
  echo "→ falta Automação para $APP_TERMINAL. Comando do painel:"
  echo '  open "x-apple.systempreferences:com.apple.preference.security?Privacy_Automation"'; FALTOU=1
fi
if [ "$TELA" != "OK" ]; then
  echo "→ falta Gravação de Tela para $APP_TERMINAL. Comando do painel:"
  echo '  open "x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture"'; FALTOU=1
fi
[ $FALTOU -eq 1 ] && cat <<'FIM_AVISO'

   Nos painéis, o que você marca é o SEU APLICATIVO DE TERMINAL, não o "claude".
   Depois de marcar, FECHE E ABRA o terminal — o macOS só aplica em processo novo.
FIM_AVISO

cat <<'FIM_LEMBRETE'

LEMBRE-SE:
  • O modo novo só vale na PRÓXIMA sessão — saia do claude e abra 'claude' de novo.
  • Na primeira vez ele mostra um aviso de responsabilidade que você tem de aceitar; aparece uma vez só.

FIM_LEMBRETE
