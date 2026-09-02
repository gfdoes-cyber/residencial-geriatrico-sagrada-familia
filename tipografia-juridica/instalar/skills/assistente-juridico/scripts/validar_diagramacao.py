#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE DE DIAGRAMAÇÃO — mede o VÃO NO PÉ de cada página do PDF já gerado.

Ordem do Dr. Gabriel, 27/08/2026: *"final de algumas páginas continua um espaço em branco,
quase que quarenta por cento da página. Formatação está horrível, você tem que arrumar
isso."* — e, antes, na regra 26: *"não deixe passar essa falha em nenhuma das peças"*.

Por que existe: medir a última página (assinatura órfã) NÃO pega este defeito. O vão nasce
no MEIO do documento, quando um bloco alto e indivisível (janela, quadro, linha do tempo,
figura de prova) não cabe no resto da folha e é empurrado inteiro para a página seguinte.

Uso:  python3 validar_diagramacao.py <arquivo.pdf> [--limite 20]
Saída: linha por página com o vão; código 1 se alguma página reprovar.
A ÚLTIMA página é isenta (o fim do texto é o fim do texto). Página que contenha apenas
uma imagem de página inteira também é isenta.
"""
import sys, os

LIMITE_PADRAO = 20.0     # % da mancha útil que pode ficar vazia no pé
CM = 28.3465             # pontos por centímetro (72 dpi)
# 02/09/2026 (item 5.1 da reanálise): limite e margens vêm de tipografia-vigente.json — fonte
# única das medidas. Antes, este gate media com margens 3,0/2,0 (revogadas em 27/08) e o JSON
# dizia "ocupação mínima 70 %" enquanto aqui valia "vão ≤ 20 %". Um número só.
import json
CFG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "tipografia-vigente.json")
def _cfg():
    try:
        with open(CFG, encoding="utf-8") as fh: return json.load(fh)
    except Exception:
        return {}


def medir(pdf_path, limite=None, margem_sup=None, margem_inf=None):
    cfg = _cfg()
    if limite is None:
        limite = float(cfg.get("paginacao", {}).get("vao_maximo_pct", LIMITE_PADRAO))
    if margem_sup is None:
        margem_sup = float(cfg.get("margens_cm", {}).get("superior", 3.0))
    if margem_inf is None:
        margem_inf = float(cfg.get("margens_cm", {}).get("inferior", 2.0))
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("[aviso] PyMuPDF ausente; gate de diagramação não rodou.")
        return [], True

    doc = fitz.open(pdf_path)
    total = doc.page_count
    linhas, ok = [], True

    for n, pag in enumerate(doc):
        altura = pag.rect.height
        pe = altura - margem_inf * CM                 # onde a mancha termina
        mancha = altura - (margem_sup + margem_inf) * CM

        ymax = 0.0
        for b in pag.get_text("blocks"):
            if b[4].strip() and b[3] > ymax:
                ymax = b[3]
        for im in pag.get_images(full=True):
            try:
                r = pag.get_image_bbox(im)
                if r.y1 > ymax:
                    ymax = r.y1
            except Exception:
                pass

        if ymax == 0:                                  # página vazia de conteúdo
            linhas.append((n + 1, 100.0, 0.0, "PÁGINA VAZIA"))
            ok = False
            continue

        vao_pt = max(0.0, pe - ymax)
        pct = vao_pt / mancha * 100.0
        ultima = (n == total - 1)
        reprova = (pct > limite) and not ultima
        if reprova:
            ok = False
        linhas.append((n + 1, pct, vao_pt / CM,
                       "REPROVA" if reprova else ("última página" if ultima else "ok")))

    return linhas, ok


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    pdf = sys.argv[1]
    limite = None
    if "--limite" in sys.argv:
        limite = float(sys.argv[sys.argv.index("--limite") + 1])
    if not os.path.exists(pdf):
        print("arquivo não encontrado:", pdf)
        sys.exit(2)

    linhas, ok = medir(pdf, limite)
    if not linhas:
        sys.exit(0)

    ruins = [l for l in linhas if l[3] == "REPROVA"]
    if limite is None:
        limite = float(_cfg().get("paginacao", {}).get("vao_maximo_pct", LIMITE_PADRAO))
    print("GATE DE DIAGRAMAÇÃO — vão no pé da página (limite %.0f%%)" % limite)
    for n, pct, cm, st in linhas:
        marca = "  <<<< REPROVA" if st == "REPROVA" else ""
        print("  p.%-3d %5.1f%%  (%.1f cm)%s" % (n, pct, cm, marca))
    if ruins:
        print("\n%d página(s) com vão acima do limite: %s"
              % (len(ruins), ", ".join("p." + str(l[0]) for l in ruins)))
        print("CAUSA típica: bloco alto e indivisível empurrado inteiro para a folha "
              "seguinte (janela, quadro, linha do tempo ou figura de prova), às vezes "
              "grudado a um título com break-after: avoid.")
        print("CONSERTO: deixar o bloco quebrar entre páginas (classe .longa), reduzir a "
              "altura da imagem, ou mover o bloco para outro ponto do texto.")
        sys.exit(1)
    print("\nOK — nenhuma página com vão acima do limite.")
    sys.exit(0)


if __name__ == "__main__":
    main()
