# Reanálise dos dois cursos de Tipografia Jurídica — índice (02/09/2026)

> **Ordem do Gabriel (02/09/2026):** pegar os dois cursos da conta de aluno
> (`aluno.tipografiajuridica.com.br`, produto 2468122) com **todas as legendas**, conferir
> antes o que o vault já tem para não repetir trabalho, analisar **aula por aula, todo o
> material e todos os modelos de peça**, produzir os **esboços de formatação das peças do
> escritório** com base nas aulas e **ligar cada esboço à lei**. Motivo declarado: *"não sei
> se passou batido alguma coisa e quero aproveitar cada caractere"*. Reforço na mesma
> conversa: *"são dois cursos, masterclass e printscreen, eles têm que ser absorvidos"*.

## 0. Estado em 02/09/2026, à tarde — ordem cumprida: "adote os 14 itens e corrija os arquivos revogados"

Os 14 itens do arquivo `02`, item 3, foram **adotados** (12 implementados; capitular e etiqueta
lateral recusados com motivo, como proposto) e as **nove entradas com medida revogada** do
item 4 foram **corrigidas**. Tudo está em `instalar/`: geradores e validadores com o adendo
(testados em Chromium com fixture sintética e páginas olhadas), `tipografia-vigente.json`
vigente desde 02/09, a regra canônica `adendo-2026-09-02-adocao-dos-14-itens.md`, os onze
arquivos corrigidos e a nota de sessão do vault. **Como o padrão da casa é anotar no Obsidian e
o vault mora no Mac** (o Drive é espelho, não se edita), o registro entra no vault pelo
`instalar/instalar.sh`, que copia com backup datado e não apaga nada.

## 1. O que está nesta pasta

| Arquivo | O que é | Para que serve |
|---|---|---|
| `01-aula-por-aula.md` | Os 13 vídeos, os 3 PDFs e os 20 `.docx`, um a um: o que ensinam, o que a casa já tem, o que ficou de fora | Prova de que nada passou batido |
| `02-auditoria-de-lacunas.md` | Confronto de cada regra do curso com a régua vigente; lacunas reais; contradições internas do acervo; decisões que só o Gabriel pode tomar | Lista de trabalho |
| `03-esbocos-por-peca.md` | Os esboços tipográficos de 16 peças/documentos do escritório, bloco a bloco, com o elemento do curso adotado e o dispositivo legal de cada bloco | Usar ao redigir |
| `04-ligacao-legal.md` | A matriz regra de forma ↔ norma, com o texto dos artigos conferido na cópia do CPC que a casa baixou do Planalto | Fundamentar a forma quando alguém a questionar |
| `instalar/` | Adendo canônico de 02/09, geradores e validadores corrigidos, os 11 arquivos revogados corrigidos, nota do vault, fixtures e `instalar.sh` | Instalar no Mac (vault + skills) com backup datado |

## 2. Honestidade sobre a fonte (regra 22)

- **A plataforma do curso não foi aberta nesta sessão.** O ambiente de execução bloqueia o
  domínio `aluno.tipografiajuridica.com.br` (o proxy devolve `403` ao `CONNECT`) e também
  bloqueia `planalto.gov.br`. Nada foi baixado de novo da conta de aluno.
- **O que foi lido, na íntegra:** as **13 transcrições oficiais** (faixa de legenda
  `textstream_pt_br`, baixadas pela casa em 27/08/2026, 55.485 palavras), os **3 PDFs de
  apoio** (texto extraído), a **transcrição e medição dos 20 `.docx`** feita em 30/08/2026,
  e **41 arquivos de regra e nota** da casa sobre o tema (referências da skill
  `assistente-juridico`, notas do vault migradas ao Notion, `tipografia-vigente.json`,
  checklists da skill `requisitos-das-pecas`). Tudo foi obtido do espelho do vault no Google
  Drive (`Cerebro-Vault-Obsidian`), **somente leitura** — o espelho não foi editado.
- **A lei foi conferida na cópia que a casa mantém em disco** (`codigos/cpc-2015.txt`,
  `lei-8906-1994-estatuto-advocacia.txt`, `lei-11419-2006-processo-eletronico.txt`, baixadas
  do Planalto pela casa). Onde este trabalho cita artigo, o texto foi lido nessa cópia em
  02/09/2026 e está marcado `[conferido: acervo da casa]`. O que não foi lido está marcado
  `[VERIFICAR]`.
