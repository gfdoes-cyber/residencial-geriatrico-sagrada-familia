# -*- coding: utf-8 -*-
"""
Gerador de PDF de CONTRATO / documento institucional GFES Advocacia.
markdown -> HTML -> PDF (Chrome headless). PAPEL TIMBRADO (logo no topo).

Uso:  python3 gerar_contrato_pdf.py "/caminho/contrato.md" [--sem-logo] [--sem-validacao]

Diferente de gerar_pdf.py (peça forense LIMPA): contrato é documento INSTITUCIONAL e
leva LOGOMARCA no cabeçalho (decisão 29/05/2026: contrato/parecer/carta = papel
timbrado; a exceção sem logo é só a peça forense). Tipografia ABNT idêntica:
Times New Roman 12, A4, margens 3/2/2/3 cm, entrelinha 1,5, justificado, recuo 1,25 cm.

Marcação no .md:
  `# TÍTULO`         -> título do contrato (centralizado, negrito, caixa alta)
  `## CLÁUSULA ...`  -> cabeçalho de cláusula (negrito, à esquerda)
  `### ...`          -> subcláusula / subtítulo (negrito, à esquerda)
  `@@ texto`         -> linha centralizada (local/data, linhas de assinatura)
  `---`              -> separador (espaço vertical entre blocos)
  `- texto`          -> item de lista
  `**Rótulo:** ...`  -> início de item (negrito inline; parágrafo sem recuo)
  `\\` (linha só)    -> espaço vertical
  demais linhas      -> parágrafo justificado com recuo de 1ª linha

Gate: roda scripts/validar_norma_culta.py sobre o corpo (sem frontmatter). Erro -> aborta.
Logo: assets/logo_advocacia.png (override: env GFES_LOGO=/caminho ; --sem-logo remove).
"""
import re, html, sys, os, subprocess, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from metadados_pdf import limpar_metadados, titulo_de_arquivo

