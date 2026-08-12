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

## 2026-08-12 — Implementação completa dos 11 capítulos (pedido do Kelson)
- Kelson pediu todos os capítulos de uma vez, sem verificação em navegador ("testo aqui").
  Portão de qualidade: `tools/checar.py` em todos os HTML.
- **Kit da Oficina gerado** por `tools/gerar_kit.py` (stdlib puro, seed fixa, mini-gerador
  de PDF embutido): bagunca/ 34 arquivos, gastos-2025.csv 306 linhas (grafias inconsistentes,
  6 categorias vazias, 5 duplicatas, outlier de R$ 4.890), participantes.csv 30 pessoas +
  modelo com {{PLACEHOLDERS}}, contrato fictício de 41 págs (valores/prazos plantados p/
  extração) + 3 anexos, release Aurora Termo 500, apostila de juros compostos.
- Caps 02–04 escritos à mão (02: seletor Win/Mac com body[data-so]; 03: montador de pedido
  em 3 peças; 04: template estrutural das práticas). Práticas 05–10 + cap 11 escritos por
  agentes paralelos seguindo o template do 04 + briefs com fatos exatos do kit.
- Padrão pedagógico das práticas consolidado: diagnóstico → plano → execução → conferência,
  com "piloto antes do lote" (06) e "referência da cláusula" (07) como variações do freio.
- CLAUDE.md (nome técnico) só aparece no cap 11; na Prática 08 é "tom-de-voz.txt".
- Git aparece no cap 11 como "ponto de restauração", instalado pelo próprio Claude via prompt.
