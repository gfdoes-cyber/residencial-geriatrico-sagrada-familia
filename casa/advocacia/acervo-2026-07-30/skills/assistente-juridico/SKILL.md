---
name: assistente-juridico
description: Método GFES para qualquer consulta jurídica, análise de processo ou cálculo de prazo. Usar SEMPRE que a tarefa envolver lei, súmula, precedente, prazo processual, DJEN/Domicílio Judicial Eletrônico ou petição. Contém protocolo antialucinação, fontes oficiais e o script calcular_prazo.py.
---

# Assistente Jurídico GFES (versão nuvem)

## Protocolo antialucinação (obrigatório)

1. Nenhuma norma, súmula ou precedente entra em documento sem leitura na fonte
   oficial NA sessão, com URL + data de acesso. Se a rede bloquear a fonte
   (`.jus.br` costuma estar bloqueado na nuvem), rotular [NÃO VERIFICADO] e
   listar como pendência de conferência local — nunca fingir verificação.
2. Rotular toda afirmação relevante: [VERIFICADO] / [INFERÊNCIA] / [NÃO VERIFICADO].
3. Legislação: sempre na versão COMPILADA do Planalto.
4. Súmula: conferir a redação vigente no portal na data da peça (ver regra da
   Súmula 545/STJ no CLAUDE.md).

## Prazos — marcos iniciais (Resolução CNJ 569/2024, vigente desde 16/05/2025)

Comunicações fora de DJEN/Domicílio (eproc, PJe, portais) são meramente informativas.

- **DJEN** (intimações a advogados): publicação = dia útil seguinte à
  disponibilização; prazo inicia no 1º dia útil seguinte à publicação
  (CPC art. 224 §§1º-2º).
- **Domicílio Judicial Eletrônico:**
  - citação confirmada → prazo inicia no 5º dia útil após a leitura;
  - citação NÃO confirmada → PJ de direito público: 10 dias corridos do envio;
    PJ de direito privado: prazo NÃO se inicia (citação refeita + justificativa,
    sob pena de multa);
  - demais intimações sem confirmação → 10 dias corridos do envio.
- MP, advocacia pública e Defensoria: sempre via Domicílio (intimação pessoal).
- Processo penal: prazos em dias corridos (CPP art. 798); processo civil: dias
  úteis (CPC art. 219).

**Cálculo sempre pelo script:** `scripts/calcular_prazo.py` (ver `--help`).
Feriados não estão embutidos — passar via `--feriados` quando souber.

## Fontes oficiais

Ver `references/fontes-oficiais.md` (portais por tribunal, regra do portal novo
do TJSC, regulatório ILPI).

## Saída padrão de pesquisa de jurisprudência

Separar em: favoráveis / contrários / vinculantes (súmula, repetitivo, RG).
Acórdão do TJSC pós-08/10/2025: SÓ no portal novo (eproc); o antigo é base
histórica até essa data.
