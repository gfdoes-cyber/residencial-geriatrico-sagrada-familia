---
tipo: registro-de-sessao
predio: A — Espírito Santo Advocacia (GFES)
criado: 2026-09-02
tags: [advocacia, tipografia, regra-27, canonico, curso, gerador]
---

# 📐 02/09/2026 — Adoção dos 14 itens do curso e correção do acervo revogado

**Ordem do Gabriel:** reanalisar os dois cursos de Tipografia Jurídica aula por aula (feito de
manhã, `tipografia-juridica/00…04` no repositório), depois *"adote os 14 itens e corrija os
arquivos revogados"* e *"padrão é anotar no obsidian"*.

## O que mudou

1. **Adendo de 02/09 à regra 27** — `references/adendo-2026-09-02-adocao-dos-14-itens.md`:
   versalete nos títulos e no cabeçalho · `[!requerimentos]` na capa · numeração por `@numerar`
   · título fica em 12 · quadro de tutela em duas colunas · `[provatrio]` · `[provaquadro]` ·
   seta no `[provapar]` · marca reduzida nas páginas seguintes do parecer e do contrato ·
   "a que couber por distribuição" · revisar com intervalo · CPC 425, VI. **Capitular e
   etiqueta lateral recusados com motivo.** Um número só para o vão (20 %).
2. **`tipografia-vigente.json`** vigente desde 02/09/2026, com as chaves novas.
3. **Geradores e validadores** com o adendo implementado e **testados em Chromium com fixture
   sintética, páginas renderizadas e olhadas** (regra 26). Backups `*_pre-adendo-20260902.*.bak`
   ao lado de cada arquivo substituído.
4. **Onze arquivos que ainda ensinavam medida revogada** corrigidos, cada correção datada no
   próprio texto: `janelas-e-linha-do-tempo` (seção Tipografia reescrita), `forma-da-peticao`
   E.1.5, `checklist-universal` 1.10 (skill `requisitos-das-pecas`), `metodo-das-pecas` passo 5,
   `tipografia-e-design` cabeçalho, as notas do vault *Cláusula pétrea — marca do advogado* (b) e
   *Padrão visual 27-08*, a nota *Tipografia Jurídica* de 07/05 (banner de revogação),
   `padrao-formatacao-peca` e `tipografia-pecas-14-08` (banner de histórico) e a `SKILL.md` da
   `assistente-juridico` (duas linhas).

## O que fica pendente (dito, não escondido)

- **`recorte --tracejado`** (item 3.10-b): o `recorte` é Swift e compila só no Mac.
- **Os dez modelos de peça** de `requisitos-das-pecas/assets/modelos/` ainda não usam
  `[!requerimentos]` nem o quadro de tutela em duas colunas — não estavam no espelho lido;
  atualizar no Mac com o esboço do arquivo `03`.
- **RISTJ, art. 343-A**: continua `[VERIFICAR]` na fonte oficial antes de citar ao STJ.
- **Primeiro PDF real** depois da instalação: olhar página a página (o teste aqui foi com
  Liberation Serif, porque a máquina de teste não tem Times).

## Onde está e como instalar

Repositório `gfdoes-cyber/residencial-geriatrico-sagrada-familia`, branch
`claude/analise-pecas-processuais-l9f1i1`, pasta `tipografia-juridica/instalar/`. No Mac:
`bash tipografia-juridica/instalar/instalar.sh` — copia para o vault (`Advocacia/`) e para as
skills, com backup datado; não apaga nada.

## Rodapé de prédio

Prédio A. Nenhum caso real tocado; fixtures sintéticas; nada protocolado; espelho do Drive
não editado. Quem atendeu: a banca, para a Lourdes.
