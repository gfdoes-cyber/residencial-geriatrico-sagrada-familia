# Residencial Geriátrico Sagrada Família

Site institucional de um residencial geriátrico (ILPI) e aplicativo iOS que exibe esse mesmo site dentro do app, funcionando offline.

O repositório contém duas coisas que compartilham um único arquivo de conteúdo:

1. **Site** — `index.html`, um arquivo único (HTML + CSS + JS + SVG inline), sem nenhuma dependência externa. Pode ser aberto direto no navegador ou publicado no GitHub Pages.
2. **App iOS "Sagrada Família"** — projeto Xcode em SwiftUI que embute o `index.html` da raiz em um `WKWebView`. Links de WhatsApp, telefone, e-mail e Google Maps abrem nos apps do sistema.

> Atenção: todos os dados de contato (telefone, WhatsApp, e-mail, endereço, CNPJ, responsável técnico) são **placeholders fictícios** e precisam ser substituídos antes de publicar. Veja a lista ao final deste arquivo.

## Estrutura de pastas

```
.
├── index.html                          # o site (arquivo único; também é o recurso embutido no app)
├── README.md
├── .gitignore                          # padrão Xcode/Swift
├── SagradaFamilia.xcodeproj/           # projeto Xcode (abra este)
│   ├── project.pbxproj
│   └── project.xcworkspace/contents.xcworkspacedata
└── SagradaFamilia/                     # código do app iOS
    ├── SagradaFamiliaApp.swift         # ponto de entrada (@main)
    ├── ContentView.swift               # tela principal: WebView + carregando + tela de erro
    ├── WebView.swift                   # WKWebView (UIViewRepresentable) e tratamento de links externos
    ├── AppConfig.swift                 # configurações: página embutida, URL remota, cores
    ├── PrivacyInfo.xcprivacy           # manifesto de privacidade (o app não coleta dados)
    └── Assets.xcassets/                # ícone do app (AppIcon) e cor de destaque (AccentColor)
```

O `index.html` **não** é copiado para dentro de `SagradaFamilia/`: o projeto referencia o arquivo da raiz do repositório como recurso do target. Editar o site atualiza o app no próximo build.

## Requisitos

- macOS com **Xcode 15 ou superior** (o projeto abre também no Xcode 16/17).
- iPhone/iPad com **iOS 16 ou superior** (ou o Simulador do Xcode).
- Uma conta Apple (a conta gratuita basta para rodar no simulador e em um aparelho próprio).

## Como abrir e rodar no Xcode

1. Clone ou baixe o repositório.
2. Dê **duplo clique em `SagradaFamilia.xcodeproj`** (ou, no Xcode, File → Open… e escolha esse arquivo).
3. Na barra lateral, clique no projeto **SagradaFamilia** (ícone azul, no topo) → target **SagradaFamilia** → aba **Signing & Capabilities**.
4. Em **Team**, selecione a sua conta Apple. Se ela não aparecer, adicione-a em Xcode → Settings… → Accounts.
5. Se o Xcode avisar que o *bundle identifier* já está em uso, troque `br.com.residencialsagradafamilia.app` por um identificador seu (por exemplo `br.com.seudominio.sagradafamilia`).
6. Na barra superior, escolha um simulador (por exemplo **iPhone 15**) e pressione **Run** (▶ ou Cmd+R).

O app abre em tela cheia mostrando o site. Toques em "Agendar visita", "Ligar agora", e-mail e "Ver no Google Maps" abrem os apps correspondentes (no simulador, telefone e WhatsApp não existem, então esses links não fazem nada; teste em um iPhone real).

### Rodar em um iPhone físico

1. Conecte o iPhone por cabo (ou pareie por Wi-Fi) e selecione-o como destino no Xcode.
2. No iPhone, ative o **Modo Desenvolvedor**: Ajustes → Privacidade e Segurança → Modo do Desenvolvedor → ativar e reiniciar. (O item só aparece depois que o Xcode tenta instalar um app pela primeira vez.)
3. Pressione **Run**. Na primeira vez, o iPhone bloqueia o app por ser de um "desenvolvedor não confiável".
4. No iPhone, vá em Ajustes → Geral → **Gerenciamento de VPN e Dispositivo** (ou "Gerenciamento de Dispositivo"), toque no seu perfil de desenvolvedor e em **Confiar**.
5. Abra o app novamente.

Com conta Apple gratuita, o app instalado por cabo expira em 7 dias; basta rodar de novo pelo Xcode. Para distribuir para outras pessoas (TestFlight ou App Store) é necessário o Apple Developer Program.

## Como editar os dados de contato (bloco "EDITE AQUI")

Abra `index.html` e procure o comentário **`EDITE AQUI`**, perto do fim do arquivo, dentro da tag `<script>`. Há um objeto `const SITE = { ... }` com todos os dados:

