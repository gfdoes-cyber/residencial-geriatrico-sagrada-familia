#!/usr/bin/env bash
# Uso: tools/build.sh entrada.md pasta_saida  -> gera .docx, .pdf e PNGs de conferência
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
IN="$1"; OUT="$2"; mkdir -p "$OUT"
BASE="$(basename "${IN%.md}")"
node "$HERE/gen_docx.js" "$IN" "$OUT/$BASE.docx"
node "$HERE/md2pdf.js" "$IN" "$OUT/$BASE.pdf"
python3 - "$OUT/$BASE.pdf" "$OUT/$BASE" <<'PY'
import sys, pymupdf
pdf, prefix = sys.argv[1], sys.argv[2]
d = pymupdf.open(pdf)
print('paginas:', d.page_count)
for n, p in enumerate(d, 1):
    p.get_pixmap(dpi=60).save(f"{prefix}-p{n:02d}.png")
PY
