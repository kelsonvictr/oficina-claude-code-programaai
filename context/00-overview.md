# IA na Prática — Programa AI (branch feat/ia-na-pratica)

Material didático em HTML: curso prático de **Inteligência Artificial na Prática**
para não-programadores, com a **oficina Claude Code** embutida como aprofundamento
do Módulo 6.

## O que este material É

- Um **site estático** no padrão da família `super-html` (hub + capítulos autocontidos,
  tema dark, animações Motion com fallback CSS, quizzes, fluxos animados).
- Um **curso de 6 módulos** (`modulos/`): fundação de IA/LLM, criação (texto/imagem/vídeo),
  agentes (Manus), NotebookLM, Universo Claude, teaser Claude Code.
- Uma **oficina mão-na-massa** (`oficina/`): os 11 capítulos originais de Claude Code
  (base + 7 práticas + fechamento), acessível pelo Módulo 6 e pelo cartão do hub.
- **Zero pré-requisito de programação.** O participante escreve PORTUGUÊS.

## O que este material NÃO é

- Não é curso de programação, nem de Git, nem de Python (coadjuvantes na oficina).
- Não é documentação completa de cada produto (ChatGPT, Gemini, Manus…): só o que
  serve ao leigo nas primeiras semanas.
- Não é material de venda — custos e limites são ditos com clareza quando conhecidos.

## Público

Adultos iniciantes, áreas diversas, notebook próprio (Windows na maioria, alguns macOS).
Sabem usar navegador, WhatsApp, Word.

## Formato

- **Presencial / imersão**: módulos 1–5 do curso + teaser 6; oficina Claude Code em
  bloco separado ou segundo dia.
- **Autoestudo**: hub autossuficiente; oficina independente após o Módulo 6.

## Estrutura de pastas (neste branch)

| Pasta / arquivo | Papel |
|---|---|
| `index.html` | Hub do curso (6 módulos + link da oficina) |
| `modulos/01`…`06` | Capítulos do curso IA na Prática |
| `oficina/` | Oficina Claude Code (hub próprio + caps 01–11) |
| `shared/` | CSS/JS compartilhados |
| `assets/kit/` | Kit de treino da oficina |
| `context/` | Memória viva |
| `tools/` | `checar.py`, `gerar_kit.py` |

## Arquivos desta pasta (`context/`)

| Arquivo | Conteúdo |
|---|---|
| `01-decisoes.md` | Log cronológico de decisões (append-only) |
| `02-plano-capitulos.md` | Arco da oficina Claude Code (sob `oficina/`) |
| `02b-plano-modulos.md` | Arco dos 6 módulos do curso |
| `03-fatos-instalacao.md` | Fatos verificados (atualizar quando mudar) |
| `04-design-system.md` | Identidade visual "terminal amigável" |