CHROME = os.environ.get("GFES_CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
LOGO_DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo_advocacia.png")

CSS = """
/* MARGENS E ENTRELINHA — Masterclass "Formatando Petições com Excelência", aula 2
   (transcrita palavra por palavra em 27/08/2026): laterais nunca abaixo de 5 cm no total
   (o professor usa 3 + 3), porque são elas que definem o comprimento da linha; e "fuja
   daquele entrelinhamento de 1,5, é muito entrelinhamento para a maioria das fontes".
   Ordem do Dr. Gabriel de 27/08/2026: vale para QUALQUER documento do escritório. */
/* 02/09/2026 (item 3.11): logo completa só na primeira página (fluxo); nas seguintes, a
   marca reduzida em texto e a numeração, por caixas de margem de página. */
@page { size: A4; margin: 2.5cm 3cm 2cm 3cm;
  @top-center { content: "ESPÍRITO SANTO ADVOCACIA"; font: bold 8pt 'Times New Roman', Times, serif;
                color: #1F3864; letter-spacing: 0.4pt; vertical-align: bottom; padding-bottom: 6pt; }
  @bottom-center { content: "Pg. " counter(page); font: 8pt 'Times New Roman', Times, serif; color: #33475b; } }
@page :first { @top-center { content: none; } @bottom-center { content: none; } }
* { box-sizing: border-box; }
body { font-family: 'Times New Roman', Times, serif; font-size: 12pt; line-height: 1.35;
       hyphens: auto; -webkit-hyphens: auto;
       text-align: justify; color:#000; margin:0; }
.logo { text-align:center; margin: 0 0 18pt 0; }
.logo img { width: 3.5cm; height:auto; }
h1.titulo { font-size: 13pt; font-weight: bold; text-align:center; text-transform:uppercase;
            text-indent:0; margin: 0 0 16pt 0; line-height:1.3; }
h2.clausula { font-size: 12pt; font-weight: bold; text-align:left; text-indent:0;
              margin: 14pt 0 6pt 0; }
h3.sub { font-size: 12pt; font-weight: bold; text-align:left; text-indent:0; margin: 13pt 0 8pt 0; }

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
p { text-indent: 2cm; margin: 0; }
p.center { text-align:center; text-indent:0; margin: 0 0 6pt 0;
           /* 27/08/2026 (ordem do Dr. Gabriel): o endereçamento ao juízo NUNCA se
              separa. Sem hifenização e sem quebra dentro de palavra. */
           hyphens: none; -webkit-hyphens: none; overflow-wrap: normal;
           word-break: keep-all; }
p.flush  { text-indent:0; margin: 0 0 6pt 0; }
ul { margin: 0 0 6pt 0; padding-left: 1.9cm; }
li { margin: 0 0 2pt 0; text-align: justify; }
strong { font-weight: bold; }
.sp { height: 0.6cm; }

/* JANELAS SUSPENSAS (padrão canônico 26/08/2026 — estendido do gerador de peça por ordem do
   Dr. Gabriel: vale para toda peça E para as procurações). Cores discretas, sem saturação. */
.jan { border: 0.6pt solid; border-left-width: 3pt; border-radius: 2pt;
       padding: 7pt 10pt 6pt 10pt; margin: 10pt 0 12pt 0; text-align: justify;
       page-break-inside: avoid; text-indent: 0; }
.jan p { text-indent: 0; margin: 0 0 4pt 0; }
.jan p:last-child { margin: 0; }
.jan .jrot { display:block; font-size: 10pt; font-weight: bold; letter-spacing: 0.3pt;
             text-transform: uppercase; margin: 0 0 4pt 0; }
/* qualificação da parte — outorgante/outorgado, contratante/contratado */
.jan.qualif { background:#F4F6FA; border-color:#C3CDDE; border-left-color:#1F3864;
              margin-left: 1.5cm; }
.jan.qualif .jrot { color:#1F3864; }
/* citação (dispositivo, cláusula de outro instrumento) — rótulo vira etiqueta de fonte abaixo */
.jan.cita { background:#F7F7F4; border-color:#DCDCD4; border-left-color:#6E6E62;
            margin-left: 2cm; font-family: Charter, 'Bitstream Charter', Georgia, serif;
            font-size: 11pt; display: flex; flex-direction: column; }
.jan.cita .jrot { order: 2; align-self: flex-end; margin: 5pt 0 0 0;
                  font-size: 8.5pt; font-weight: bold; text-transform: none;
                  color: #1F3864; background: #EDF1F7; border: 0.5pt solid #C3CDDE;
                  border-radius: 2pt; padding: 2pt 6pt; letter-spacing: 0.2pt; }
/* poderes / objeto — destaque sóbrio do núcleo do instrumento */
.jan.poderes { background:#F5F7FA; border-color:#CBD4E0; border-left-color:#2E5077; }

/* --- 27/08/2026: repertório unificado com o gerador de peça (ordem do Dr. Gabriel) --- */
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
.jan.poderes .jrot { color:#2E5077; }
"""


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


JANELAS = {"qualificacao": "qualif", "qualif": "qualif",
           "citacao": "cita", "cita": "cita",
           "poderes": "poderes", "objeto": "poderes",
           # 27/08/2026 — unificado com o gerador de peça:
           "linhadotempo": "tempo", "tempo": "tempo",
           "calculo": "calc", "calc": "calc",
           "doutrina": "dout", "dout": "dout",
           "sumula": "jur", "jurisprudencia": "jur", "jur": "jur"}


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

def _celulas(s):
    return [c.strip() for c in s.strip().strip("|").split("|")]


def _num(c):
    return " class='num'" if re.match(r"^\*?\*?(R\$\s*)?[\d.,%()+\-]+\*?\*?$", c.strip()) else ""


def body_to_html(body, _nivel=0):
    out, in_list = [], False
    jan_tipo, jan_rot, jan_buf = None, None, []
    tab, cap = [], None

    def close():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def flush_tab():
        nonlocal tab, cap
        if not tab: return
        linhas = [l for l in tab if not re.match(r"^\|[\s:\-|]+\|$", l)]
        # 27/08/2026 — quadro com 8 linhas ou mais quebra entre páginas, repetindo o
        # cabeçalho, em vez de abrir vão no pé da página anterior.
        out.append("<table class='q longa'>" if len(linhas) >= 8 else "<table class='q'>")
        if cap: out.append("<caption>" + inline(cap) + "</caption>")
        for i, l in enumerate(linhas):
            cs = _celulas(l)
            if i == 0:
                out.append("<thead><tr>" + "".join("<th" + _num(c) + ">" + inline(c) + "</th>" for c in cs) + "</tr></thead><tbody>")
            else:
                tot = " class='tot'" if re.search(r"(?i)\*\*(total|soma)", l) else ""
                out.append("<tr" + tot + ">" + "".join("<td" + _num(c) + ">" + inline(c) + "</td>" for c in cs) + "</tr>")
        out.append("</tbody></table>")
        tab, cap = [], None

    def fecha_janela():
        nonlocal jan_tipo, jan_rot, jan_buf
        if jan_tipo is None:
            return
        cls = JANELAS.get(jan_tipo, "qualif")
        if cls == "tempo":
            interno = eixo_do_tempo(jan_buf)
        else:
            interno = body_to_html("\n".join(jan_buf), _nivel + 1) if jan_buf else ""
        rot = ("<span class='jrot'>" + inline(jan_rot) + "</span>") if jan_rot else ""
        # 27/08/2026 — janela alta quebra entre páginas em vez de abrir vão no pé.
        _alta = (len("\n".join(jan_buf)) > 700 or "'tl longa'" in interno
                 or "'q longa'" in interno)
        out.append("<div class='jan " + cls + (" longa" if _alta else "")
                   + "'>" + rot + interno + "</div>")
        jan_tipo, jan_rot, jan_buf = None, None, []

    for line in body.split("\n"):
        s = line.strip()
        m_jan = re.match(r">\s*\[!(\w+)\]\s*(.*)", s)
        if m_jan and _nivel == 0 and m_jan.group(1).lower() in JANELAS:
            close(); fecha_janela()
            jan_tipo, jan_rot, jan_buf = m_jan.group(1).lower(), m_jan.group(2).strip(), []
            continue
        if jan_tipo is not None:
            if s.startswith(">"):
                jan_buf.append(re.sub(r"^\s*>\s?", "", line)); continue
            if s == "":
                jan_buf.append(""); continue
            fecha_janela()
        if s == "":
            close(); continue
        if s == "---" or s == "\\":
            close(); out.append("<div class='sp'></div>"); continue
        # assinatura canônica (27/08/2026)
        if s.startswith("@assinatura"):
            _cargo = s[len("@assinatura"):].strip() or "Advogado"
            out.append("<div class='assin'>"
                       "<p class='assin-nome'><strong>Gabriel Fabrízio do Espírito Santo</strong></p>"
                       "<p class='assin-cargo'>" + html.escape(_cargo) + "</p>"
                       "<p class='assin-oab'>OAB/SC 53.040</p></div>"); continue
        if s.startswith("@@ "):
            close(); out.append("<p class='center'>" + inline(s[3:].strip()) + "</p>"); continue
        if s.startswith("### "):
            close(); out.append("<h3 class='sub'>" + inline(s[4:].strip()) + "</h3>"); continue
        if s.startswith("## "):
            close(); out.append("<h2 class='clausula'>" + inline(s[3:].strip()) + "</h2>"); continue
        if s.startswith("# "):
            close(); out.append("<h1 class='titulo'>" + inline(s[2:].strip()) + "</h1>"); continue
        if s.startswith("|") and s.endswith("|"):
            tab.append(s); continue
        if tab: flush_tab()
        if s.startswith("- "):
            if not in_list:
                out.append("<ul>"); in_list = True
            out.append("<li>" + inline(s[2:].strip()) + "</li>"); continue
        close()
        cls = " class='flush'" if re.match(r"^\*\*[^*]+[:.]\*\*", s) else ""
        out.append("<p" + cls + ">" + inline(s) + "</p>")
    close()
    fecha_janela()
    if tab: flush_tab()
    return "\n".join(out)


def main():
    argv = sys.argv[1:]
    sem_logo = "--sem-logo" in argv
    sem_validacao = "--sem-validacao" in argv
    argv = [a for a in argv if a not in ("--sem-logo", "--sem-validacao")]
    if not argv:
        print("uso: python3 gerar_contrato_pdf.py CONTRATO.md [--sem-logo] [--sem-validacao]")
        sys.exit(2)
    md_path = argv[0]
    raw = open(md_path, encoding="utf-8").read()
    if raw.lstrip().startswith("---"):
        parts = raw.split("---", 2)  # remove frontmatter YAML, se houver
        if len(parts) == 3:
            raw = parts[2]
    body = raw.strip()
    # Gate de TAG CRUA (ordem do Gabriel, 19/08/2026): nenhum documento da casa sai com
    # marcacao de maquina visivel — ela denuncia confeccao por ferramenta.
    _tags = re.findall(r"<\s*/?\s*(?:br|p|div|span|b|i|u|hr|table|tr|td|th|img|a|h[1-6]|"
                       r"strong|em|ul|ol|li|blockquote|pre|code|font|center)\b[^>]*>|<!--.*?-->",
                       body, flags=re.I | re.S)
    if _tags:
        print("TAGS HTML CRUAS no markdown — o PDF sairia com elas impressas:")
        for _n, _l in enumerate(body.splitlines(), 1):
            for _t in re.findall(r"<[^>\n]{1,80}>", _l):
                if re.match(r"<\s*/?\s*(?:br|p|div|span|b|i|u|hr|table|tr|td|th|img|a|h[1-6]|"
                            r"strong|em|ul|ol|li|blockquote|pre|code|font|center)\b", _t, re.I):
                    print(f"  L{_n}: {_t}    -> {_l.strip()[:70]}")
        print("\nPDF NAO gerado. Use markdown puro — nunca tag HTML.")
        sys.exit(1)

    # Gate de norma culta (sobre o corpo que vira PDF)
    if not sem_validacao:
        validador = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "scripts", "validar_norma_culta.py")
        if os.path.exists(validador):
            chk = subprocess.run([sys.executable, validador, "--stdin", "--modo", "peca"],
                                 input=body, text=True, capture_output=True)
            if chk.returncode == 1:
                print(chk.stdout)
                print("PDF NÃO gerado: corrija os ERROS acima (ou use --sem-validacao).")
                sys.exit(1)
        else:
            print("[aviso] validar_norma_culta.py não encontrado; gerando sem gate.")

    # Logo (papel timbrado) — documento institucional leva timbre
    logo_html = ""
    logo_path = os.environ.get("GFES_LOGO", LOGO_DEFAULT)
    if not sem_logo:
        if os.path.exists(logo_path):
            logo_html = "<div class='logo'><img src='file://" + logo_path + "'></div>"
        else:
            print(f"[aviso] logo não encontrada em {logo_path}; gerando sem timbre.")
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
            "</style></head><body>" + logo_html + body_to_html(body) + "</body></html>")
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    with tempfile.TemporaryDirectory() as td:
        html_tmp = os.path.join(td, "c.html")
        pdf_tmp = os.path.join(td, "c.pdf")
        open(html_tmp, "w", encoding="utf-8").write(full)
        try:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--user-data-dir=" + os.path.join(td, "cdir"),
                            "--no-pdf-header-footer", "--print-to-pdf=" + pdf_tmp,
                            "file://" + html_tmp],
                           timeout=120, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            pass
        if not os.path.exists(pdf_tmp):
            print("ERRO: PDF não gerado")
            sys.exit(1)
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
    if os.path.exists(gate_pag) and not sem_validacao:
        chk = subprocess.run([sys.executable, gate_pag, pdf_path], capture_output=True, text=True)
        if chk.returncode == 1:
            print(chk.stdout)
            print(">>> O PDF FOI GERADO, MAS REPROVOU NO GATE DE PAGINAÇÃO. NÃO ENTREGUE ASSIM.")
            sys.exit(1)


if __name__ == "__main__":
    main()
