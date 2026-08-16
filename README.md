# IA na Prática — Programa AI

Material didático em HTML: curso de **Inteligência Artificial na Prática** para
não-programadores, com a **oficina Claude Code** embutida como aprofundamento.

O participante escreve português, nunca código.

## Como usar

Abra `index.html` no navegador (funciona direto do arquivo, sem servidor).

### Curso (6 módulos)

- **01 · IA na Prática** — LLM, mitos, prompts, ChatGPT / Gemini / Claude
- **02 · Criando com IA** — textos, imagens, roteiros de vídeo
- **03 · Agentes (Manus AI)** — objetivos e automação em várias etapas
- **04 · NotebookLM** — seus documentos como base de conhecimento
- **05 · Universo Claude** — Artifacts, Projects, Skills, Cowork
- **06 · Claude Code** — teaser + porta para a oficina prática

### Oficina Claude Code (aprofundamento)

Hub em [`oficina/index.html`](oficina/index.html) — 11 capítulos: instalar, primeira
conversa, 7 práticas (pasta, planilha, PDF, marketing…) e hábitos de segurança.

## Kit da Oficina

Arquivos de treino fictícios em `assets/kit/` (baixados no Cap 03 da oficina).
Para regenerar:

```bash
python3 tools/gerar_kit.py
```

## Manutenção

- Memória viva em `context/` — comece por `context/00-overview.md`.
- Depois de editar HTML: `python3 tools/checar.py`.
- Instalação/preços: só `context/03-fatos-instalacao.md`.
- Branch de trabalho do curso: `feat/ia-na-pratica` (não mergear em `master` sem pedido).
