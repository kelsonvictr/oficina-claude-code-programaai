# Oficina Claude Code — para quem nunca programou

Material didático HTML: oficina prática de Claude Code para **não-programadores** de
áreas diversas (adm, direito, marketing, educação...). O participante escreve português,
nunca código. Tom adulto, caloroso, zero infantilização.

**A memória viva mora em `context/`** — leia `context/00-overview.md` primeiro.
Plano dos capítulos em `02-plano-capitulos.md`; decisões em `01-decisoes.md` (append-only);
fatos verificados de instalação/planos em `03-fatos-instalacao.md` (NUNCA inventar
comandos/flags fora dessa lista); identidade visual em `04-design-system.md`.

Regras do workspace (CLAUDE.md raiz) valem integralmente: ligatures OFF em fontes mono
(inclusive nas classes novas `.prompt-card pre`, `.tela-*`, `.chat-*`), escapar `<>&` em
`<pre>`, PT-BR, um conceito por vez. Este diretório é (será) um repo git independente.

Restrições específicas:
- **Nenhuma menção a semestre/ano/datas** no conteúdo — material reaproveitável.
- Dados dos exercícios são **fictícios** (CPFs inválidos por design, nomes inventados).
- Comandos de instalação/preços: só os de `context/03-fatos-instalacao.md`, com a data
  de verificação; se for revisar o material, revalidar nas docs oficiais.

## Depois de editar qualquer HTML, rode

```bash
python3 tools/checar.py
```
