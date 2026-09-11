# Consumo de tokens — linha de base para conferir amanhã

Marcada em **08/09/2026, ~22h43 UTC** (19h43 em Florianópolis). Nada foi alterado na
configuração de propósito: o objetivo é ver, em 09/09, se o consumo sobe sozinho durante a
noite. Se subir sem sessão aberta, a causa não é nenhuma das abaixo e precisa ser investigada
com o suporte.

## Cotas no momento da marcação (relato do Gabriel)

- **Fable: 23% consumido**
- **Semanal: 19% consumido**

## Estado verificado da conta

| O que | Estado |
|---|---|
| Rotinas ativas (`list_triggers enabled=true`) | **nenhuma** — lista vazia |
| Rotina "Vigia DJEN 5007704" | desativada em 25/08; não pôde ser apagada pelo agente (criada via API HTTP), pendente de exclusão manual |
| Sessões em execução | **uma**: "Consumo de tokens sem uso" (esta) |
| Sessão "Claude no Xcode" | IDLE desde 08/09 01h20 — não consome |
| Sessão "Ecossistema da casa" | arquivada em 08/09 |

## Custo já apurado

| Sessão | Contexto | Tokens | Custo |
|---|---|---|---|
| Ecossistema da casa (05–07/09), `xhigh` + ultracode | 423.326 | ~231,6 mi | US$ 249,44 |
| Claude no Xcode (07–08/09), `low` | 143.890 | ~13,8 mi | US$ 17,94 |
| Esta sessão, 4 mensagens em 3h15, `xhigh` + ultracode | 95.557 | ~608 mil | US$ 1,42 |

Média desta sessão: **~152 mil tokens por mensagem**.

## Hipótese a testar

Nada consome em segundo plano; o gasto é por turno e a configuração `xhigh` + ultracode é o
multiplicador. **Se amanhã as cotas estiverem nos mesmos 23% / 19%, a hipótese se confirma** e
o remédio é configuração (esforço `low`, ultracode desligado, conectores não usados
desconectados, sessões curtas). Se tiverem subido com a conta parada, a hipótese cai.
