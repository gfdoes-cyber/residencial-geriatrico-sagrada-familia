#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE DE PAGINAÇÃO E TIPOGRAFIA (27/08/2026) — Prédio A, Espírito Santo Advocacia.

Roda sobre o PDF JÁ GERADO e REPROVA o que a regra da casa proíbe:
  - página em branco ou subocupada (buraco de janela indivisível);
  - linha ÓRFÃ (última linha de um parágrafo sozinha no topo da página);
  - linha VIÚVA (primeira linha de um parágrafo sozinha no pé da página);
  - título de seção no pé da página, separado do texto que abre;
  - última página com só o fecho e a assinatura;
  - divergência das MEDIDAS (fonte, corpo, entrelinha, margens, recuos) contra
    references/tipografia-vigente.json, que é a fonte única de verdade.

POR QUE ELE EXISTE (ordem do Gabriel em 27/08/2026: "anote para não haver mais erros"):
numa mesma peça a casa (a) declarou "conforme a regra canônica" um PDF que media valores
JÁ REVOGADOS — porque conferiu contra a memória, e não contra a camada mais nova da regra —
e (b) entregou petição com três títulos órfãos, uma página a 43% e uma página final com só
sete linhas, porque conferiu apenas a última página. Anotação não impede erro; gate impede.

Uso:
  validar_paginacao.py peca.pdf            reprova com código 1 se houver ERRO
  validar_paginacao.py peca.pdf --so-aviso nunca reprova (só informa)
  validar_paginacao.py peca.pdf --json     saída em JSON

