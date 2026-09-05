---
name: documentos-ilpi
description: Gerar documentos padronizados do Residencial Geriátrico Sagrada Família (recibo de mensalidade, comunicado interno, kit de sindicância, termo de desligamento/entrega de residente, rescisão de prestador, ofício de prontuários). Usar sempre que o Gabriel pedir um documento da ILPI/Antunelli.
---

# Documentos padronizados — ILPI Sagrada Família

## Fluxo

1. Escolher o modelo em `templates/` (HTML com papel timbrado da Antunelli).
2. Buscar os dados reais no vault do Drive (ficha do residente, balancete,
   relação de colaboradores). **Nunca inventar** nome, CPF, valor ou data —
   campo sem fonte sai como linha em branco ou [PREENCHER].
3. Editar o HTML (copiar para o scratchpad), gerar PDF:
   `/opt/pw-browsers/chromium --headless --no-sandbox --disable-gpu --print-to-pdf="NOME.pdf" --no-pdf-header-footer arquivo.html`
4. Conferir o PDF visualmente (Read) antes de entregar via SendUserFile.

## Regras específicas

- Assinatura: **linha em branco** (punho) ou DocuSeal. NUNCA assinatura
  estilizada/simulada (regra permanente 13/07/2026).
- Emissor: Antunelli & Antunelli Instituição de Idosos Ltda., CNPJ
  02.145.891/0001-08 — assinado pelo administrador, **sem OAB**.
- Recibo de mensalidade: espelhar `templates/recibo-mensalidade.html`;
  valor confirmado em pelo menos 2 fontes do vault (ficha + balancete).
- Medicamentos controlados em termos de entrega: sempre com quantidades,
  lote e assinatura específica.
- Numeração de comunicados internos: conferir o último número usado
  (Comunicado nº 01/2026 foi o da apuração BO-00708, 13/07/2026).

## Dados fixos

Endereço: Rua Vergilino Domingos da Silva, 1003 — Serraria, São José/SC,
CEP 88115-170. Fones: (48) 98880-7020 · (48) 98421-6664 · (48) 98819-8788.
Administrador/representante legal: Gabriel Fabrízio do Espírito Santo.
Assistente social: Lucia Regina Presa Madruga — CRESS/SC 010721.