```js
const SITE = {
  nome: 'Residencial Geriátrico Sagrada Família',
  telefone: '(00) 0000-0000',          // aparece no site; o link tel: é gerado a partir dele
  whatsapp: '(00) 00000-0000',         // aparece no site; o link wa.me é gerado a partir dele
  email: 'contato@exemplo.com.br',
  endereco: 'Rua Exemplo, 123 – Bairro',
  cidadeUF: 'Cidade/UF',
  cep: '00000-000',
  horarioVisitas: 'Consulte-nos ao agendar a visita',
  cnpj: '00.000.000/0000-00',
  responsavelTecnico: 'Nome do(a) Responsável Técnico(a) – registro profissional 000000',
  // ...
};
```

Ao carregar a página, o JavaScript preenche todos os elementos marcados com `data-site="..."` e gera automaticamente os links `tel:`, `https://wa.me/55...`, `mailto:` e do Google Maps (o prefixo +55 é adicionado e só os dígitos são usados).

Observações:

- O HTML contém os **mesmos placeholders** como texto fixo (fallback para quem navega sem JavaScript). Para não sobrar nenhum "(00) 0000-0000" nesse cenário, faça uma busca no arquivo pelos valores antigos e substitua também no HTML. Os pontos são: cabeçalho e hero (links `wa.me` e `tel:`), seção Contato, rodapé e botão flutuante.
- `<title>` e `<meta name="description">` no `<head>` também são textos fixos; ajuste-os se mudar o nome.
- Textos de serviços, estrutura, equipe e dúvidas frequentes descrevem uma oferta típica de ILPI. Revise cada frase e mantenha só o que o residencial realmente oferece.

## Modo offline x modo remoto no app

Por padrão o app carrega o `index.html` embutido (`AppConfig.remoteURL = nil`), então funciona sem internet e a cada build leva a versão atual do arquivo.

Para o app passar a exibir o site publicado (e refletir alterações sem atualizar o app), edite `SagradaFamilia/AppConfig.swift`:

```swift
static let remoteURL: URL? = URL(string: "https://gfdoes-cyber.github.io/residencial-geriatrico-sagrada-familia/")
```

Nesse modo, se o aparelho estiver sem conexão o app mostra uma tela de erro em português com o botão "Tentar novamente". Links para o mesmo domínio do site continuam dentro do app; os demais (WhatsApp, telefone, e-mail, Maps) abrem fora.

## Publicar o site no GitHub Pages

1. No GitHub, abra o repositório → **Settings** → **Pages**.
2. Em **Build and deployment**, escolha **Source: Deploy from a branch**.
3. Em **Branch**, selecione **`main`** e a pasta **`/ (root)`**; clique em **Save**.
4. Aguarde alguns minutos. A URL prevista é:

   `https://gfdoes-cyber.github.io/residencial-geriatrico-sagrada-familia/`

   (o formato é `https://<usuário>.github.io/<repositório>/`; confirme o nome de usuário exato na própria página de Settings → Pages, que exibe a URL final).

Como o site é um único `index.html` sem dependências, não há etapa de build. Cada `git push` na branch `main` republica automaticamente.

## O que você precisa preencher ou decidir

| Item | Onde |
|---|---|
| Telefone fixo | `index.html` → `SITE.telefone` (+ fallbacks `tel:` no HTML) |
| WhatsApp | `index.html` → `SITE.whatsapp` (+ fallbacks `wa.me` no HTML) |
| E-mail | `index.html` → `SITE.email` (+ fallbacks `mailto:` no HTML) |
| Endereço, cidade/UF e CEP | `index.html` → `SITE.endereco`, `SITE.cidadeUF`, `SITE.cep` |
| Horário de visitas | `index.html` → `SITE.horarioVisitas` |
| CNPJ | `index.html` → `SITE.cnpj` |
| Responsável técnico(a) e registro profissional | `index.html` → `SITE.responsavelTecnico` |
| Nome oficial (se diferente) | `SITE.nome`, `SITE.marcaLinha1/2`, `<title>` e `<meta name="description">` |
| Frase normativa do rodapé (RDC nº 502/2021 da ANVISA e Lei nº 10.741/2003) | `index.html`, seção `<footer>` — revisar com o responsável técnico se a redação de compromisso é adequada à situação real da instituição (licença sanitária, alvará etc.) |
| Bundle identifier do app | Xcode → target → Signing & Capabilities (ou `PRODUCT_BUNDLE_IDENTIFIER` em `project.pbxproj`) |
| Team (conta Apple) | Xcode → Signing & Capabilities → Team |
| URL remota do site (opcional) | `SagradaFamilia/AppConfig.swift` → `remoteURL` |
| Ícone do app | `SagradaFamilia/Assets.xcassets/AppIcon.appiconset/AppIcon.png` (1024×1024, sem transparência) |

## Privacidade

O site não usa formulários, cookies próprios, fontes externas nem ferramentas de rastreamento. O app não coleta dados (`PrivacyInfo.xcprivacy` declara zero tipos de dados e zero rastreamento). O único tráfego acontece quando a pessoa escolhe abrir WhatsApp, Google Maps, telefone ou e-mail — serviços de terceiros com políticas próprias.
