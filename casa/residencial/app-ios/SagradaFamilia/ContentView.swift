import SwiftUI

/// Tela principal: o site do Residencial em tela cheia, com indicador de
/// carregamento e uma tela de erro com "Tentar novamente".
struct ContentView: View {
    @State private var isLoading = true
    @State private var loadError: String?
    @State private var reloadToken = 0

    var body: some View {
        ZStack {
            Color(uiColor: AppConfig.backgroundColor)
                .ignoresSafeArea()

            WebView(isLoading: $isLoading, loadError: $loadError, reloadToken: reloadToken)
                .ignoresSafeArea()

            if isLoading && loadError == nil {
                loadingOverlay
            }

            if let message = loadError {
                errorView(message: message)
            }
        }
        // O site é sempre claro (color-scheme: light); força o mesmo no app para que a
        // barra de status e os textos nativos fiquem legíveis com o iPhone em modo escuro.
        .preferredColorScheme(.light)
    }

    // MARK: - Subviews

    private var loadingOverlay: some View {
        ZStack {
            Color(uiColor: AppConfig.backgroundColor)
                .ignoresSafeArea()
            ProgressView("Carregando…")
                .progressViewStyle(.circular)
                .padding(24)
                .background(
                    RoundedRectangle(cornerRadius: 16, style: .continuous)
                        .fill(Color(uiColor: .secondarySystemBackground))
                )
        }
        .transition(.opacity)
        .accessibilityLabel("Carregando a página do Residencial")
    }

    private func errorView(message: String) -> some View {
        ZStack {
            Color(uiColor: AppConfig.backgroundColor)
                .ignoresSafeArea()

            VStack(spacing: 16) {
                Image(systemName: "wifi.exclamationmark")
                    .font(.system(size: 48, weight: .regular))
                    .foregroundColor(.accentColor)
                    .accessibilityHidden(true)

                Text("Não foi possível carregar a página")
                    .font(.title2.weight(.semibold))
                    .foregroundColor(Color(uiColor: AppConfig.textColor))
                    .multilineTextAlignment(.center)

                Text(message)
                    .font(.body)
                    .foregroundColor(Color(uiColor: AppConfig.secondaryTextColor))
                    .multilineTextAlignment(.center)

                Button {
                    retry()
                } label: {
                    Text("Tentar novamente")
                        .font(.body.weight(.semibold))
                        .padding(.horizontal, 24)
                        .padding(.vertical, 12)
                }
                .buttonStyle(.borderedProminent)
                .padding(.top, 8)
            }
            .padding(32)
        }
    }

    // MARK: - Ações

    private func retry() {
        loadError = nil
        isLoading = true
        reloadToken += 1
    }
}

// PreviewProvider clássico (compatível com iOS 16 / Xcode 14, sem depender da macro #Preview).
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
