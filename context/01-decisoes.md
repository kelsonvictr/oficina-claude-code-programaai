# Log de decisões (append-only — marcar superseded, nunca apagar)

## 2026-08-12 — Nascimento do projeto
- **Público**: adultos não-programadores de áreas diversas, notebook próprio (maioria
  Windows). Pedido do prof. Kelson: oficina prática, situações reais de várias áreas,
  prompts prontos, "o que vai precisar", fluxos animados, qualidade dos irmãos.
- **Formato**: hub + 3 caps de base + 7 práticas independentes + fechamento
  (ver 02-plano-capitulos.md). Funciona presencial (~3–4h) e autoestudo.
- **Git e Python NÃO são pré-requisito** (pergunta explícita do Kelson). Motivo: o
  instalador nativo não depende de nada; o próprio Claude instala/contorna ferramentas
  quando a prática exigir — e isso vira momento didático ("peça a ele"). Git aparece só
  no cap 11 como "máquina do tempo" opcional. Fatos em 03-fatos-instalacao.md.
- **Porta de entrada dupla no cap 02**: app desktop (recomendada p/ leigos) e terminal
  (para quem quiser a experiência raiz). Seletor interativo mac/win.
- **Transparência de custo**: dizer já no cap 01 que exige plano pago (~US$20/mês Pro),
  com link para claude.com/pricing. Sem surpresa no meio da oficina.
- **Fundação**: `shared/` copiado de `engenharia-software` e adaptado (paleta coral
  Claude `#d97757` + verde-terminal `#4ade80`, identidade "terminal amigável").
  Podados: `.blueprint`, `.ia-box`, `.dinamica`. Novos: `.chat-claude`, `.prompt-card`,
  `.precisa`, `.tela`, `.pratica-meta`, `.armadilha` (ver 04-design-system.md).
- **Kit da Oficina**: arquivos de exercício fictícios gerados por `tools/gerar_kit.py`,
  zip único + pastas por prática em `assets/kit/`.
- **claude.ai/code (web)**: omitido do material — exige GitHub, atrito demais p/ o público.
