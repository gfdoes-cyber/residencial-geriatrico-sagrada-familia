# A casa reunida — mapa do que veio de onde (06/09/2026)

Até 05/09/2026 o trabalho da casa estava espalhado por sete branches deste mesmo repositório,
cada uma o produto de uma sessão diferente e nenhuma enxergando as outras. Em 06/09/2026 tudo o
que essas branches produziram foi copiado para cá, em duas alas separadas pelas travas.

**A reunião copiou, não moveu.** As branches de origem seguem intactas no remoto, com seu
histórico. Nada foi apagado. Quem apaga branch é o Gabriel.

---

## 1. Três coisas antes de qualquer trabalho

### 1.1 ⏰ O prazo do Ev. 25 venceu em 04/09/2026 — confirmar hoje se foi protocolado

O `CHECKLIST-PROTOCOLO.md` do caso ACP registra: **prazo fatal sexta-feira, 04/09/2026,
23h59min59s**, sob **pena de deserção**. As três peças e a procuração foram preparadas em
02/09/2026, com meta de protocolar no mesmo dia, e o preparo de **R$ 720,00** consta pago em
02/09/2026 (Ev. 31).

Não há neste material nenhum registro de protocolo: nem número de evento, nem comprovante. Isso
**não significa que o prazo foi perdido** — significa que a sessão da nuvem não tem como saber,
porque o eproc é inalcançável daqui. Estado do campo: **VAZIO**.

| Campo | Valor | Coordenada |
|---|---|---|
| Prazo final | 04/09/2026, 23h59min59s | `auditoria/CHECKLIST-PROTOCOLO.md`, linha 3 (Ev. 27) |
| Pena | deserção | idem (CPC art. 99, § 2º; Súmula 481/STJ) |
| Preparo | R$ 720,00, pago em 02/09/2026 | idem, seção A (Ev. 31) |
| Protocolo efetivado | **VAZIO — não apurável sem o eproc** | VAZIO |

**Próximo ato do Gabriel:** abrir o eproc 2º grau no processo 0900193-90.2016.8.24.0064 e ver se
o Ev. 27 está baixado e se há evento de protocolo posterior ao 32. Se foi protocolado, anotar o
número do evento aqui. Se não foi, o prazo é perdido e não se apaga: mede-se o dano (deserção da
apelação) e levanta-se o remédio, com a auditoria de preparo já pronta em
`casos/ACP-0900193-90.2016.8.24.0064/2026-09-02-cumprimento-ev25/auditoria/`.

### 1.2 🔓 Este repositório é público

Conferido em 06/09/2026 na API do GitHub: `"private": false`. O repositório
`gfdoes-cyber/residencial-geriatrico-sagrada-familia` é **público**, descrito como "Website do
Residencial Geriátrico Sagrada Família". GitHub Pages está desligado (`has_pages: false`), mas
o código-fonte é legível por qualquer pessoa e indexável.

Isso já era verdade antes desta reunião: o material dos casos foi enviado para cá pelas sessões
anteriores, em branches deste mesmo repositório público. A reunião não aumentou a exposição —
apenas a tornou visível num lugar só. O que está exposto hoje:

| O que | Onde |
|---|---|
| CPF, RG, estado civil e endereço residencial do Gabriel | `casos/ACP-.../pecas/02-procuracao-ad-judicia.md` e os `.docx`/`.pdf` ao lado |
| CNPJ, NIRE e termo de autenticação na JUCESC da Antunelli e Antunelli | idem |
| Peças, dossiê de fatos e auditoria de um processo em curso | `casos/ACP-0900193-90.2016.8.24.0064/` |
| Método interno, caderno de erros e régua tipográfica do escritório | `advocacia/tipografia-e-geradores/` |

**Decisão que é do Gabriel, e só dele.** Duas saídas, não excludentes:

1. **Tornar o repositório privado** (Settings → General → Danger Zone → Change visibility). Custo:
   se um dia o site do Residencial for publicado por Pages a partir daqui, isso precisa de plano
   pago ou de outro caminho de publicação.
