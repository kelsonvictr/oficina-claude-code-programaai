# Fatos verificados — instalação, planos e login (verificado em 2026-08-12)

Fonte: docs oficiais (code.claude.com/docs). **Revalidar antes de grandes revisões** —
instalação e preços mudam. NUNCA inventar comandos/flags além dos listados aqui.

## Instalação (instalador nativo = recomendado; auto-atualiza; NÃO precisa de Node)

| Plataforma | Comando |
|---|---|
| macOS / Linux / WSL | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` |
| macOS Homebrew (alt.) | `brew install --cask claude-code` |
| Windows WinGet (alt.) | `winget install Anthropic.ClaudeCode` |

- Windows roda **nativo** (PowerShell/CMD), sem WSL. Win 10 build 1809+ / macOS 13+.
- **Git NÃO é obrigatório.** No Windows, Git for Windows é opcional (habilita Bash;
  sem ele o Claude usa PowerShell — funciona igual para o nosso público).
- **Node NÃO é necessário** no instalador nativo (só no método npm, que não ensinamos).

## App desktop (porta de entrada recomendada para leigos)

- Download: mac `https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect` ·
  win `https://claude.ai/api/desktop/win32/x64/setup/latest/redirect`
- Abas: Chat / Cowork / **Code** (a que usamos). Mesmo motor do CLI, com painel visual
  de mudanças e terminal embutido. Configurações compartilhadas com o CLI.

## Conta e custo (dizer com transparência no material)

- **Conta gratuita NÃO serve.** Precisa: Claude Pro (~US$20/mês), Max, Team/Enterprise,
  ou créditos de API no Console. Preço atual: https://claude.com/pricing
- Alternativa sem instalar nada: claude.ai/code (web, research preview, exige GitHub —
  NÃO recomendado para este público; mencionar só de passagem ou omitir).

## Login (primeiro uso)

`claude` no terminal (ou abrir o app) → abre o navegador → entra com a conta claude.ai →
volta ao terminal com "Login successful". Se o navegador não voltar sozinho: aparece um
código de 6 caracteres para colar. Depois disso fica logado; `/login` para trocar de conta.

## Padrões de segurança relevantes para o material

- Modo padrão pede permissão antes de editar arquivo/rodar comando (Manual). É recurso,
  não defeito — o material celebra isso.
- `/memory` mostra o que ele anotou; CLAUDE.md = "caderninho de regras" da pasta.
- Primeira resposta da sessão pode demorar (ele está lendo a pasta) — avisar o aluno.

## Decisão pedagógica derivada (ver 01-decisoes.md)

- **Git e Python NÃO entram como pré-requisito.** O único pré-requisito real é: conta paga
  + instalador nativo (ou app desktop). Quando uma prática precisar de Python/ferramenta,
  o roteiro é "peça ao Claude — ele instala ou contorna", e isso vira momento didático.
- Git aparece só no cap 11 como "máquina do tempo" opcional, instalada pelo próprio Claude.