- **O que não existe em lugar nenhum e portanto não foi analisado:** vídeo da página
  "Modelos v2" (é página de download, sem vídeo) e a legenda do vídeo promocional da fonte
  Dupincel (não tem faixa de legenda; é oferta comercial, não método). A casa já havia
  registrado as duas ausências em 27/08/2026 e esta reanálise as confirma.

## 3. O que esta reanálise conclui, em uma página

1. **A régua da casa não muda.** Nenhuma medida de `tipografia-vigente.json` (Times 12,
   Charter 11 a 3 cm, entrelinha 1,35, 3+3 cm, 2,3/1,8 cm, recuo 2 cm) é contrariada pelo
   curso; onde diverge, a divergência já está registrada com data e motivo. O curso prescreve
   **princípios** (linha curta, entrelinha ajustada à fonte, um só marcador de parágrafo,
   citação só por recuo e corpo menor) e a casa mediu os **valores** para a própria fonte.
2. **Passou batido pouco, mas passou.** A varredura achou **14 itens do curso sem posição escrita, sem ferramenta
   ou sem fundamento registrado na casa** (item 3 do arquivo `02`); os 11 de forma são: versalete, quadro de
   requerimentos preliminares com caixas de seleção, capitular, etiqueta lateral de lei,
   numeração automática de seções, título um ponto maior que o corpo, quadro de tutela em duas
   colunas, série de três imagens com legenda única, quadro de apoio ao lado do documento,
   seta ligando página e zoom, marca reduzida nas páginas seguintes do parecer.
3. **O acervo da casa tem nove entradas (dez arquivos) que ainda ensinam medida revogada**
   (item 4 do arquivo `02`). Uma já era pendência desde 30/08; as outras oito são novas. Nenhum foi
   alterado aqui, porque são canônicos e a correção é ato de quem os editou.
4. **Dois números da própria régua se contradizem** (ocupação mínima 70 % no JSON contra vão
   máximo 20 % na regra 1-B) e **uma citação regimental continua sem fonte oficial**
   (RISTJ, art. 343-A). Ambos estão no arquivo `02`, item 5.
5. **Os esboços** (arquivo `03`) não reinventam a peça: fixam, para cada uma das 16
   peças/documentos, a ordem dos blocos, o elemento visual de cada bloco, a medida da casa
   e o dispositivo que exige o bloco — com o texto legal conferido no arquivo `04`.

## 4. Como usar

- **Antes de redigir uma peça:** abrir o esboço dela em `03` e o checklist da skill
  `requisitos-das-pecas` (a lei); a tipografia é aplicada pelo gerador a partir do JSON.
- **Antes de mexer na régua:** ler `02`, itens 3 a 5, e decidir por escrito o que entra.
- **Quando alguém questionar a forma da peça:** `04` responde com o artigo.

## 5. Fontes desta pasta (todas em somente leitura)

Transcrições `MASTER-*` e `PRINT-*` (13) · `Formatando Petições com Excelência.pdf` ·
`Material de apoio - Luciana Petri.pdf` · `Material de apoio - Printscreen de impacto.pdf` ·
`modelos-docx-masterclass-transcritos-2026-08-30.md` · `regra-geral-de-formatacao-2026-08-27.md` ·
`tipografia-vigente.json` · `ficha-tecnica-tipografia-da-casa-2026-08-27.md` ·
`masterclass-transcrita-passo-a-passo-2026-08-27.md` · `caderno-de-erros-da-casa-2026-08-27.md` ·
`janelas-e-linha-do-tempo-2026-08-27.md` · `vao-no-pe-da-pagina-2026-08-27.md` ·
`prova-visual-e-conferencia-2026-08-27.md` · `printscreens-de-impacto-2026-08-27.md` ·
`redacao-objetiva-guia-petri-2026-08-27.md` · `forma-da-peticao-2026-08-26.md` ·
`padrao-formatacao-peca-2026-08-20.md` · `tipografia-e-design-da-informacao-2026-08-24.md` ·
`tipografia-pecas-2026-08-14.md` · `tipos-de-peca.md` · `metodo-das-pecas.md` · `citacao-abnt.md` ·
`compliance-e-rodape.md` · `norma-culta.md` · `checklist-universal.md` · `checklist-por-peca.md` ·
`cpc-inicial.md` · `consequencias-e-erros.md` · `00-LEIA-ME.md` (modelos da casa) ·
`codigos/cpc-2015.txt` · `codigos/lei-8906-1994-estatuto-advocacia.txt` ·
`codigos/lei-11419-2006-processo-eletronico.txt` · e as 12 notas do vault/Notion datadas de
07/05, 15/08, 27/08 (×7), 28/08, 29/08, 30/08 e 31/08/2026.
