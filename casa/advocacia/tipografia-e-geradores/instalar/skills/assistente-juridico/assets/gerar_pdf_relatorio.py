# -*- coding: utf-8 -*-
"""
Gerador de PDF de RELATÓRIO / PARECER interno GFES: markdown completo -> HTML -> PDF (Chrome headless).
Diferente de gerar_pdf.py (peça forense), este renderiza TÍTULOS (#, ##, ###), TABELAS,
CITAÇÕES (>), listas ordenadas/não-ordenadas, negrito/itálico/código — para documentos de
trabalho LEGÍVEIS (parecer, análise, relatório). NÃO é peça protocolável.

Uso:  python3 gerar_pdf_relatorio.py "/caminho/do/parecer.md"   (gera parecer.pdf ao lado)
- Frontmatter YAML é removido (não vaza no PDF).
"""
import re, html, sys, os, subprocess, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from metadados_pdf import limpar_metadados, titulo_de_arquivo

CHROME = os.environ.get("GFES_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

CSS = """
/* MARGENS E ENTRELINHA — Masterclass "Formatando Petições com Excelência", aula 2
   (transcrita palavra por palavra em 27/08/2026): as laterais definem o comprimento da
   linha e são a parte mais importante da ergonomia visual — "em regra não vamos deixar
   menos de 5 cm no total lateral"; e "fuja daquele entrelinhamento de 1,5, é muito
   entrelinhamento para a maioria das fontes". Ordem do Dr. Gabriel de 27/08/2026: esta
   tipografia vale para QUALQUER peça ou documento do escritório. */
/* 02/09/2026 (item 3.11, Masterclass aula 2): a PRIMEIRA página leva o timbre completo e o
   rodapé com os dados; as SEGUINTES levam só a marca reduzida e a numeração, para não
   pesar. Feito com caixas de margem de página (Chrome 131+): nada se repete no fluxo. */
@page { size: A4; margin: 2.0cm 2.7cm 1.8cm 2.7cm;
  @top-left { content: "ESPÍRITO SANTO ADVOCACIA"; font: bold 8pt 'Times New Roman', Times, serif;
              color: #1a2b3c; letter-spacing: 0.4pt; vertical-align: bottom; padding-bottom: 4pt; }
  @top-right { content: "OAB/SC 53.040"; font: 8pt 'Times New Roman', Times, serif; color: #33475b;
               vertical-align: bottom; padding-bottom: 4pt; }
  @bottom-center { content: "Pg. " counter(page); font: 8pt 'Times New Roman', Times, serif; color: #33475b; } }
@page :first { margin-top: 1.8cm;
  @top-left { content: none; } @top-right { content: none; }
  @bottom-center { content: "Rua Angelita Figueiredo, 1.596, Sala 1004, Torre B — Areias, São José/SC · (48) 98421-6664\A gfdoes@gmail.com · espiritosantoadvocaciasc.com.br"; white-space: pre-line; font: 7.5pt 'Times New Roman', Times, serif; color:#33475b; line-height: 1.3; text-align: center; } }
* { box-sizing: border-box; }
body { font-family: 'Times New Roman', Times, serif; font-size: 12pt;
       line-height: 1.35; color:#000; margin:0; text-align: justify;
       hyphens: auto; -webkit-hyphens: auto; }
h1 { font-size: 17pt; color:#1a2b3c; text-align:left; border-bottom:2px solid #1a2b3c;
     padding-bottom:5px; margin: 0 0 12pt 0; line-height:1.25; }
h2 { font-size: 13.5pt; color:#1a2b3c; text-align:left; margin: 20pt 0 10pt 0;
     border-bottom:1px solid #ccc; padding-bottom:3px; }
h3 { font-size: 12pt; color:#33475b; text-align:left; margin: 15pt 0 8pt 0; }

/* ═══ VÃO NO PÉ DA PÁGINA — ordem do Dr. Gabriel, 27/08/2026 ══════════════════════════
   "final de algumas páginas continua um espaço em branco, quase que quarenta por cento".
   Na Masterclass (aula 2, transcrita), "muito espaço em branco à TOA" é defeito da peça
   ruim, e não se deixa "latifúndio improdutivo": branco COM função é respiro; branco à
   toa é falha. CAUSA: bloco alto e indivisível empurrado inteiro para a folha seguinte.
   REGRA: o que não pode partir é a LINHA — nunca o bloco inteiro.
   ══════════════════════════════════════════════════════════════════════════════════ */
.janela.longa, .jan.longa { page-break-inside: auto; break-inside: auto; }
.janela.longa > p, .jan.longa > p,
.janela.longa li, .jan.longa li { page-break-inside: avoid; break-inside: avoid; }
.janela.longa > p:last-child, .jan.longa > p:last-child { page-break-before: avoid; break-before: avoid; }
.janela.longa > p:first-child, .jan.longa > p:first-child { page-break-after: avoid; break-after: avoid; }
table.longa { page-break-inside: auto; break-inside: auto; }
table.longa thead { display: table-header-group; }
table tr { page-break-inside: avoid; break-inside: avoid; }
ul.tl.longa { page-break-inside: auto; break-inside: auto; }
ul.tl.longa li:last-child  { page-break-before: avoid; break-before: avoid; }
ul.tl.longa li:first-child { page-break-after: avoid;  break-after: avoid; }
img { max-height: 8.2cm; width: auto; height: auto; }

/* ASSINATURA CANÔNICA — marca registrada do advogado (ordem do Dr. Gabriel, 27/08/2026). */
.assin { margin: 34pt 0 0 0; text-align: center; page-break-inside: avoid; }
.assin p { text-indent: 0; margin: 0; text-align: center; line-height: 1.35; }
.assin-nome, .assin-cargo, .assin-oab { font-size: 12pt; }
p { margin: 0 0 7pt 0; }
ul, ol { margin: 0 0 7pt 0; padding-left: 1.6em; }
li { margin: 0 0 4pt 0; }
strong { font-weight: bold; color:#111; }
code { font-family: 'SF Mono', Menlo, Consolas, monospace; font-size: 9.5pt;
       background:#eef1f4; padding:1px 4px; border-radius:3px; }
hr { border:0; border-top:1px solid #ccc; margin: 14pt 0; }
/* Citação em bloco a 3 cm — mesma aula: 4 cm é recuo demais ("quanto maior o recuo,
   menor a coluna, mais problema de formatação"). Marcas da citação: recuo e fonte
   menor. Nunca itálico — o itálico é da citação direta no corpo do texto. */
blockquote { margin: 8pt 0 8pt 3cm; padding: 0; text-align:left; line-height: 1.3;
             font-family: Charter, 'Bitstream Charter', Georgia, serif; font-size: 11pt; }
blockquote p { margin: 0 0 4pt 0; }
blockquote p:last-child { margin:0; }
table { border-collapse: collapse; width:100%; margin: 8pt 0; font-size: 10.5pt; }
th { background:#1a2b3c; color:#fff; text-align:left; padding:6px 9px; border:1px solid #1a2b3c; }
td { padding:6px 9px; border:1px solid #cbd2d9; vertical-align:top; text-align:left; }
tr:nth-child(even) td { background:#f5f7f9; }

/* Título e subtítulo centralizados do parecer (marcação @@ / @@@) — 25/08/2026 */
p.doc-title { text-align:center; hyphens: none; -webkit-hyphens: none; word-break: keep-all; font-size:16pt; font-weight:bold; color:#1a2b3c;
              margin: 4pt 0 2pt 0; line-height:1.2; letter-spacing:0.2pt; }
p.doc-sub   { text-align:center; font-size:10.5pt; color:#33475b; font-style:italic;
              margin: 0 0 14pt 0; }

/* Janelas de destaque (callouts coloridos) — 25/08/2026 */
.janela { border-radius:6px; padding:9pt 12pt 8pt 12pt; margin:11pt 0; text-align:left;
          page-break-inside:avoid; border-left:4px solid; }
.janela .jt { font-weight:bold; font-size:11pt; margin:0 0 4pt 0; }
.janela p { margin:0 0 4pt 0; text-align:left; }
.janela p:last-child { margin:0; }
.janela.destaque  { background:#eef4fb; border-color:#2e6fb7; }
.janela.destaque  .jt { color:#1f4e86; }
.janela.favoravel { background:#eef7ef; border-color:#3a915a; }
.janela.favoravel .jt { color:#256b3f; }
.janela.atencao   { background:#fdf3ec; border-color:#c9642a; }
.janela.atencao   .jt { color:#9a4a1a; }
/* --- 27/08/2026: REPERTÓRIO UNIFICADO com o gerador de peça (ordem do Dr. Gabriel).
   Os tipos antigos (destaque/favoravel/atencao/processo) seguem válidos. --- */
.jan { border: 0.6pt solid; border-left-width: 3pt; border-radius: 2pt;
       padding: 7pt 10pt 6pt 10pt; margin: 10pt 0 12pt 0; text-align: justify;
       page-break-inside: avoid; text-indent: 0; }
.jan p { text-indent: 0; margin: 0 0 4pt 0; }
.jan p:last-child { margin: 0; }
.jan .jrot { display:block; font-size: 10pt; font-weight: bold; letter-spacing: 0.3pt;
             text-transform: uppercase; margin: 0 0 4pt 0; }
.jan.qualif { background:#F4F6FA; border-color:#C3CDDE; border-left-color:#1F3864;
              margin-left: 2cm; }
.jan.qualif .jrot { color:#1F3864; }
.jan.cita { background:#F7F7F4; border-color:#DCDCD4; border-left-color:#6E6E62;
            margin-left: 2cm; font-family: Charter, 'Bitstream Charter', Georgia, serif;
            font-size: 11pt; display: flex; flex-direction: column; }
.jan.cita .jrot { order: 2; align-self: flex-end; margin: 5pt 0 0 0;
                  font-size: 8.5pt; font-weight: bold; text-transform: none;
                  color: #1F3864; background: #EDF1F7; border: 0.5pt solid #C3CDDE;
                  border-radius: 2pt; padding: 2pt 6pt; letter-spacing: 0.2pt; }
.jan.poderes { background:#F5F7FA; border-color:#CBD4E0; border-left-color:#2E5077; }
.jan.poderes .jrot { color:#2E5077; }
.jan.tempo { background:#F5F7FA; border-color:#CBD4E0; border-left-color:#2E5077; }
.jan.tempo .jrot { color:#2E5077; }
.jan.tempo ul.tl { margin: 2pt 0 0 0; }
.jan.calc { background:#FAF7F0; border-color:#E2D9C4; border-left-color:#8C7340; }
.jan.calc .jrot { color:#6E5A2E; }
.jan.calc table.q { margin: 2pt 0 0 0; }
.jan.dout { background:#F4F7F1; border-color:#CDD9C4; border-left-color:#4A6B3A;
            margin-left: 2cm; font-family: Charter, 'Bitstream Charter', Georgia, serif;
            font-size: 11pt; display: flex; flex-direction: column; }
/* A etiqueta é FAIXA DE LARGURA TOTAL: cabe a referência completa, que existe para o julgador
   CONFERIR a fonte (lição do Dr. Gabriel, de quando foi assessor de juiz — 26/08/2026). */
.jan.dout .jrot { order: 2; align-self: stretch; margin: 6pt 0 0 0;
                  font-size: 8.5pt; font-weight: normal; text-transform: none;
                  text-align: left; line-height: 1.3;
                  color: #3B5730; background: #EDF3E8; border: 0.5pt solid #CDD9C4;
                  border-radius: 2pt; padding: 3pt 7pt; letter-spacing: 0; }
.jan.dout .jrot::before { content: "Fonte: "; font-weight: bold; }
.jan.jur { background:#F7F4F9; border-color:#DACFE2; border-left-color:#5B4576;
           margin-left: 2cm; font-family: Charter, 'Bitstream Charter', Georgia, serif;
           font-size: 11pt; display: flex; flex-direction: column; }
.jan.jur .jrot { order: 2; align-self: stretch; margin: 6pt 0 0 0;
                 font-size: 8.5pt; font-weight: normal; text-transform: none;
                 text-align: left; line-height: 1.3;
                 color: #4A3663; background: #F1EBF5; border: 0.5pt solid #DACFE2;
                 border-radius: 2pt; padding: 3pt 7pt; letter-spacing: 0; }
.jan.jur .jrot::before { content: "Fonte: "; font-weight: bold; }
/* Linha do tempo */
ul.tl { list-style:none; margin: 8pt 0 12pt 0; padding-left: 1.2cm; }
ul.tl li { position:relative; margin: 0 0 6pt 0; text-align:left; line-height:1.35;
           padding-left: 0.5cm; border-left: 1.2pt solid #B8C4D4; page-break-inside: avoid; }
ul.tl li .dt { display:inline-block; font-weight:bold; color:#1F3864; min-width:3.1cm; }
ul.tl li.mark { border-left-color:#1F3864; }
ul.tl li.mark .dt { color:#8C2B2B; }

.janela.processo  { background:#f3eefb; border-color:#6a4bb0; }
.janela.processo  .jt { color:#4a327f; }

/* --- papel timbrado GFES (18/08/2026) --- */
table#folha { border-collapse: collapse; width:100%; margin:0; font-size: inherit; }
table#folha > thead > tr > th, table#folha > tbody > tr > td,
table#folha > tfoot > tr > td { border:0; padding:0; background:none; color:inherit; }
table#folha > tbody > tr > td { padding: 0; }
#timbre { border-bottom: 1.2pt solid #1a2b3c; padding-bottom: 5pt; margin-bottom: 12pt; text-align:left; }
#timbre .nome { font-size: 13.5pt; font-weight: bold; color:#1a2b3c;
                letter-spacing: 0.4pt; margin: 0; line-height: 1.2; }
#timbre .oab  { font-size: 9pt; color:#33475b; margin: 2pt 0 0 0; line-height: 1.2;
                font-weight: normal; }
#rodape { border-top: 0.6pt solid #98a4b0; padding-top: 3pt; margin-top: 10pt;
          font-size: 8pt; color:#33475b; text-align: center; line-height: 1.35;
          font-weight: normal; }
#rodape p { margin: 0; }
"""

FOLHA_ABRE = """<table id="folha"><tbody><tr><td>
<div id="timbre">
  <p class="nome">ESP\u00cdRITO SANTO ADVOCACIA</p>
  <p class="oab">Dr. Gabriel Fabr\u00edzio do Esp\u00edrito Santo &mdash; OAB/SC 53.040 &nbsp;&middot;&nbsp; CNPJ 50.411.747/0001-00</p>
</div>
<!-- 02/09/2026: o rodapé com os dados foi para a caixa de margem da primeira página; as páginas
     seguintes levam só a marca reduzida e "Pg. n" (item 3.11). -->
"""
FOLHA_FECHA = "</td></tr></tbody></table>"

def inline(s):
    s = html.escape(s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*([^*]+?)\*(?![\*\w])", r"<em>\1</em>", s)
    return s

def render_table(rows):
    # rows = lista de linhas markdown de tabela (inclui a linha separadora ---)
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    header, body = cells[0], cells[2:]   # cells[1] = separador
    # 27/08/2026 — tabela com 8 linhas ou mais quebra entre páginas (repetindo o
    # cabeçalho) em vez de ser empurrada inteira e abrir vão no pé da folha anterior.
    out = ["<table class='longa'><thead><tr>" if len(body) >= 8 else "<table><thead><tr>"]
    out += ["<th>" + inline(c) + "</th>" for c in header]
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>" + "".join("<td>" + inline(c) + "</td>" for c in row) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)

def is_table_row(s):
    return s.startswith("|") and s.endswith("|") and "|" in s[1:]


JANELAS_CANON = {"qualificacao": "qualif", "qualif": "qualif",
                 "citacao": "cita", "cita": "cita",
                 "linhadotempo": "tempo", "tempo": "tempo",
                 "calculo": "calc", "calc": "calc",
                 "doutrina": "dout", "dout": "dout",
                 "sumula": "jur", "jurisprudencia": "jur", "jur": "jur",
                 "poderes": "poderes", "objeto": "poderes"}

def eixo_do_tempo(linhas):
    """Renderiza os eventos '~ data | texto' como EIXO HORIZONTAL com seta e cortes
    verticais marcando o tempo (padrão canônico 26/08/2026). Prefixo '!' destaca o marco.
    Linhas que não forem evento entram como parágrafo antes do eixo."""
    antes, marcos = [], []
    for l in linhas:
        s = l.strip()
        if not s: continue
        if s.startswith("~ "):
            corpo = s[2:].strip()
            mark = ""
            if corpo.startswith("!"): mark, corpo = " mark", corpo[1:].strip()
            dt, _, tx = corpo.partition("|")
            marcos.append((dt.strip(), tx.strip(), mark))
        else:
            antes.append("<p>" + inline(s) + "</p>")
    if not marcos:
        return "".join(antes)
    cels = "".join("<span class='mk%s'><span class='dt'>%s</span>"
                   "<span class='tx'>%s</span></span>" % (m, inline(d), inline(t))
                   for d, t, m in marcos)
    return ("".join(antes) + "<div class='eixo'><div class='trilho'></div>"
            "<div class='marcos'>" + cels + "</div></div>")

def body_to_html(body):
    lines = body.split("\n")
    out, i = [], 0
    list_stack = None   # 'ul' ou 'ol'
    def close_list():
        nonlocal list_stack
        if list_stack: out.append("</%s>" % list_stack); list_stack = None
    while i < len(lines):
        s = lines[i].rstrip()
        st = s.strip()
        if st == "":
            close_list(); i += 1; continue
        # separador horizontal
        if re.fullmatch(r"-{3,}", st):
            close_list(); out.append("<hr>"); i += 1; continue
        # título/subtítulo centralizado do parecer (@@ = título, @@@ = subtítulo) — 25/08/2026
        # assinatura canônica (27/08/2026)
        if st.startswith("@assinatura"):
            _cargo = st[len("@assinatura"):].strip() or "Advogado"
            close_list()
            out.append("<div class='assin'>"
                       "<p class='assin-nome'><strong>Gabriel Fabrízio do Espírito Santo</strong></p>"
                       "<p class='assin-cargo'>" + html.escape(_cargo) + "</p>"
                       "<p class='assin-oab'>OAB/SC 53.040</p></div>"); i += 1; continue
        m = re.match(r"(@{2,3})\s+(.*)", st)
        if m:
            close_list()
            cls = "doc-sub" if len(m.group(1)) >= 3 else "doc-title"
            out.append("<p class='%s'>%s</p>" % (cls, inline(m.group(2).strip()))); i += 1; continue
        # títulos
        m = re.match(r"(#{1,6})\s+(.*)", st)
        if m:
            close_list(); lvl = min(len(m.group(1)), 3)
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2).strip()), lvl)); i += 1; continue
        # tabela
        if is_table_row(st):
            close_list(); tbl = []
            while i < len(lines) and is_table_row(lines[i].strip()):
                tbl.append(lines[i].strip()); i += 1
            if len(tbl) >= 2: out.append(render_table(tbl))
            else: out.append("<p>" + inline(tbl[0]) + "</p>")
            continue
        # citação / janela de destaque (agrupa linhas > consecutivas)
        if st.startswith(">"):
            close_list(); buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            first = buf[0].strip() if buf else ""
            mcal = re.match(r"\[!(\w+)\]\s*(.*)", first)
            if mcal:
                tipo = mcal.group(1).lower()
                if tipo in JANELAS_CANON:          # 27/08/2026 — repertório da peça
                    ccls = JANELAS_CANON[tipo]
                    rot = mcal.group(2).strip()
                    corpo_c = buf[1:]
                    if ccls == "tempo":
                        interno_c = eixo_do_tempo(corpo_c)
                    else:
                        # processa tabela DENTRO da janela (senão a marcação sai crua)
                        interno_c, jbuf = "", []
                        def _flush_j():
                            nonlocal_j = None
                        k = 0
                        while k < len(corpo_c):
                            xs = corpo_c[k].strip()
                            if is_table_row(xs):
                                tb = []
                                while k < len(corpo_c) and is_table_row(corpo_c[k].strip()):
                                    tb.append(corpo_c[k].strip()); k += 1
                                interno_c += render_table(tb); continue
                            if xs:
                                interno_c += "<p>" + inline(xs) + "</p>"
                            k += 1
                    rot_h = ("<span class='jrot'>" + inline(rot) + "</span>") if rot else ""
                    # 27/08/2026 — janela ALTA quebra entre páginas (nunca dentro de uma
                    # linha) em vez de abrir vão no pé da folha anterior.
                    _alta = (len("\n".join(corpo_c)) > 700 or "'longa'" in interno_c
                             or "tl longa" in interno_c)
                    out.append("<div class='jan " + ccls + (" longa" if _alta else "")
                               + "'>" + rot_h + interno_c + "</div>")
                    continue
                cls = tipo if tipo in ("destaque", "favoravel", "atencao", "processo") else "destaque"
                titulo = mcal.group(2).strip()
                corpo = buf[1:]
                inner = ("<p class='jt'>" + inline(titulo) + "</p>") if titulo else ""
                inner += "".join("<p>" + inline(x.strip()) + "</p>" for x in corpo if x.strip())
                _alta = len("\n".join(corpo)) > 700
                out.append("<div class='janela " + cls + (" longa" if _alta else "")
                           + "'>" + inner + "</div>"); continue
            inner = "".join("<p>" + inline(x.strip()) + "</p>" for x in buf if x.strip())
            out.append("<blockquote>" + inner + "</blockquote>"); continue
        # lista ordenada
        m = re.match(r"\d+\.\s+(.*)", st)
        if m:
            if list_stack != "ol": close_list(); out.append("<ol>"); list_stack = "ol"
            out.append("<li>" + inline(m.group(1).strip()) + "</li>"); i += 1; continue
        # lista não-ordenada
        if st.startswith("- "):
            if list_stack != "ul": close_list(); out.append("<ul>"); list_stack = "ul"
            out.append("<li>" + inline(st[2:].strip()) + "</li>"); i += 1; continue
        # parágrafo
        close_list(); out.append("<p>" + inline(st) + "</p>"); i += 1
    close_list()
    return "\n".join(out)

