# Plano dos módulos — IA na Prática (curso em 6 noites)

Arco do **curso** no hub raiz, alinhado ao cronograma oficial do curso presencial
(6 encontros de ~2h). A oficina Claude Code (roteiro detalhado das práticas) está
documentada em `02-plano-capitulos.md` e vive em `oficina/`.

**Requisito duro:** toda noite tem teoria E prática juntas, já na primeira. Anatomia fixa
de cada `modulos/NN-slug/index.html` (molde: `03-agente-nos-arquivos`):
`#objetivo` (checklist + roteiro em `.timeline` de blocos ~2h) → `#teoria` (curta) →
`#demo` (`.chat-claude` com `data-seq`) → `#pratica-a`, `#pratica-b` [, `#pratica-c`]
(`.precisa` + passos com `.prompt-card`/`.tela` + tip "roteiro completo" para a oficina) →
`#desafio` (`.exercise.solo` + `.try-first` + `.toggler` com solução) → `#quiz-final` →
`#resumo` (`.checklist` + `.cap-nav`). Prompts e números do kit são copiados dos capítulos
da oficina — nunca inventados.

| Noite | Pasta | Tópicos | Prática |
|---|---|---|---|
| 1 | `modulos/01-panorama-da-ia` | O que uma LLM faz, mitos, contexto, alucinação, como pedir bem, qual ferramenta usar (ChatGPT, Gemini, Claude, NotebookLM, imagem) | A: ruim × bom · B: o mesmo pedido em 3 ferramentas · C: NotebookLM com o contrato do kit (citação + pergunta-armadilha) |
| 2 | `modulos/02-do-chat-ao-agente` | Chat × agente, ciclo pedir-aprovar-conferir, instalação do Claude Code e primeira conversa | A: conta, porta, vacina, login, teste do "oi" (aponta para oficina/02) · B: pasta, kit, abrir na pasta certa, ler × mexer (oficina/03) · desafio: inventário do kit (43 arquivos) |
| 3 | `modulos/03-agente-nos-arquivos` | Diagnóstico, plano, execução, conferência | A: pasta bagunçada (oficina/04) · B: planilha de gastos (oficina/05) |
| 4 | `modulos/04-agente-nos-documentos` | Descrever o resultado, piloto antes do lote, alucinação e referência da cláusula | A: declarações em lote (oficina/06) · B: contrato de 40 páginas (oficina/07) |
| 5 | `modulos/05-conteudo-e-ensino` | Caderninho de regras, iteração, curadoria, Skill × Conector | A: texto vira dez (oficina/08) · B: prova com gabarito (oficina/09) · C: Skill a partir do tom-de-voz.txt + Conector do Drive (demo do instrutor, opcional ao aluno) |
| 6 | `modulos/06-pagina-e-dia-a-dia` | Pedir-ver-ajustar, limites honestos, dados sensíveis, hábitos, caderninho (CLAUDE.md), máquina do tempo | A: sua página (oficina/10) · B: caderninho + máquina do tempo (oficina/11) · desafio: levar uma tarefa real para o trabalho |

## Material de apoio (fora das 6 noites)

Os antigos módulos que não estão no cronograma viraram consulta em `apoio/`
(mesma profundidade de pasta, então `../../shared` continua valendo):
`01-criando-com-ia` (texto/imagem/vídeo), `02-agentes-manus`, `03-notebooklm`
(aprofundamento da Prática C da Noite 1), `04-universo-claude` (Skills, Conectores,
Plugins, Cowork — base da Prática C da Noite 5). Rotulados "Apoio NN", não "Módulo".

## Oficina (fora da numeração 01–06)
Hub em `oficina/index.html` + caps `oficina/01`…`11` — ver `02-plano-capitulos.md`.
Cada noite 2–6 linka o capítulo correspondente como "roteiro completo".
