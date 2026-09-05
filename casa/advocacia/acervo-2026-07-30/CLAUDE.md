# GFES — Base de Trabalho (Gabriel Fabrízio do Espírito Santo)

Este repositório é a base permanente das sessões Claude Code na nuvem do Gabriel
(advocacia + ILPI). Leia este arquivo antes de qualquer tarefa.

## Identidade tríplice (cláusula pétrea — NUNCA misturar)

| Vetor | Identidade | Uso |
|---|---|---|
| **Gabriel-PF** | CPF 544.074.601-30 | IRPF, AJG, causa própria (5007704) |
| **PJ-Advocacia** | ESPIRITO SANTO Sociedade Individual de Advocacia · CNPJ 50.411.747/0001-00 · OAB/SC 53.040 | peças judiciais, pareceres, site GFES Advocacia (Direito Digital) |
| **PJ-Antunelli** | Antunelli & Antunelli Instituição de Idosos Ltda. · CNPJ 02.145.891/0001-08 · NIRE 42206612731 | Residencial Geriátrico Sagrada Família (ILPI) — documentos assinados pelo ADMINISTRADOR, **sem menção à OAB** |

Endereço ILPI: Rua Vergilino Domingos da Silva, 1003 — Serraria, São José/SC, CEP 88115-170.
Fones: (48) 98880-7020 · (48) 98421-6664 · (48) 98819-8788. E-mails: gfdoes@gmail.com (pessoal/adv) · residencialsgfinanceiro@gmail.com (ILPI).

## Regras da casa (vinculantes em toda tarefa)

1. **Antialucinação:** nenhuma lei/súmula/precedente entra sem leitura na fonte oficial NA sessão, com URL + data. Rotular tudo: [VERIFICADO] / [INFERÊNCIA] / [NÃO VERIFICADO]. Nunca inventar dados cadastrais — campo desconhecido sai como [PREENCHER].
2. **Prazo sempre calculado programaticamente** (usar `.claude/skills/assistente-juridico/scripts/calcular_prazo.py`).
3. **Leitura integral:** autos e documentos lidos palavra por palavra, em ordem cronológica.
4. **NUNCA aplicar assinatura estilizada/simulada** em documento algum (regra permanente de 13/07/2026). Campo de assinatura sai em branco (punho) ou vai pelo DocuSeal.
5. **Súmula só entra com redação conferida no portal oficial NA DATA da peça.** Exemplo-padrão: Súmula 545/STJ foi REVISADA em 10/09/2025 (Tema 1194) — nunca citar redação antiga.
6. Correção apontada pelo Gabriel vira **regra permanente** registrada aqui e no vault (regra do refino, 27/05).
7. Documentos PDF: gerar via HTML + Chromium headless (`/opt/pw-browsers/chromium --headless --no-sandbox --print-to-pdf=...`), entregar pelo chat (SendUserFile) e/ou Drive. Modelos prontos em `templates/`.

## Ambiente na nuvem — limites conhecidos

- `~/.claude/skills/` do PC local NÃO existe aqui; as skills desta base ficam em `.claude/skills/` do repositório (carregam sozinhas).
- Rede: domínios `.jus.br` (eproc, DJEN/comunicaapi, tjsc) **bloqueados pela política do ambiente** — pedir ao Gabriel para liberar em claude.ai/code → environment → network policy, ou executar na sessão local.
- Processos sigilosos/pessoais: só na sessão local com eproc logado. Nunca pedir senha/2FA.
- Disco é efêmero: tudo que importa vai para o chat, Drive ou commit+push neste repositório.
- Conectores ativos na conta: Google Drive (vault GFES), Gmail (gfdoes), Calendar, Notion, DocuSeal (assinaturas — template de comunicado id 4966011).

## Fontes canônicas

- Página Notion "⚖️ Skills Jurídicas GFES — Auditoria e Base Técnica Verificada" (13/07/2026): https://app.notion.com/p/39cc0f7ec68481509dcdd56a0128acd9
- Fontes oficiais e portais: `.claude/skills/assistente-juridico/references/fontes-oficiais.md`
- Vault do escritório: Google Drive (buscar via conector; fichas de residentes, financeiro, contratados).