Limite honesto: mede o que o PDF É. Se o CSS e o tipografia-vigente.json divergirem da regra
escrita, o gate acusa a divergência entre eles — mas quem decide qual está certo é o Gabriel.
"""
import json, os, sys

CFG = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "references", "tipografia-vigente.json")
CM = 28.3465  # pt por cm


def carrega_cfg():
    try:
        with open(CFG, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as e:
        print("[aviso] tipografia-vigente.json ilegível (%s); medidas não conferidas." % e)
        return None


def linhas_da_pagina(p):
    out = []
    for b in p.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            txt = " ".join(s["text"] for s in l["spans"]).strip()
            if txt:
                s = l["spans"][0]
                # 27/08/2026 — a linha inteira é negrito? Só o primeiro span não basta:
                # parágrafo do corpo que ABRE com destaque em negrito era lido como
                # título e reprovava a peça sem defeito (falso positivo medido na
                # defesa 5013466, p. 10, em "esclarecer e a identificar o terceiro").
                todo_bold = all("Bold" in sp["font"] for sp in l["spans"]
                                if sp["text"].strip())
                out.append({"y0": l["bbox"][1], "y1": l["bbox"][3], "x0": l["bbox"][0],
                            "x1": l["bbox"][2], "txt": txt, "fonte": s["font"],
                            "todo_bold": todo_bold, "cor": s.get("color", 0),
                            "sz": round(s["size"], 1)})
    out.sort(key=lambda d: d["y0"])
    return out


def eh_titulo(l):
    return (l["fonte"].endswith("BoldMT") and l["sz"] == 12
            and l.get("todo_bold", True)
            and len(l["txt"]) < 95 and not l["txt"].rstrip().endswith((".", ";", ":", ",")))


def main():
    try:
        import fitz
    except ImportError:
        print("[aviso] PyMuPDF ausente; gate de paginação não rodou.")
        return 0

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    pdf = args[0]
    so_aviso = "--so-aviso" in sys.argv
    saida_json = "--json" in sys.argv

    cfg = carrega_cfg()
    d = fitz.open(pdf)
    H, W = d[0].rect.height, d[0].rect.width
    m = (cfg or {}).get("margens_cm", {"superior": 3.0, "inferior": 2.0})
    topo = m["superior"] * CM
    pe = H - m["inferior"] * CM
    util = pe - topo

    erros, avisos = [], []
    paginas = [linhas_da_pagina(p) for p in d]
    n = len(paginas)

    # ---------- paginação ----------
    pg = (cfg or {}).get("paginacao", {})
    # 02/09/2026: um número só para o vão — ocupação mínima = 100 − vão máximo (item 5.1).
    ocup_min = 100 - pg.get("vao_maximo_pct", 100 - pg.get("ocupacao_minima_pct", 70))
    ult_min = pg.get("ultima_pagina_linhas_minimas", 8)

    for i, L in enumerate(paginas, 1):
        if not L:
            erros.append("pág. %d: PÁGINA EM BRANCO" % i); continue
        ocup = (L[-1]["y1"] - L[0]["y0"]) / util * 100
        if i < n and ocup < ocup_min:
            erros.append("pág. %d: SUBOCUPADA (%.0f%%, mínimo %d%%) — buraco, provavelmente "
                         "janela/figura indivisível que não coube" % (i, ocup, ocup_min))
        if i < n and eh_titulo(L[-1]):
            erros.append("pág. %d: TÍTULO NO PÉ, separado do texto que abre — \"%s\""
                         % (i, L[-1]["txt"][:60]))

    if paginas and len(paginas[-1]) < ult_min:
        erros.append("pág. %d (última): só %d linhas — fecho/assinatura quase sozinhos "
                     "(mínimo %d; seção 7 da canônica de 24/08)"
                     % (n, len(paginas[-1]), ult_min))

    for i in range(1, n):
        L = paginas[i]
        if len(L) >= 2:
            a, b = L[0], L[1]
            if (a["txt"].rstrip().endswith((".", ";")) and b["y0"] - a["y1"] > 4
                    and len(a["txt"]) < 78 and a["sz"] == 12):
                erros.append("pág. %d: LINHA ÓRFÃ no topo — \"%s\"" % (i + 1, a["txt"][:60]))

    for i in range(0, n - 1):
        L = paginas[i]
        if len(L) >= 2:
            u, ant = L[-1], L[-2]
            if (u["y0"] - ant["y1"] > 4 and u["sz"] == 12
                    and not u["txt"].rstrip().endswith((".", ";", ":")) and not eh_titulo(u)):
                erros.append("pág. %d: LINHA VIÚVA no pé — \"%s\"" % (i + 1, u["txt"][:60]))

    # ---------- medidas ----------
    if cfg:
        from collections import Counter
        xs, xr, ys, cit, fontes = [], [], [], [], Counter()
        for L in paginas:
            prev = None
            for l in L:
                fontes[(l["fonte"], l["sz"])] += len(l["txt"])
                if l["fonte"].startswith("TimesNewRoman") and l["sz"] == 12:
                    xs.append(round(l["x0"], 1)); xr.append(round(l["x1"], 1))
                    if prev is not None and 0 < l["y0"] - prev < 40:
                        ys.append(round(l["y0"] - prev, 1))
                    prev = l["y0"]
                if l["fonte"].startswith("Charter") and l["sz"] == 11:
                    cit.append(round(l["x0"], 1))
        tol = cfg.get("tolerancia_cm", 0.10)

        def cmp_cm(nome, medido_cm, esperado_cm):
            if abs(medido_cm - esperado_cm) > tol:
                erros.append("MEDIDA %s: %.2f cm — esperado %.2f cm (tipografia-vigente.json)"
                             % (nome, medido_cm, esperado_cm))

        if xs:
            esq = Counter(xs).most_common(1)[0][0]
            cmp_cm("margem esquerda", esq / CM, cfg["margens_cm"]["esquerda"])
            cmp_cm("margem direita", (W - max(xr)) / CM, cfg["margens_cm"]["direita"])
            rec = Counter([x for x in xs if x > esq + 20]).most_common(1)
            if rec:
                cmp_cm("recuo de 1ª linha", (rec[0][0] - esq) / CM, cfg["recuo_1a_linha_cm"])
            if cit:
                cmp_cm("recuo da citação", (Counter(cit).most_common(1)[0][0] - esq) / CM,
                       cfg["citacao"]["recuo_cm"])
        if ys:
            el = Counter(ys).most_common(1)[0][0]
            esp = cfg["entrelinha"]["pt_esperado"]
            if abs(el - esp) > cfg["entrelinha"].get("tolerancia_pt", 0.8):
                erros.append("MEDIDA entrelinha: %.1f pt (fator %.2f) — esperado %.1f pt "
                             "(fator %.2f)" % (el, el / 12, esp, cfg["entrelinha"]["fator"]))
        if fontes:
            (f, sz), _ = fontes.most_common(1)[0]
            if not f.startswith("TimesNewRoman") or sz != cfg["corpo"]["tamanho_pt"]:
                erros.append("MEDIDA corpo: %s %.0f pt — esperado %s %d pt"
                             % (f, sz, cfg["corpo"]["fonte"], cfg["corpo"]["tamanho_pt"]))
            if cit and not any(f2.startswith("Charter") for (f2, _s) in fontes):
                avisos.append("citação não está em Charter")

    # ---------- saída ----------
    if saida_json:
        print(json.dumps({"pdf": pdf, "paginas": n, "erros": erros, "avisos": avisos},
                         ensure_ascii=False, indent=1)); return 1 if erros and not so_aviso else 0

    print("GATE DE PAGINAÇÃO E TIPOGRAFIA — %s (%d páginas)" % (os.path.basename(pdf), n))
    if cfg:
        print("Régua: tipografia-vigente.json, vigente desde %s" % cfg.get("vigente_desde"))
    if erros:
        print("\nERROS — bloqueiam (%d):" % len(erros))
        for e in erros: print("    " + e)
    if avisos:
        print("\nAVISOS (%d):" % len(avisos))
        for a in avisos: print("    " + a)
    print("\nRESUMO: %d erro(s), %d aviso(s)." % (len(erros), len(avisos)))
    if erros and not so_aviso:
        print("VEREDITO: BLOQUEADO. Petição não sai com linha órfã, viúva ou página em branco.")
        print("Ordem para fechar buraco: %s" % " · ".join(
            (cfg or {}).get("ordem_para_fechar_buraco", [])))
        return 1
    print("VEREDITO: LIBERADO." if not erros else "VEREDITO: erros rebaixados a aviso (--so-aviso).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
