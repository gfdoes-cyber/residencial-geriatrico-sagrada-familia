# tools — geração de DOCX e PDF a partir de markdown

- `gen_docx.js entrada.md saida.docx` — DOCX A4, Times New Roman 12, entrelinhas 1,5, margens 3/2/3/2 cm (requer `npm install docx`).
- `md2pdf.js entrada.md saida.pdf` — PDF via Chromium headless (Playwright), mesma tipografia.
- `build.sh entrada.md pasta_saida` — gera ambos e PNGs de conferência (requer `pip install pymupdf`).

Sintaxe do markdown aceito: `@@ ` linha centralizada; `# ` título; `## ` capítulo; `> ` transcrição recuada; `- ` lista; `| a | b |` tabela; `**negrito**`, `*itálico*`, `__sublinhado__`; `\pagebreak`.
