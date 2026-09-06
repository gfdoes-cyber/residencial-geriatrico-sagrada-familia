// Markdown-subset -> HTML -> PDF (Chromium headless). Uso: node md2pdf.js entrada.md saida.pdf [saida.html]
const fs = require('fs');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, inFile, outPdf, outHtml] = process.argv;
const src = fs.readFileSync(inFile, 'utf8').replace(/\r\n/g, '\n');
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const inline = s => esc(s)
  .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>')
  .replace(/__([^_]+)__/g, '<u>$1</u>')
  .replace(/\*([^*]+)\*/g, '<i>$1</i>');
const lines = src.split('\n');
let html = [], para = [], i = 0;
const flush = () => { if (para.length) { const t = para.join(' ').replace(/\s+/g, ' ').trim(); if (t) html.push(`<p>${inline(t)}</p>`); para = []; } };
while (i < lines.length) {
  const line = lines[i].replace(/\s+$/, '');
  if (!line.trim()) { flush(); i++; continue; }
  if (line.trim() === '\\pagebreak' || line.trim() === '<<<QUEBRA>>>') { flush(); html.push('<div class="pb"></div>'); i++; continue; }
  if (/^---+$/.test(line.trim())) { flush(); html.push('<hr>'); i++; continue; }
  if (line.startsWith('@@ ')) {
    flush(); const grp = [];
    while (i < lines.length && (lines[i].startsWith('@@ ') || (lines[i].trim() === '' && i + 1 < lines.length && lines[i + 1].startsWith('@@ ')))) { if (lines[i].startsWith('@@ ')) grp.push(`<p class="c">${inline(lines[i].slice(3))}</p>`); i++; }
    html.push(`<div class="keep">${grp.join('')}</div>`); continue;
  }
  if (line.startsWith('# ')) { flush(); html.push(`<h1>${inline(line.slice(2))}</h1>`); i++; continue; }
  if (line.startsWith('## ')) { flush(); html.push(`<h2>${inline(line.slice(3))}</h2>`); i++; continue; }
  if (line.startsWith('### ')) { flush(); html.push(`<h3>${inline(line.slice(4))}</h3>`); i++; continue; }
  if (line.startsWith('>')) { flush(); const q = []; while (i < lines.length && lines[i].startsWith('>')) { q.push(lines[i].replace(/^>\s?/, '')); i++; } html.push(`<blockquote>${inline(q.join(' ').replace(/\s+/g, ' ').trim())}</blockquote>`); continue; }
  if (/^\s*[-•]\s+/.test(line)) { flush(); html.push('<ul>'); while (i < lines.length && /^\s*[-•]\s+/.test(lines[i])) { html.push(`<li>${inline(lines[i].replace(/^\s*[-•]\s+/, ''))}</li>`); i++; } html.push('</ul>'); continue; }
  if (/^\s*\|.*\|\s*$/.test(line)) {
    flush(); const rows = [];
    while (i < lines.length && /^\s*\|.*\|\s*$/.test(lines[i])) { if (!/^\s*\|?\s*:?-{2,}/.test(lines[i])) rows.push(lines[i].trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim())); i++; }
    html.push('<table>' + rows.map((r, ri) => '<tr>' + r.map(c => ri === 0 ? `<th>${inline(c)}</th>` : `<td>${inline(c)}</td>`).join('') + '</tr>').join('') + '</table>');
    continue;
  }
  para.push(line.trim()); i++;
}
flush();
const css = `
@page { size: A4; margin: 3cm 2cm 2.5cm 3cm; }
body { font-family: "Times New Roman", "Liberation Serif", Times, serif; font-size: 12pt; line-height: 1.5; color: #000; text-align: justify; hyphens: auto; -webkit-hyphens: auto; lang: pt-BR; }
p { margin: 0 0 6pt 0; text-indent: 1.25cm; orphans: 2; widows: 2; }
p.c { text-align: center; text-indent: 0; hyphens: none; -webkit-hyphens: none; }
h1 { font-size: 12pt; text-align: center; text-transform: uppercase; margin: 12pt 0 12pt 0; font-weight: bold; }
h2 { font-size: 12pt; margin: 18pt 0 9pt 0; font-weight: bold; page-break-after: avoid; break-after: avoid; }
h3 { font-size: 12pt; margin: 12pt 0 6pt 0; font-weight: bold; font-style: italic; page-break-after: avoid; }
blockquote { margin: 0 0 10pt 4cm; font-size: 11pt; line-height: 1.15; text-align: justify; }
ul { margin: 0 0 6pt 1.25cm; padding: 0; } li { margin: 0 0 4pt 0; list-style: "– "; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; line-height: 1.2; margin: 6pt 0 10pt 0; page-break-inside: auto; }
th, td { border: 1px solid #999; padding: 3pt 5pt; vertical-align: top; text-align: left; } th { background: #ededed; }
hr { border: 0; border-top: 1px solid #000; margin: 8pt 0; }
.pb { page-break-after: always; break-after: page; }
.keep { page-break-inside: avoid; break-inside: avoid; }
`;
const doc = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${css}</style></head><body>${html.join('\n')}</body></html>`;
if (outHtml) fs.writeFileSync(outHtml, doc);
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setContent(doc, { waitUntil: 'load' });
  await page.pdf({ path: outPdf, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;font-family:\'Times New Roman\',serif;font-size:9pt;text-align:right;padding-right:2cm;color:#000;"><span class="pageNumber"></span></div>' });
  await browser.close();
  console.log('PDF OK', outPdf);
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
