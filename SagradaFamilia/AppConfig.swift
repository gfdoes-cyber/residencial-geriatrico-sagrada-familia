import UIKit

/// Configurações centrais do aplicativo.
///
/// Modo padrão (offline): o app carrega o `index.html` embutido no bundle,
/// que é o mesmo arquivo da raiz do repositório (adicionado como recurso do target).
///
/// Modo remoto: preencha `remoteURL` com a URL publicada do site e o app passará
/// a carregar a página da internet em vez do arquivo local.
enum AppConfig {
    /// Nome (sem extensão) da página embutida no bundle.
    static let bundledPageName = "index"

    /// Extensão da página embutida no bundle.
    static let bundledPageExtension = "html"

    /// URL remota do site. Deixe `nil` para usar a página embutida (offline).
    /// Para usar o site publicado, troque por algo como:
    /// `URL(string: "https://gfdoes-cyber.github.io/residencial-geriatrico-sagrada-familia/")`
    static let remoteURL: URL? = nil

    /// Cor de fundo do site: `--creme: #FBF6EE`, a mesma do `body` e do `theme-color`
    /// no index.html. É pintada atrás do WKWebView para não "piscar" enquanto a página carrega.
    static let backgroundColor = UIColor(
        red: 0xFB / 255.0,
        green: 0xF6 / 255.0,
        blue: 0xEE / 255.0,
        alpha: 1.0
    )

    /// Cor de texto principal do site (`--texto: #3B2A22`), usada na tela de erro nativa.
    static let textColor = UIColor(
        red: 0x3B / 255.0,
        green: 0x2A / 255.0,
        blue: 0x22 / 255.0,
        alpha: 1.0
    )

    /// Cor de texto secundária do site (`--texto-suave: #6B5A50`), usada na tela de erro nativa.
    static let secondaryTextColor = UIColor(
        red: 0x6B / 255.0,
        green: 0x5A / 255.0,
        blue: 0x50 / 255.0,
        alpha: 1.0
    )

    /// Esquemas de URL que, quando acionados por um link, são abertos fora do app
    /// (Safari, Telefone, Mail, Mensagens). Links para o próprio site continuam no app.
    static let externalSchemes = ["http", "https", "tel", "mailto", "sms"]
}
