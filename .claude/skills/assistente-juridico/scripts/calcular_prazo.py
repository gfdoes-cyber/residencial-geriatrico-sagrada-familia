#!/usr/bin/env python3
"""Calculadora de prazos processuais — GFES.

Implementa os marcos iniciais da Resolução CNJ 569/2024 (vigente desde
16/05/2025) e a contagem do CPC (dias úteis, art. 219) / CPP (dias corridos,
art. 798). Feriados NÃO estão embutidos: passar via --feriados AAAA-MM-DD,...

Canais (--canal):
  djen                          intimação a advogado via DJEN:
                                publicação = 1º dia útil após a disponibilização;
                                prazo inicia no 1º dia útil seguinte à publicação.
  domicilio_confirmada          citação confirmada no Domicílio: prazo inicia no
                                5º dia útil após a data da LEITURA (--data é a leitura).
  domicilio_nao_confirmada_pj_publica
                                citação não confirmada, PJ de direito público:
                                ciência tácita em 10 dias corridos do ENVIO;
                                prazo inicia no 1º dia útil seguinte.
  domicilio_intimacao_nao_confirmada
                                demais intimações sem confirmação: ciência tácita
                                em 10 dias corridos do envio; prazo inicia no 1º
                                dia útil seguinte.
  direto                        (default) --data já é o termo inicial informado;
                                prazo inicia no 1º dia útil seguinte.

Obs.: citação NÃO confirmada de PJ de direito PRIVADO não inicia prazo
(citação deve ser refeita + justificativa, sob pena de multa) — o script
recusa esse cenário de propósito.

Exemplos:
  calcular_prazo.py --data 2026-07-02 --dias 15 --canal djen
  calcular_prazo.py --data 2026-07-10 --dias 15 --canal domicilio_confirmada
  calcular_prazo.py --data 2026-07-01 --dias 10 --canal domicilio_nao_confirmada_pj_publica
  calcular_prazo.py --data 2026-07-06 --dias 5 --corridos          # CPP
"""
import argparse
import sys
from datetime import date, timedelta


def eh_util(d: date, feriados: set) -> bool:
    return d.weekday() < 5 and d not in feriados


def proximo_util(d: date, feriados: set) -> date:
    while not eh_util(d, feriados):
        d += timedelta(days=1)
    return d


def soma_uteis(d: date, n: int, feriados: set) -> date:
    """n-ésimo dia útil APÓS d (exclui d)."""
    c = 0
    while c < n:
        d += timedelta(days=1)
        if eh_util(d, feriados):
            c += 1
    return d


def contar(termo_inicial: date, dias: int, corridos: bool, feriados: set) -> date:
    """Conta o prazo a partir do termo inicial (dia em que o prazo COMEÇA a
    correr, incluído na contagem), devolvendo o vencimento.
    Exclui-se o dia do começo e inclui-se o do vencimento (CPC art. 224):
    aqui o termo_inicial já é o 1º dia de contagem."""
    if corridos:
        venc = termo_inicial + timedelta(days=dias - 1)
        return proximo_util(venc, feriados)  # prorroga se cair em dia não útil
    d, c = termo_inicial, 1 if eh_util(termo_inicial, feriados) else 0
    while c < dias:
        d += timedelta(days=1)
        if eh_util(d, feriados):
            c += 1
    return d


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", required=True,
                    help="AAAA-MM-DD — significado depende do canal (disponibilização, leitura ou envio)")
    ap.add_argument("--dias", type=int, required=True, help="tamanho do prazo")
    ap.add_argument("--canal", default="direto",
                    choices=["djen", "domicilio_confirmada",
                             "domicilio_nao_confirmada_pj_publica",
                             "domicilio_intimacao_nao_confirmada", "direto"])
    ap.add_argument("--corridos", action="store_true",
                    help="contar o prazo em dias corridos (CPP art. 798); default: dias úteis (CPC art. 219)")
    ap.add_argument("--feriados", default="",
                    help="lista AAAA-MM-DD separada por vírgula")
    a = ap.parse_args()

    d0 = date.fromisoformat(a.data)
    fer = {date.fromisoformat(x) for x in a.feriados.split(",") if x.strip()}
    log = []

    if a.canal == "djen":
        pub = proximo_util(d0 + timedelta(days=1), fer)
        termo = proximo_util(pub + timedelta(days=1), fer)
        log += [f"Disponibilização no DJEN: {d0}", f"Publicação (1º útil seguinte): {pub}",
                f"Termo inicial (1º útil após a publicação): {termo}"]
    elif a.canal == "domicilio_confirmada":
        quinto = soma_uteis(d0, 5, fer)
        termo = quinto
        log += [f"Leitura/confirmação no Domicílio: {d0}",
                f"Termo inicial (5º dia útil após a leitura): {termo}"]
    elif a.canal in ("domicilio_nao_confirmada_pj_publica",
                     "domicilio_intimacao_nao_confirmada"):
        tacita = d0 + timedelta(days=10)
        termo = proximo_util(tacita + timedelta(days=1), fer)
        log += [f"Envio pelo Domicílio: {d0}", f"Ciência tácita (10 dias corridos): {tacita}",
                f"Termo inicial (1º útil seguinte): {termo}"]
    else:
        termo = proximo_util(d0 + timedelta(days=1), fer)
        log += [f"Marco informado: {d0}", f"Termo inicial (1º útil seguinte): {termo}"]

    venc = contar(termo, a.dias, a.corridos, fer)
    modo = "corridos (CPP 798)" if a.corridos else "úteis (CPC 219)"
    log.append(f"Prazo de {a.dias} dias {modo} → VENCIMENTO: {venc} ({venc.strftime('%A')})")
    print("\n".join(log))
    if a.canal == "direto":
        print("[!] Canal 'direto': confirme se o marco não deveria ser DJEN/Domicílio (Res. CNJ 569/2024).")


if __name__ == "__main__":
    if "--pj-privada-nao-confirmada" in sys.argv:
        sys.exit("Citação de PJ de direito privado NÃO confirmada: prazo NÃO se inicia "
                 "(citação refeita + justificativa, sob pena de multa) — Res. CNJ 569/2024.")
    main()