def main():
    md_path = sys.argv[1]
    raw = open(md_path, encoding="utf-8").read()
    if raw.startswith("---"):
        raw = raw.split("---", 2)[2]
    body = raw.strip()
    # Gate de TAG CRUA (ordem do Gabriel, 19/08/2026).
    # Nenhum documento da casa pode sair com marcação de máquina visível — <br>, <div>, <p>,
    # comentário HTML. Além de feio, denuncia que o texto foi montado por ferramenta, e o
    # documento do escritório não pode carregar essa marca. Ver a nota no vault.
    tags = re.findall(r"<\s*/?\s*(?:br|p|div|span|b|i|u|hr|table|tr|td|th|img|a|h[1-6]|"
                      r"strong|em|ul|ol|li|blockquote|pre|code|font|center)\b[^>]*>|<!--.*?-->",
                      body, flags=re.I | re.S)
    if tags:
        print("TAGS HTML CRUAS no markdown — o PDF sairia com elas impressas:")
        for n, linha in enumerate(body.splitlines(), 1):
            for t in re.findall(r"<[^>\n]{1,80}>", linha):
                if re.match(r"<\s*/?\s*(?:br|p|div|span|b|i|u|hr|table|tr|td|th|img|a|h[1-6]|"
                            r"strong|em|ul|ol|li|blockquote|pre|code|font|center)\b", t, re.I):
                    print(f"  L{n}: {t}    → {linha.strip()[:70]}")
        print("\nPDF NÃO gerado. Use markdown puro: linha em branco separa parágrafo,")
        print("'**texto**' para negrito, '---' para filete. Nunca tag HTML.")
        sys.exit(1)
    # Gate de norma culta (Decreto 6.583/2008 — AO 1990) sobre o corpo que vira PDF.
    # Documento de trabalho interno: modo "geral" (admite [VERIFICADO]/[VERIFICAR], que o
    # modo "peca" bloqueia). Alcance ampliado a TODO documento da casa em 19/08/2026.
    validador = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "..", "scripts", "validar_norma_culta.py")
    if os.path.exists(validador):
        chk = subprocess.run([sys.executable, validador, "--stdin", "--modo", "geral"],
                             input=body, text=True, capture_output=True)
        if chk.returncode == 1:
            print(chk.stdout)
            print("PDF NÃO gerado: corrija os ERROS acima.")
            sys.exit(1)
    else:
        print("[aviso] validar_norma_culta.py não encontrado; gerando sem gate.")
    # Gate da REGRA DO PORTADOR (canônica 19/08/2026) — fato sem coordenada não vira tese.
    # Complementa o gate de norma culta: aquele cuida do DIREITO, este cuida do FATO.
    validador_fato = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "..", "scripts", "validar_ficha_de_fatos.py")
    if os.path.exists(validador_fato):
        chk_fato = subprocess.run([sys.executable, validador_fato, "--stdin", "--modo", "geral"],
                                  input=body, text=True, capture_output=True)
        if chk_fato.returncode == 1:
            print(chk_fato.stdout)
            print("PDF NÃO gerado: corrija os ERROS de fato acima (regra do portador).")
            sys.exit(1)
    else:
        print("[aviso] validar_ficha_de_fatos.py não encontrado; gerando sem esse gate.")

    full = ("<!doctype html><html lang='pt-br'><head><meta charset='utf-8'><style>" + CSS +
            "</style></head><body>" + FOLHA_ABRE + body_to_html(body) + FOLHA_FECHA + "</body></html>")
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    with tempfile.TemporaryDirectory() as td:
        html_tmp = os.path.join(td, "doc.html")
        pdf_tmp  = os.path.join(td, "doc.pdf")
        open(html_tmp, "w", encoding="utf-8").write(full)
        try:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--user-data-dir=" + os.path.join(td, "cdir"),
                            "--no-pdf-header-footer", "--print-to-pdf=" + pdf_tmp,
                            "file://" + html_tmp],
                           timeout=90, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            pass
        if not os.path.exists(pdf_tmp):
            print("ERRO: PDF não gerado"); sys.exit(1)
        shutil.copy(pdf_tmp, pdf_path)
    # Metadados canônicos (regra 19): o Chrome deixa /Title doc.html,
    # /Creator HeadlessChrome e /Producer Skia/PDF — metadado denunciante.
    # Reescreve ANTES do gate forense e antes de qualquer entrega.
    limpar_metadados(pdf_path, titulo=titulo_de_arquivo(pdf_path))
    # Gate FORENSE (regra 19, canônica 24/08/2026): nenhum PDF sai com rastro de IA,
    # marcação crua, tag, camada oculta ou metadado denunciante. Faltava aqui até
    # 27/08/2026 — foi por essa porta que o relatório de caso saiu com metadado do Chrome.
    forense = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "scripts", "forense_documento.py")
    if os.path.exists(forense):
        chk_f = subprocess.run([sys.executable, forense, pdf_path, "--modo", "saida"],
                               capture_output=True, text=True)
        if chk_f.returncode == 1:
            reprovado = os.path.splitext(pdf_path)[0] + "_REPROVADO-FORENSE.pdf"
            os.replace(pdf_path, reprovado)
            print(chk_f.stdout)
            print("PDF REPROVADO no gate forense (regra 19) e renomeado para:", reprovado)
            print("NÃO entregar. Corrija a origem e gere de novo.")
            sys.exit(1)
    # Gate de DIAGRAMAÇÃO (ordem do Dr. Gabriel, 27/08/2026): mede o VÃO no pé de cada
    # página. Bloco alto e indivisível empurrado para a folha seguinte deixa 30-45% de
    # branco — defeito que a conferência da última página NÃO pega.
    _diag = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "scripts", "validar_diagramacao.py")
    if os.path.exists(_diag):
        _chk = subprocess.run([sys.executable, _diag, pdf_path],
                              capture_output=True, text=True)
        if _chk.returncode == 1:
            print(_chk.stdout)
            print(">>> VÃO NO PÉ DA PÁGINA: conserte antes de entregar (regra 27).")
    print("PDF:", pdf_path)

    # ---- GATE DE PAGINAÇÃO E TIPOGRAFIA (27/08/2026) --------------------------------
    # Ordem do Gabriel: "nas petições não pode haver linhas órfãs ou páginas em branco"
    # e "anote para não haver mais erros". Roda DEPOIS de gerar, sobre o PDF, e confere
    # contra references/tipografia-vigente.json (fonte única das medidas). Não aborta a
    # geração — o PDF já existe —, mas GRITA e devolve código 1, para que ninguém entregue
    # peça com órfã, viúva, página em branco ou medida revogada sem ter visto o aviso.
    gate_pag = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "scripts", "validar_paginacao.py")
    if os.path.exists(gate_pag) and "--sem-validacao" not in sys.argv:
        chk = subprocess.run([sys.executable, gate_pag, pdf_path], capture_output=True, text=True)
        if chk.returncode == 1:
            print(chk.stdout)
            print(">>> O PDF FOI GERADO, MAS REPROVOU NO GATE DE PAGINAÇÃO. NÃO ENTREGUE ASSIM.")
            sys.exit(1)

if __name__ == "__main__":
    main()
