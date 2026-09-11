#!/usr/bin/env bash
# Instala no Mac o ADENDO de 02/09/2026 (adoção dos 14 itens) e as correções do acervo.
# Copia com BACKUP DATADO; não apaga nada. Uso:  bash instalar.sh [--dry-run]
set -euo pipefail
AQUI="$(cd "$(dirname "$0")" && pwd)"
SKILLS="${GFES_SKILLS:-$HOME/.claude-gfdoes/skills}"
VAULT="${GFES_VAULT:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone}"
DRY="${1:-}"
STAMP="pre-adendo-20260902"
copiar() { # copiar ORIGEM DESTINO
  local o="$1" d="$2"
  if [[ "$DRY" == "--dry-run" ]]; then echo "[dry] $o -> $d"; return; fi
  mkdir -p "$(dirname "$d")"
  if [[ -f "$d" ]] && ! cmp -s "$o" "$d"; then
    local b="${d%.*}_${STAMP}.${d##*.}.bak"; cp -p "$d" "$b"; echo "backup  $b"
  fi
  cp "$o" "$d"; echo "gravado $d"
}
[[ -d "$SKILLS/assistente-juridico" ]] || { echo "skills não encontradas em $SKILLS (defina GFES_SKILLS)"; exit 2; }
[[ -d "$VAULT" ]] || { echo "vault não encontrado em $VAULT (defina GFES_VAULT)"; exit 2; }
cd "$AQUI/skills"
find . -type f | while read -r f; do copiar "$f" "$SKILLS/${f#./}"; done
cd "$AQUI/vault"
find . -type f | while read -r f; do copiar "$f" "$VAULT/${f#./}"; done
echo
echo "Pronto. Próximos passos: (1) gerar um PDF de teste:"
echo "   python3 \"$SKILLS/assistente-juridico/assets/gerar_pdf.py\" \"$AQUI/fixtures/peca/peca-teste.md\" --tipo generico"
echo "(2) renderizar e OLHAR página a página (regra 26); (3) atualizar os dez modelos com [!requerimentos] e o quadro de tutela."
