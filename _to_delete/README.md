# `_to_delete/` — a lixeira que não apaga

A casa não apaga nada em definitivo. Quando um arquivo deixa de servir, ele **não** é removido:
move-se para cá, com o nome original preservado e um sufixo datado se houver colisão.

```bash
mv <arquivo> _to_delete/<arquivo>.saiu-20260906
```

Ao mover, acrescente uma linha na tabela abaixo dizendo **o que era, de onde saiu e por quê**.
Arquivo nesta pasta sem linha na tabela é arquivo órfão, e órfão ninguém sabe se pode ir embora.

Quem esvazia esta pasta é o Gabriel, e só ele. Nenhuma sessão apaga daqui por conta própria.

| Arquivo | Saiu de | Data | Por quê |
|---|---|---|---|
| `gerar_pdf.cpython-311.pyc.saiu-20260906` | `casa/advocacia/tipografia-e-geradores/instalar/skills/assistente-juridico/assets/__pycache__/` | 06/09/2026 | Bytecode que o Python 3.11 desta nuvem gerou ao testar o gerador, e que entrou num commit por descuido. Não é material da casa, e o Mac roda Python 3.9: o arquivo não serviria lá. `__pycache__/` e `*.pyc` passaram a ficar de fora pelo `.gitignore`. |
