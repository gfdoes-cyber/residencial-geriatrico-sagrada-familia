#!/bin/bash
# Casa GFES — abre o Claude com mãos na máquina e deixa a sessão disponível
# no app (claude.ai/code e celular). Duplo clique no Finder ou execute no Terminal.
# Requisitos: claude instalado e logado via /login (plano Pro/Max), sem API key.
cd "$HOME/.claude-gfdoes" 2>/dev/null || cd "$HOME"
echo "Casa GFES — Remote Control. Pressione espaço para o QR code; Ctrl+C encerra."
exec claude remote-control
