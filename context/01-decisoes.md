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

## 2026-08-12 — CORREÇÃO: Git é obrigatório no app do Windows (SUPERSEDE a decisão acima)
- Kelson reportou da prática: o app desktop no Windows pede o Git logo de cara. Confirmado
  nas docs oficiais: *"On Windows, Git must be installed for local sessions to work"*.
- Causa do erro: a pesquisa inicial verificou o CLI (onde git É opcional, com fallback para
  PowerShell) e generalizamos para o app — que é justamente a porta recomendada aos leigos.
  O material chegou a afirmar "sem Node, sem git, sem Python" em dois lugares.
- Correções aplicadas: cap 02 ganhou o Git como **passo 1 da Porta A no Windows** (botão
  secundário `.c2-download.ajudante`, enquadrado como "ajudante de bastidores" que você nunca
  usa direto), nota tranquilizadora no Mac, tip da Porta B reescrita (opcional lá, obrigatório
  na Porta A), item novo no checklist, toggler novo em "Deu errado?" ("falta o Git" + dica de
  fechar/reabrir o app, com a Porta B como saída), teaser do cap 01 ajustado ("um programa
  ajudante"), e cap 11 agora diz que a máquina do tempo JÁ está instalada para a maioria.
- Lição para o futuro: verificar fatos **por caminho de instalação**, nunca em geral.

## 2026-08-12 — Python vira passo RECOMENDADO no cap 02 ("a vacina")
- Decisão do Kelson, por risco operacional de sala: a IA tende a resolver tarefas de dados
  escrevendo Python; se faltar na máquina do aluno, ela para e pede instalação **no meio da
  prática**, com a turma esperando. Melhor tomar a vacina antes.
- Argumento que fechou: a "ferramenta de PDF" que as Práticas 06/07 mandam instalar é, na
  prática, Python + biblioteca. O material já empurrava uma instalação de Python — só que
  escondida atrás da palavra "ferramenta" e no pior momento.
- Enquadramento adotado (honesto, sem virar pré-requisito falso): seção **"A vacina"** no
  cap 02, entre a Porta B e o login, marcada como **recomendação forte** para quem vai fazer
  as práticas 05/06/07 e explicitamente pulável para quem só fará as de texto (08/09/10).
- Cuidado nº 1 no Windows: a caixinha `Add python.exe to PATH` do instalador, desmarcada por
  padrão — avisada 3x (passo, warning e toggler de "instalei mas não acha"). Alternativa sem
  senha de administrador: Microsoft Store. No Mac, costuma vir com as ferramentas do git.
- Adicionado também o **prompt de emergência** genérico ("não consigo instalar isso agora,
  tem outro jeito?") — vale para qualquer ferramenta faltante, não só Python.
- Ajustes de coerência: hero do cap 02 não promete mais "sem pré-requisitos escondidos";
  teaser do cap 01 fala em "um ou dois programas ajudantes"; `.precisa` das práticas 05, 06
  e 07 linkam para `../02-preparando/#vacina`.

## 2026-08-13 — Curso IA na Prática no branch (opção 3)
- Pedido: transformar o PDF Keynote `IA_na_Pratica_COMPLETO_3.pdf` (121 slides,
  6 módulos) no padrão HTML deste repo **sem atrapalhar a oficina Claude Code**.
- **Decisão de arquitetura (opção 3):** branch `feat/ia-na-pratica`; no branch o hub
  vira o curso de 6 módulos; a oficina atual move para `oficina/` como aprofundamento
  do Módulo 6. `master` permanece oficina pura até merge explícito.
- Estrutura: `index.html` (hub curso) · `modulos/01`…`06` · `oficina/` (hub + caps 01–11).
- Módulo 6 é teaser + CTA para `oficina/`; não duplica os 11 capítulos.
- Conteúdo dos módulos reescrito em prosa a partir do PDF (não slide-a-slide).
- Sem "Junho 2026" / datas no conteúdo HTML (regra da casa).
- Merge futuro: promove o curso a `master`; oficina permanece em `oficina/` (nada se perde).
  Hub secundário `oficina/index.html` já criado para porta direta "só Claude Code".

## 2026-08-16 — Módulo 05: Skills, MCP, Conectores e Plugins
- Expandido o Módulo 05 com: Skills (3 exemplos reais), o que é MCP (tomada padrão),
  Conectores (face do MCP no Claude + exemplos Drive/Gmail/Slack), Plugins (kit instalável),
  e quadro final Skill × Conector × Plugin.
- Fonte de nomes/papéis: docs oficiais de Connectors (claude.com/docs/connectors/overview).
  Sem inventar preços; lista de conectores dita como exemplos oficiais que podem mudar.
