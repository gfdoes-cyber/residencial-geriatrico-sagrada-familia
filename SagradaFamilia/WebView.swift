import SwiftUI
import WebKit

/// Envelope SwiftUI para o `WKWebView` que exibe o site do Residencial.
///
/// - `isLoading`: verdadeiro enquanto a página está carregando.
/// - `loadError`: mensagem de erro (pt-BR) quando o carregamento falha; `nil` se não há erro.
/// - `reloadToken`: incremente para forçar um novo carregamento (botão "Tentar novamente").
struct WebView: UIViewRepresentable {
    @Binding var isLoading: Bool
    @Binding var loadError: String?
    var reloadToken: Int

    func makeCoordinator() -> Coordinator {
        Coordinator(parent: self)
    }

    func makeUIView(context: Context) -> WKWebView {
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        configuration.allowsInlineMediaPlayback = true

        let webView = WKWebView(frame: .zero, configuration: configuration)
        // Delegates do WebKit são referências fracas; o coordinator vive junto da view.
        webView.navigationDelegate = context.coordinator
        webView.uiDelegate = context.coordinator
        webView.allowsBackForwardNavigationGestures = true
        webView.scrollView.contentInsetAdjustmentBehavior = .never
        webView.isOpaque = false
        webView.backgroundColor = AppConfig.backgroundColor
        webView.scrollView.backgroundColor = AppConfig.backgroundColor

        // Carrega uma única vez aqui; recarregamentos só acontecem via `reloadToken`.
        context.coordinator.lastReloadToken = reloadToken
        context.coordinator.load(in: webView)
        return webView
    }

    func updateUIView(_ webView: WKWebView, context: Context) {
        // Mantém os bindings atualizados no coordinator.
        context.coordinator.parent = self

        // Idempotente: só recarrega quando o token mudou.
        guard context.coordinator.lastReloadToken != reloadToken else { return }
        context.coordinator.lastReloadToken = reloadToken
        context.coordinator.load(in: webView)
    }

    // MARK: - Coordinator

    final class Coordinator: NSObject, WKNavigationDelegate, WKUIDelegate {
        var parent: WebView
        var lastReloadToken: Int?

        init(parent: WebView) {
            self.parent = parent
        }

        // MARK: Carregamento

        /// Carrega a URL remota (se configurada) ou o `index.html` embutido no bundle.
        func load(in webView: WKWebView) {
            if let remoteURL = AppConfig.remoteURL {
                webView.load(URLRequest(url: remoteURL))
                return
            }

            guard let fileURL = Bundle.main.url(
                forResource: AppConfig.bundledPageName,
                withExtension: AppConfig.bundledPageExtension
            ) else {
                setLoading(false)
                setError(
                    "A página do Residencial não foi encontrada dentro do aplicativo. "
                    + "Verifique se o arquivo \(AppConfig.bundledPageName).\(AppConfig.bundledPageExtension) "
                    + "está incluído no target e reinstale o app."
                )
                return
            }

            webView.loadFileURL(fileURL, allowingReadAccessTo: fileURL.deletingLastPathComponent())
        }

        // MARK: Atualização de estado (sempre na main queue, fora do ciclo de atualização da view)

        private func setLoading(_ value: Bool) {
            DispatchQueue.main.async { [weak self] in
                self?.parent.isLoading = value
            }
        }

        private func setError(_ message: String?) {
            DispatchQueue.main.async { [weak self] in
                self?.parent.loadError = message
            }
        }

        private func handle(_ error: Error) {
            let nsError = error as NSError
            setLoading(false)

            // Navegação cancelada (ex.: link externo aberto no Safari) não é erro para o usuário.
            if nsError.domain == NSURLErrorDomain && nsError.code == NSURLErrorCancelled {
                return
            }
            // "Frame load interrupted" (WebKitErrorDomain 102) acontece quando cancelamos a navegação.
            if nsError.domain == "WebKitErrorDomain" && nsError.code == 102 {
                return
            }

            setError(nsError.localizedDescription)
        }

        // MARK: Links externos

        /// Decide se uma URL deve abrir fora do app (Safari, Telefone, Mail, Mensagens).
        private func shouldOpenExternally(_ url: URL, from webView: WKWebView) -> Bool {
            if url.isFileURL { return false }
            guard let scheme = url.scheme?.lowercased(),
                  AppConfig.externalSchemes.contains(scheme) else {
                return false
            }
            // Navegação dentro do próprio site remoto (mesmo host) continua no app.
            if let remoteHost = AppConfig.remoteURL?.host?.lowercased(),
               url.host?.lowercased() == remoteHost {
                return false
            }
            // Âncoras (#secao) da página atual continuam no app.
            if let current = webView.url, stripFragment(current) == stripFragment(url) {
                return false
            }
            return true
        }

        private func stripFragment(_ url: URL) -> String {
            guard var components = URLComponents(url: url, resolvingAgainstBaseURL: false) else {
                return url.absoluteString
            }
            components.fragment = nil
            return components.string ?? url.absoluteString
        }

        private func openExternally(_ url: URL) {
            UIApplication.shared.open(url)
        }

        /// Verdadeiro para http/https no mesmo host da `AppConfig.remoteURL` (modo remoto).
        private func isSameRemoteSite(_ url: URL) -> Bool {
            guard let scheme = url.scheme?.lowercased(), scheme == "http" || scheme == "https",
                  let remoteHost = AppConfig.remoteURL?.host?.lowercased(),
                  url.host?.lowercased() == remoteHost else {
                return false
            }
            return true
        }

        // MARK: WKNavigationDelegate

        func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
            setLoading(true)
        }

        func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
            setLoading(false)
        }

        func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
            handle(error)
        }

        func webView(
            _ webView: WKWebView,
            didFailProvisionalNavigation navigation: WKNavigation!,
            withError error: Error
        ) {
            handle(error)
        }

        func webView(
            _ webView: WKWebView,
            decidePolicyFor navigationAction: WKNavigationAction,
            decisionHandler: @escaping (WKNavigationActionPolicy) -> Void
        ) {
            guard let url = navigationAction.request.url else {
                decisionHandler(.allow)
                return
            }

            let isUserLink = navigationAction.navigationType == .linkActivated
                || navigationAction.targetFrame == nil

            if isUserLink && shouldOpenExternally(url, from: webView) {
                openExternally(url)
                decisionHandler(.cancel)
                return
            }

            decisionHandler(.allow)
        }

        func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
            // O processo de conteúdo foi encerrado pelo sistema (memória); recarrega a página.
            webView.reload()
        }

        // MARK: WKUIDelegate

        /// Links com `target="_blank"` não abrem uma nova janela no app: vão para fora
        /// (se forem externos) ou, se apontarem para o próprio site, são carregados no
        /// WKWebView atual. Qualquer outra URL (about:blank, javascript:, data:) é ignorada.
        func webView(
            _ webView: WKWebView,
            createWebViewWith configuration: WKWebViewConfiguration,
            for navigationAction: WKNavigationAction,
            windowFeatures: WKWindowFeatures
        ) -> WKWebView? {
            guard let url = navigationAction.request.url else { return nil }

            if shouldOpenExternally(url, from: webView) {
                openExternally(url)
            } else if url.isFileURL {
                webView.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
            } else if isSameRemoteSite(url) {
                webView.load(URLRequest(url: url))
            }
            // Demais esquemas: não navega, para não substituir o site por uma página em branco.
            return nil
        }
    }
}
