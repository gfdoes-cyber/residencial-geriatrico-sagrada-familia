# ACP 0900193-90.2016.8.24.0064 — cumprimento do despacho do Ev. 25 (02/09/2026)

Apelação Cível no TJSC — 2ª Câmara de Direito Público — Gab. 03 — Des. Carlos Adilson Silva.
Prazo do Ev. 25/27: **04/09/2026, 23h59min59s**.

## Conteúdo

| Pasta/arquivo | O que é |
|---|---|
| `auditoria/RELATORIO-AUDITORIA.{md,docx,pdf}` | Auditoria ponta a ponta: estado do processo, auditoria da guia paga, representação, cadastro, caminho processual, riscos e pendências |
| `auditoria/CHECKLIST-PROTOCOLO.{md,docx,pdf}` | Passo a passo do protocolo no eproc 2º grau e o que conferir antes |
| `pecas/01-peticao-cumprimento-ev25.{md,docx,pdf}` | Peça principal: preparo recolhido, desistência da gratuidade, representação |
| `pecas/02-procuracao-ad-judicia.{md,docx,pdf}` | Procuração da Antunelli ao advogado, com cláusula de ratificação (Doc. 2) |
| `pecas/03-regularizacao-cadastro-intimacao-exclusiva.{md,docx,pdf}` | Petição separada: baixa das renunciantes, intimação exclusiva, razão social |
| `fontes/DOSSIE-0900193.md` | Dossiê de fatos com coordenadas (eventos, datas, documentos) usado na auditoria e nas peças |
| `fontes/laudos/*.json` | Laudos das auditorias e da verificação adversarial (agentes independentes) |

## Ordem de protocolo

1. Conferir a aba "Custas" (guia do Ev. 31 paga/baixada) e o teor do Ev. 25.
2. Assinar a procuração **pela Antunelli** (e-CNPJ ou punho digitalizado).
3. Protocolar a peça 01 com os Docs. 1 a 4, respondendo à intimação do Ev. 27.
4. Protocolar a peça 03 (sem prazo), referindo os Docs. 2 e 3.

## Como regenerar DOCX/PDF a partir do markdown

Os `.md` são a fonte. O DOCX é gerado com `docx` (npm) e o PDF com Chromium headless (Playwright); ver `tools/` na raiz do repositório.

```bash
node tools/gen_docx.js pecas/01-peticao-cumprimento-ev25.md pecas/01-peticao-cumprimento-ev25.docx
node tools/md2pdf.js  pecas/01-peticao-cumprimento-ev25.md pecas/01-peticao-cumprimento-ev25.pdf
```
