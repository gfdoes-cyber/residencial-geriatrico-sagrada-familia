#!/bin/bash
# Casa GFES — abre o Claude com mãos na máquina e deixa a sessão disponível
# no app (claude.ai/code e celular). Duplo clique no Finder ou execute no Terminal.
# Requisitos: claude instalado e logado via /login (plano Pro/Max), sem API key.
#
# Desde 05/09/2026 a sessão abre na raiz permanente do escritório (Advocacia/, no vault) e
# herda Advocacia/CLAUDE.md, o settings.json do projeto e o plugin gfes instalado no perfil.
# O modo servidor (claude remote-control) só aceita as flags documentadas em
# https://code.claude.com/docs/en/remote-control — não aceita --add-dir nem --plugin-dir.
# Pasta extra entra por permissions.additionalDirectories no settings do projeto.
# Se o perfil da casa for outro (CLAUDE_CONFIG_DIR), exporte-o no ~/.zshrc: este script
# respeita o que já estiver no ambiente e não escolhe perfil sozinho.
ESCRITORIO="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/iPhone/Advocacia"
if [ -d "$ESCRITORIO" ]; then
  cd "$ESCRITORIO" || exit 1
else
  echo "Raiz permanente não encontrada: $ESCRITORIO — abrindo em ~/.claude-gfdoes." >&2
  cd "$HOME/.claude-gfdoes" 2>/dev/null || cd "$HOME"
fi
echo "Casa GFES — Remote Control em: $(pwd)"
echo "Pressione espaço para o QR code; Ctrl+C encerra (retomável por cerca de 4 h com --continue)."
exec claude remote-control --name "Escritório GFES" --permission-mode acceptEdits
