# Abrir o app do Residencial no Mac — instruções prontas

Sessão da nuvem não alcança o Mac. Quem tem mãos na máquina é a sessão que **roda no Mac**.
Este arquivo existe para que abrir essa sessão custe um comando e uma colagem.

## Passo 1 — Um comando no Terminal

```
cd ~/Documents && \
git clone -b claude/espirito-santo-advocacia-setup-f6st5i \
  https://github.com/gfdoes-cyber/residencial-geriatrico-sagrada-familia.git residencial-app 2>/dev/null || \
  (cd ~/Documents/residencial-app && git pull) ; \
cd ~/Documents/residencial-app && claude --permission-mode acceptEdits
```

Se preferir dirigir do celular, troque a última parte por
`claude remote-control --name "App Sagrada Família" --permission-mode acceptEdits`.

**Por que fora do vault.** O iCloud faz *eviction* e o Xcode escreve muito durante o build.
Projeto Xcode dentro do vault do Obsidian dá arquivo sumido no meio da compilação. Fica em
`~/Documents/residencial-app/`.

**Trava 3.** Isto é o Residencial, não o escritório. A sessão da advocacia, aberta em
`Advocacia/`, não deve ler esta pasta. Acrescente ao `deny` do `settings.json` do escritório:
`"Read(//Users/gabriel/Documents/residencial-app/**)"`.

## Passo 2 — Colar isto na sessão

---

Você está no Mac do Gabriel, na pasta `~/Documents/residencial-app`, que é um clone da branch
`claude/espirito-santo-advocacia-setup-f6st5i`. Leia o `CLAUDE.md` da raiz e o `casa/README.md`
antes de agir. Você é o **Ciro**, engenharia do Residencial. Isto é Prédio B: não toque em
`casa/advocacia/` nem em material do escritório.

Sua tarefa é deixar o app iOS **SagradaFamilia** compilando e rodando no simulador, e reportar.

**O que já se sabe, para você não redescobrir:**

- O projeto está em `casa/residencial/app-ios/`. O site que ele embute está em
  `casa/residencial/site/index.html`, e o `project.pbxproj` referencia esse arquivo como
  `../site/index.html`. **As duas pastas precisam continuar lado a lado.**
- `objectVersion = 56`, compatibilidade Xcode 14, grupos clássicos. Não há pastas
  sincronizadas: arquivo novo no disco **não entra na compilação** até ser adicionado ao target.
- **Não há scheme compartilhado.** Só existem `project.pbxproj` e
  `project.xcworkspace/contents.xcworkspacedata`. `xcodebuild -scheme` falha até o Xcode abrir o
  projeto uma vez. Antes disso, use `-target`.
- Alvo: iOS 16, Swift 5, bundle `br.com.residencialsagradafamilia.app`.
- O app carrega o HTML embutido (`AppConfig.remoteURL = nil`). O modo remoto aponta para
  GitHub Pages deste repositório — **não ligue o Pages**, veja `casa/README.md`, item 1.3.

**Faça, nesta ordem:**

1. `xcodebuild -version` e `xcrun simctl list devices available | head`. Anote o que existe.
2. Compile sem scheme:
   `cd casa/residencial/app-ios && xcodebuild -project SagradaFamilia.xcodeproj -target SagradaFamilia -sdk iphonesimulator -configuration Debug build`
3. Se falhar, conserte e recompile até passar. Erro de assinatura no simulador não deve
   aparecer; se aparecer, use `CODE_SIGNING_ALLOWED=NO`.
4. Confirme que o `index.html` entrou no bundle do `.app` gerado. Se não entrou, o recurso
   `../site/index.html` não resolveu: conserte a referência no `project.pbxproj` e diga o que fez.
5. Crie o **scheme compartilhado** em `SagradaFamilia.xcodeproj/xcshareddata/xcschemes/` para que
   um clone novo já compile por `-scheme`. Commite.
6. Suba o simulador, instale e abra o app. Tire uma captura e **olhe**: a página tem que aparecer,
   com o fundo creme `#FBF6EE`, sem tela de erro.
7. Só então, e só se o Xcode for 16 ou superior, proponha migrar o projeto para pastas
   sincronizadas, para que arquivo novo passe a compilar sozinho. **Não migre sem dizer antes o
   que muda e sem o build verde no passo 2.**

**Limites, que não mudam:** você não assina, não publica na App Store, não cria conta Apple, não
aceita termo, não digita senha. Monta até a última tela e para. Commits em português, na branch
da sessão. Não abra pull request sem pedido.

**Ao terminar, relate em cinco linhas:** versão do Xcode; se compilou; se o HTML entrou no bundle;
se o app abriu no simulador; e o que ficou pendente do Gabriel.

---

## O que já foi conferido daqui, e não precisa refazer

| Item | Estado |
|---|---|
| Referência do `index.html` no `project.pbxproj` | apontada para `../site/index.html` em 06/09/2026 |
| Manifesto de privacidade | declara zero rastreamento e zero coleta, coerente com o site |
| Site embutido | sem formulário, sem rastreador, sem recurso externo além de WhatsApp e Google Maps |
| Dados de contato do site | **fictícios** (`(00) 0000-0000`, `contato@exemplo.com.br`, "Rua Exemplo, 123") — a lista do que preencher está no `README.md` ao lado |
| Se o projeto compila | **VAZIO** — exige macOS e Xcode; nunca foi compilado |
