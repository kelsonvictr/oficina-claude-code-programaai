# Design system — identidade "terminal amigável"

## Conceito
O medo nº 1 do público é a tela preta. Então a identidade ABRAÇA a tela preta e a torna
acolhedora: o material inteiro joga com a estética de **janela de terminal que conversa
em português**. Prompt `>` piscando, balões de conversa dentro de molduras de janela,
o coral Claude como cor humana sobre o dark técnico.

## Paleta (deltas sobre a base herdada de `engenharia-software`)
Base dark idêntica ao irmão (`--bg:#0a0f1a`, surfaces, texto, dim). Por cima:

- `--claude: #d97757` — cor-tema primária (coral/terracota Claude)
- `--claude-soft: #e8a087` — variação clara para gradientes
- `--term: #4ade80` — verde-terminal (respostas do computador, sucesso, cursor)
- Acentos herdados continuam valendo: `--accent5:#f7b731` (avisos/destaques),
  `--accent6:#a78bfa` (conceitos), `--accent2:#ff6b6b` (armadilhas), `--accent7:#06d6a0`.
- Áreas das práticas ganham cor no hub via faixa `.c04`…`.c11` (uma cor por prática).

## Tipografia
Idêntica aos irmãos: **Nunito** (corpo), **Caveat** (manuscrito — aqui vira "anotação
de quem está aprendendo"), **JetBrains Mono** (terminais, prompts copiáveis).
⚠️ Ligatures OFF em `pre, code` E em toda classe mono nova (`.prompt-card pre`,
`.tela-*`, `.chat-msg`, etc.) — regra global + repetição local, como nos irmãos.
Escapar `<>&` em `<pre>` sempre. Rodar `python3 tools/checar.py` após editar.

## Herança do `shared/` (copiado de engenharia-software e adaptado)
Mantidos: tokens/reset/progress/sidebar/hero (styles.css), cards, `.concept`, `.analogy`,
`.tip/.warning`, `.code-block`, `.exercise`, `.quiz`+confete, `.flow-container`,
`.terminal[data-typewriter]`, `.mito-real` (carimbo MITO — perfeito para os medos),
`.timeline`, `.checklist`, `.cap-nav`, `.hub-card`+`.em-breve`, `data-seq`, `onView`,
motion-fx (Motion CDN + fallback). Podados: `.blueprint` (moldura de planta), `.sim` de
processo fica como casca genérica, `.dinamica` (vira `.roteiro` se precisar p/ instrutor),
`.ia-box` (aqui TUDO é IA — sem sentido).

## Componentes NOVOS deste material
- **`.chat-claude`** — a peça central: janela de terminal estilizada com a CONVERSA
  (balão "você" em coral, resposta em verde-terminal, caixa de permissão amarela com
  botões Sim/Não). Usada nos fluxos animados via `data-seq`.
- **`.prompt-card`** — prompt pronto para copiar: cabeçalho "✨ PROMPT PRONTO", corpo mono
  (ligatures off!), botão 📋 copiar (`copiarPrompt(btn)` em scripts.js), rodapé "por que
  funciona" opcional em `.pc-por-que`.
- **`.precisa`** — checklist "🧾 O que você vai precisar" no topo de cada prática
  (itens com ✅/⬜, download do kit em destaque).
- **`.tela`** — "🖥️ O que vai aparecer na sua tela": terminal simulado mostrando a
  resposta esperada do Claude, com marcação `.tela-voce`/`.tela-claude`/`.tela-perm`.
- **`.pratica-meta`** — faixa no hero de cada prática: área 🏷️, dificuldade ★, tempo ⏱️.
- **`.armadilha`** — variação da `.warning` específica de prática ("cuidado com…").

## Receita do fluxo animado central (cap 01 e reutilizável)
Ciclo VOCÊ PEDE → CLAUDE LÊ → CLAUDE PROPÕE → VOCÊ APROVA → CLAUDE FAZ → VOCÊ CONFERE,
como `data-seq` de 6 quadros dentro de um `.chat-claude`: mensagens vão aparecendo,
caixa de permissão pisca no quadro 4, arquivos "se organizam" no quadro 5.
1º disparo automático na viewport; botão só para repetir. Fallback sem Motion.

## Estrutura de arquivos
`index.html` (hub do curso IA na Prática) · `modulos/NN-slug/index.html` (6 módulos) ·
`oficina/` (hub + caps 01–11 da oficina Claude Code) · `shared/` · `assets/`
(+ `assets/kit/` com os arquivos de exercício e `kit-oficina.zip`) · `context/` · `tools/`.
Branch `feat/ia-na-pratica`; merge em `master` só sob pedido explícito.

## Tom
PT-BR caloroso, "você", frases curtas. O leitor é ADULTO e INTELIGENTE, só não é técnico —
zero infantilização. Analogias do mundo do trabalho (estagiário genial, mala direta,
caderninho de regras). Piada seca nos subtítulos como nos irmãos. Emojis com parcimônia.
Código NUNCA é protagonista: quando aparece, vem com a moldura "isso é bastidor, respira".
