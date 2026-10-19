# IA na Prática — Programa AI

Material didático em HTML: curso de **Inteligência Artificial na Prática** para
não-programadores, com a **oficina Claude Code** embutida como aprofundamento.

O participante escreve português, nunca código.

## Como usar

Abra `index.html` no navegador (funciona direto do arquivo, sem servidor).

### Curso (6 noites — teoria curta + prática + desafio em cada uma)

- **01 · Panorama da IA** — o que uma LLM faz, como pedir bem, ChatGPT / Gemini / Claude / NotebookLM
- **02 · Do chat ao agente** — instalar o Claude Code e a primeira conversa
- **03 · O agente nos seus arquivos** — a pasta bagunçada e a planilha que se analisa sozinha
- **04 · O agente nos seus documentos** — declarações em lote e o contrato de 40 páginas
- **05 · Conteúdo e ensino no automático** — um texto vira dez, a prova com gabarito, Skills e Conectores
- **06 · Sua página e o agente no dia a dia** — página na internet, hábitos, segurança e próximos passos

### Material de apoio (`apoio/`, fora das noites)

Criando com IA · Agentes com Manus AI · NotebookLM a fundo · Universo Claude.

### Oficina Claude Code (aprofundamento)

Roteiro detalhado das Noites 2–6. Hub em [`oficina/index.html`](oficina/index.html) — 11 capítulos: instalar, primeira
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
