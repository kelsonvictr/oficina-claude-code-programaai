# Oficina Claude Code — para quem nunca programou

Material didático em HTML para uma oficina prática de **Claude Code voltada a
não-programadores** de qualquer área: administração, direito, marketing, educação,
saúde, secretaria. O participante escreve português, nunca código.

## Como usar

Abra `index.html` no navegador (funciona direto do arquivo, sem servidor) e siga
pelos cartões. O arco:

- **Ato 1 · Entender e preparar** — caps 01–03: conceito, instalação (Windows/Mac,
  app desktop ou terminal) e a primeira conversa.
- **Ato 2 · Práticas** — caps 04–10, independentes entre si, cada uma com prompts
  prontos, arquivos de treino e "o que vai aparecer na sua tela": pasta bagunçada,
  planilha de gastos, declarações em lote, contrato em PDF, marketing, prova de
  professor e o mini-site (momento uau).
- **Ato 3 · Seguir sozinho** — cap 11: hábitos, limites honestos da IA, CLAUDE.md
  e o "ponto de restauração" (git desmistificado).

## Kit da Oficina

Arquivos de treino 100% fictícios em `assets/kit/` (zip que o participante baixa
no Cap 03). Para regenerar do zero:

```bash
python3 tools/gerar_kit.py
```

## Manutenção

- A memória viva do projeto está em `context/` — leia `context/00-overview.md` primeiro.
- Depois de editar qualquer HTML: `python3 tools/checar.py` (ligaduras, escapes,
  âncoras, classes órfãs, datas proibidas).
- Comandos de instalação e preços citados no material: fatos verificados em
  `context/03-fatos-instalacao.md` — revalidar nas docs oficiais antes de revisões.