2. **Separar as duas empresas em dois repositórios**, que é a decisão já registrada no `CLAUDE.md`
   da raiz: o material da advocacia (`casa/advocacia/` e `projeto-claude-espirito-santo-advocacia/`)
   vai para o repositório próprio do escritório, e este fica só com o Residencial.

Enquanto isso não acontece: **nada de `casa/advocacia/` pode ir para caminho publicado** deste
repositório — nem `index.html` da raiz, nem `CNAME`, nem workflow de Pages. Site do escritório e
site da ILPI saindo do mesmo domínio é problema das travas 1 e 3, não questão de arrumação.

> Tornar privado não apaga o passado: o que já foi enviado a um repositório público pode ter sido
> copiado ou indexado. Trocar a visibilidade reduz a exposição daqui para a frente; não a desfaz.

### 1.3 📄 O parecer do 5026537 segue retido desde 04/09/2026

`casos/5026537-50.2020.8.24.0018/PARECER-RETIDO.md` está retido porque os autos nunca chegaram, e
traz um alerta que dizia "verificar hoje" — e aquele "hoje" era 04/09. Já se passaram dois dias.
Há ainda uma divergência aberta: o link informado é do processo **5026537-50.2020.8.24.0018** e a
branch de trabalho citava **5001125**. São processos distintos, e qual é o alvo continua VAZIO.

**Próximo ato do Gabriel:** confirmar o número, e no eproc fazer *Download Completo → Baixar Todas
as Partes (ZIP)* (o link expira em 72 horas), entregando o ZIP para a leitura integral.

---

## 2. O mapa: de onde veio cada coisa

Cento e seis arquivos, de seis branches. Nenhum arquivo foi editado ao ser trazido, salvo uma
nota datada no README do caso ACP, avisando que a ferramenta de gerar DOCX e PDF mudou de pasta.

### Ala da advocacia

| Onde está agora | Arquivos | Veio de | Commit · data |
|---|---|---|---|
| `advocacia/tipografia-e-geradores/` | 33 | `claude/analise-pecas-processuais-l9f1i1` | `a7c9662` · 02/09/2026 |
| `advocacia/casos/ACP-0900193-90.2016.8.24.0064/` | 39 | `claude/auditoria-processo-judicial-tjfklb` | `0337b39` · 02/09/2026 |
| `advocacia/ferramentas-docx-pdf/` | 4 | idem (estava em `tools/`, fora de `juridico/`) | `0337b39` · 02/09/2026 |
| `advocacia/casos/5026537-50.2020.8.24.0018/` | 1 | `claude/parecer-processo-5001125-l87z4z` | `ef1ea4d` · 04/09/2026 |
| `advocacia/paginas/formacao-acp.html` | 1 | `claude/acp-especializacao-mestrado-doutorado-vyjt3n` | `9771c40` · 28/08/2026 |
| `advocacia/paginas/` (site e teleprompter) | 2 | `claude/gfes-skills-audit-13jul-ka2vbo` | `03eb3b5` · 30/07/2026 |
| `advocacia/acervo-2026-07-30/` | 5 | idem | `03eb3b5` · 30/07/2026 |

### Ala do Residencial

| Onde está agora | Arquivos | Veio de | Commit · data |
|---|---|---|---|
| `residencial/site/index.html` | 1 | `claude/oi-gmeoip` | `10d7c35` · 05/09/2026 |
| `residencial/app-ios/` | 13 | idem | `10d7c35` · 05/09/2026 |
| `residencial/documentos/` | 7 | `claude/gfes-skills-audit-13jul-ka2vbo` | `03eb3b5` · 30/07/2026 |

O `index.html` de 1 byte que cada branch carregava não foi trazido: é arquivo vazio, resíduo do
repositório original. O da branch `oi-gmeoip` é o único de verdade, com 67 KB, e está em
`residencial/site/`.

