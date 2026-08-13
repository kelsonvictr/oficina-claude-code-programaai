# IA na Prática + Oficina Claude Code — Programa AI

Material didático HTML no padrão `super-html`. Neste branch (`feat/ia-na-pratica`)
o hub é o curso **IA na Prática** (6 módulos). A oficina Claude Code vive em
`oficina/` como aprofundamento do Módulo 6.

O participante escreve português, nunca código. Tom adulto, caloroso, zero infantilização.

**A memória viva mora em `context/`** — leia `context/00-overview.md` primeiro.
- Plano dos **módulos** do curso: `02b-plano-modulos.md`
- Plano da **oficina** Claude Code: `02-plano-capitulos.md` (caps sob `oficina/`)
- Decisões: `01-decisoes.md` (append-only)
- Fatos verificados de instalação/planos: `03-fatos-instalacao.md` (NUNCA inventar
  comandos/flags fora dessa lista)
- Identidade visual: `04-design-system.md`

Regras da casa: ligatures OFF em fontes mono (inclusive `.prompt-card pre`, `.tela-*`,
`.chat-*`), escapar `<>&` em `<pre>`, PT-BR, um conceito por vez.

Restrições específicas:
- **Nenhuma menção a semestre/ano/datas** no conteúdo — material reaproveitável.
- Dados dos exercícios são **fictícios** (CPFs inválidos por design, nomes inventados).
- Comandos de instalação/preços: só os de `context/03-fatos-instalacao.md`, com a data
  de verificação; se for revisar o material, revalidar nas docs oficiais.
- Preços/planos de ChatGPT, Gemini, Manus, NotebookLM: só o que estiver em
  `03-fatos-instalacao.md` (ou linguagem genérica "pode exigir plano pago" + link oficial).

## Depois de editar qualquer HTML, rode

```bash
python3 tools/checar.py
```
