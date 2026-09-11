// Markdown-subset -> DOCX (A4, Times New Roman 12, 1,5 entrelinhas, margens 3/2/3/2 cm)
// Uso: node gen_docx.js entrada.md saida.docx
const fs = require('fs');
const path = require('path');
const docx = (() => { try { return require('docx'); } catch (e) { return require(path.join(__dirname, '..', 'node_modules', 'docx')); } })();
const { Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel, Footer, PageNumber,
  LevelFormat, Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, PageBreak } = docx;

const [,, inFile, outFile] = process.argv;
if (!inFile || !outFile) { console.error('uso: node gen_docx.js in.md out.docx'); process.exit(1); }
const src = fs.readFileSync(inFile, 'utf8').replace(/\r\n/g, '\n');

const FONT = 'Times New Roman';
const SIZE = 24; // half-points = 12pt
const cm = (v) => Math.round(v * 567); // 1 cm = 567 DXA

function runsFromInline(text, base = {}) {
  // supports **bold**, *italic*, __underline__ ; nesting minimal
  const runs = [];
  const re = /(\*\*[^*]+\*\*|__[^_]+__|\*[^*]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), font: FONT, size: SIZE, ...base }));
    const tok = m[0];
    if (tok.startsWith('**')) runs.push(new TextRun({ text: tok.slice(2, -2), bold: true, font: FONT, size: SIZE, ...base }));
    else if (tok.startsWith('__')) runs.push(new TextRun({ text: tok.slice(2, -2), underline: {}, font: FONT, size: SIZE, ...base }));
    else runs.push(new TextRun({ text: tok.slice(1, -1), italics: true, font: FONT, size: SIZE, ...base }));
    last = m.index + tok.length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), font: FONT, size: SIZE, ...base }));
  return runs;
}

const children = [];
const lines = src.split('\n');
let i = 0;
let para = [];
const flushPara = () => {
  if (!para.length) return;
  const text = para.join(' ').replace(/\s+/g, ' ').trim();
  para = [];
  if (!text) return;
  children.push(new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: cm(1.25) },
    spacing: { line: 360, after: 120 },
    children: runsFromInline(text),
  }));
};

function tableFromLines(tl) {
  const rows = tl.filter(l => !/^\s*\|?\s*:?-{2,}/.test(l)).map(l => l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim()));
  const ncol = Math.max(...rows.map(r => r.length));
  const total = cm(16);
  const colW = Array(ncol).fill(Math.floor(total / ncol));
  const border = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
  const borders = { top: border, bottom: border, left: border, right: border };
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: colW,
    rows: rows.map((r, ri) => new TableRow({ children: Array.from({ length: ncol }, (_, ci) => new TableCell({
      width: { size: colW[ci], type: WidthType.DXA },
      borders,
      shading: ri === 0 ? { type: ShadingType.CLEAR, fill: 'EDEDED', color: 'auto' } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [new Paragraph({ spacing: { line: 276, after: 0 }, children: runsFromInline(r[ci] || '', { size: 20, bold: ri === 0 }) })],
    })) })),
  });
}

while (i < lines.length) {
  const raw = lines[i];
  const line = raw.replace(/\s+$/, '');
  if (line.trim() === '') { flushPara(); i++; continue; }
  if (line.trim() === '\\pagebreak' || line.trim() === '<<<QUEBRA>>>') { flushPara(); children.push(new Paragraph({ children: [new PageBreak()] })); i++; continue; }
  if (/^---+$/.test(line.trim())) { flushPara(); children.push(new Paragraph({ spacing: { after: 120 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '000000', space: 1 } }, children: [] })); i++; continue; }
  if (line.startsWith('@@ ')) { flushPara(); const nextIsCentered = (lines[i+1] || '').startsWith('@@ ') || ((lines[i+1] || '').trim() === '' && (lines[i+2] || '').startsWith('@@ ')); children.push(new Paragraph({ alignment: AlignmentType.CENTER, keepNext: nextIsCentered, keepLines: true, spacing: { line: 360, after: 120 }, children: runsFromInline(line.slice(3)) })); i++; continue; }
  if (line.startsWith('# ')) { flushPara(); children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240, after: 240, line: 360 }, children: runsFromInline(line.slice(2).toUpperCase(), { bold: true }) })); i++; continue; }
  if (line.startsWith('## ')) { flushPara(); children.push(new Paragraph({ alignment: AlignmentType.LEFT, keepNext: true, spacing: { before: 360, after: 180, line: 360 }, children: runsFromInline(line.slice(3), { bold: true }) })); i++; continue; }
  if (line.startsWith('### ')) { flushPara(); children.push(new Paragraph({ alignment: AlignmentType.LEFT, keepNext: true, spacing: { before: 240, after: 120, line: 360 }, children: runsFromInline(line.slice(4), { bold: true, italics: true }) })); i++; continue; }
  if (line.startsWith('> ')) {
    flushPara();
    const q = [];
    while (i < lines.length && lines[i].startsWith('>')) { q.push(lines[i].replace(/^>\s?/, '')); i++; }
    const text = q.join(' ').replace(/\s+/g, ' ').trim();
    children.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, indent: { left: cm(4) }, spacing: { line: 240, after: 200 }, children: runsFromInline(text, { size: 22 }) }));
    continue;
  }
  if (/^\s*[-•]\s+/.test(line)) {
    flushPara();
    while (i < lines.length && /^\s*[-•]\s+/.test(lines[i])) {
      const t = lines[i].replace(/^\s*[-•]\s+/, '');
      children.push(new Paragraph({ numbering: { reference: 'bullets', level: 0 }, alignment: AlignmentType.JUSTIFIED, spacing: { line: 360, after: 80 }, children: runsFromInline(t) }));
      i++;
    }
    continue;
  }
  if (/^\s*\|.*\|\s*$/.test(line)) {
    flushPara();
    const tl = [];
    while (i < lines.length && /^\s*\|.*\|\s*$/.test(lines[i])) { tl.push(lines[i]); i++; }
    children.push(tableFromLines(tl));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    continue;
  }
  para.push(line.trim());
  i++;
}
flushPara();

const doc = new Document({
  creator: 'Espírito Santo Advocacia',
  title: path.basename(outFile, '.docx'),
  styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
  numbering: { config: [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: cm(1.25), hanging: cm(0.6) } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: cm(3), right: cm(2), bottom: cm(2), left: cm(3) } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 20 })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(outFile, buf); console.log('OK', outFile, buf.length, 'bytes'); });