### ⚠️ O acervo de 30/07/2026 está superado — não é fonte

`advocacia/acervo-2026-07-30/` guarda o `CLAUDE.md`, o `STATUS.md` e a skill `assistente-juridico`
como estavam em 30/07/2026. Fica aqui como **história, não como regra**. Aquele texto é anterior
ao prédio único (28/08/2026), ao RADAR ÚNICO (04/09/2026) e à raiz permanente (05/09/2026); fala
em coisas que a casa revogou. Regra vigente é a do `CLAUDE.md` da raiz e a das skills em
`.claude/skills/`. Em caso de divergência, **vence o mais novo**, sempre.

---

## 3. O que continua só no Mac — e não veio

O que chegou é uma fatia do que a casa tem. A fonte única do plugin `gfes` 1.4.0 vive no vault do
Obsidian, em `Advocacia/02 - SKILLS E AGENTES/`, e a sessão da nuvem não alcança o disco do Mac.

| Não veio | Onde está |
|---|---|
| As 21 skills e os 6 agentes do plugin `gfes` 1.4.0 | fonte única no vault do Mac |
| Os 8 gates (aqui só chegaram 2: paginação e diagramação) | idem |
| O terceiro gerador na versão da regra 35, com a janela `[!linha]` | idem |
| Os 64 códigos do Planalto de `direito-civil-avancado` | idem |
| O vault inteiro: Sede, radar, índice de clientes, os outros casos | vault do Obsidian |
| A esteira de PDF e a rotina de WhatsApp | `03 - ESTEIRA/` e `rotinas/` no Mac |

**Como trazer o que falta, se for a vontade do Gabriel:** só uma sessão com mãos na máquina pode
ler o vault e enviar para cá. É a sessão de Remote Control, aberta no Mac conforme o `CLAUDE.md`
da raiz. Uma sessão da nuvem, como a que escreveu este mapa, nunca terá esse alcance.

Antes de trazer, porém, resolva o item 1.2: **enquanto este repositório for público, trazer o
vault para cá é ampliar a exposição**, não organizá-la.

---

## 4. As travas aplicadas a esta pasta

| Trava | Como ela vive aqui |
|---|---|
| ⛔ 1 — publicidade não se mistura | `advocacia/paginas/` e `residencial/site/` são alas separadas e **nenhuma das duas está publicada**. Não junte as duas num mesmo domínio, conta de anúncio ou landing. |
| 🔒 2 — dado de saúde de residente | Não há dado de saúde de residente neste material. O caso ACP tem a Antunelli como parte, não os residentes. Modelos em `residencial/documentos/` são formulários em branco: mantenha-os assim, sem preencher com pessoa real. |
| 💰 3 — contas e CNPJ não se misturam | As duas empresas aparecem aqui porque a ILPI é cliente do escritório neste processo. Isso é lícito e está declarado na procuração. O que não pode é conta, contrato, nota ou domínio comum — e é por isso que a separação em dois repositórios está no item 1.2. |

## 5. Como regenerar uma peça

Os `.md` são a fonte; `.docx` e `.pdf` são derivados. A ferramenta está em
`advocacia/ferramentas-docx-pdf/` e roda com Node mais `docx` e Playwright; `build.sh` gera ainda
os PNG de conferência com PyMuPDF.

```bash
node advocacia/ferramentas-docx-pdf/gen_docx.js <peça>.md <peça>.docx
node advocacia/ferramentas-docx-pdf/md2pdf.js   <peça>.md <peça>.pdf
```

Os geradores em Python da casa, com os gates, estão em
`advocacia/tipografia-e-geradores/instalar/skills/assistente-juridico/`. Eles dependem do Chrome e
das fontes do macOS: **a peça definitiva fecha no Mac**. Nesta nuvem só existe Liberation Serif, e
o PDF sairia com fonte substituta, reprovado no gate de paginação.

E vale aqui a regra da casa: PDF reprovado não se entrega, e conserta-se a peça, nunca o gate.
