# Plano de capítulos — Oficina Claude Code

> **Localização neste branch:** os capítulos abaixo vivem em `oficina/` (não mais em
> `capitulos/`). O hub da oficina é `oficina/index.html`. O arco do **curso** de 6
> módulos está em `02b-plano-modulos.md`.

Arco em 3 atos: **entender → preparar → praticar** (+ fechamento). As práticas são
independentes entre si — o participante escolhe pelas suas dores/área. Numeração fixa;
práticas novas entram como 10b, 10c... antes do fechamento.

## Ato 1 — Base (todo mundo passa por aqui)

### 01 · O que é o Claude Code? 🤝
Conceito: "um assistente que mora no SEU computador e mexe nos SEUS arquivos — conversando
em português". Fluxo animado central: você pede → ele lê → ele propõe → VOCÊ aprova → ele faz
→ você confere. Mito×Realidade: "preciso saber programar" / "ele vai apagar meus arquivos" /
"é só um ChatGPT". Galeria do que dá para fazer (gancho para as práticas). Transparência de
custo: exige plano pago (Pro ~US$20/mês) — dito sem rodeio, com link para claude.com/pricing.

### 02 · Preparando o computador 🧰
Duas portas de entrada, escolhidas por um seletor interativo:
- **Porta A (recomendada p/ a oficina): app desktop** — download mac/win, janela com abas, sem terminal.
- **Porta B: terminal** — desmistificação ("uma janela de conversa sem botões"), instalador
  nativo (1 comando; PowerShell no Win, curl no mac), SEM Node, SEM git obrigatório.
Login OAuth passo a passo com telas simuladas. Checklist final "estou pronto". Solução de
problemas comuns (comando não encontrado, navegador não abriu, código de 6 caracteres).
Fatos verificados em `03-fatos-instalacao.md` — NÃO inventar flags/comandos.

### 03 · A primeira conversa 💬
Criar a pasta da oficina; baixar o **Kit da Oficina** (zip com os arquivos das práticas);
abrir o Claude Code NA pasta certa (conceito-chave: ele enxerga a pasta onde foi aberto).
Anatomia de um bom pedido (contexto + o quê + como quero o resultado). O ciclo de permissão
(ele SEMPRE pede antes — simulador de aprovar/recusar). "Apareceu código na tela — e agora?"
(resposta: respira, olha o resultado final, o código é o bastidor). Comandos de sobrevivência:
Esc interrompe, /help, /clear, fechar e voltar.

## Ato 2 — Práticas (escolha as suas)

Cada prática segue o MESMO esqueleto (ver design-system, componente `.pratica`):
cenário-história → 🧾 "o que você vai precisar" → arquivos do kit → prompts prontos
copiáveis → 🖥️ "o que vai aparecer na tela" → conferindo o resultado → variações para a
SUA vida → armadilhas da prática → desafio solo.

### 04 · 🗂️ Domando a pasta bagunçada — universal · ★☆☆
Kit: pasta `bagunca/` com ~40 arquivos mistos (fotos, pdfs, docs, planilhas com nomes péssimos).
Organizar por tipo, renomear em lote com padrão de data, achar duplicados, relatório do que mudou.
Conceito embutido: pedir um PLANO antes de deixar mexer.

### 05 · 📊 A planilha que se analisa sozinha — financeiro/adm · ★★☆
Kit: `gastos-2025.csv` (300 linhas de despesas com sujeira proposital). Perguntar em português
("quanto gastei por categoria?"), gerar resumo, gráfico em HTML, achar lançamentos estranhos.
Conceito: Claude escreve e roda scripts nos bastidores — você só valida números.

### 06 · 📄 Cem declarações em cinco minutos — secretaria/RH · ★★☆
Kit: `participantes.csv` + `modelo-declaracao.txt`. Mala direta sem Word: gerar 1 documento
por pessoa (docx/pdf), nome de arquivo padronizado. Conceito: descrever o RESULTADO, não o passo a passo.

### 07 · 📚 O contrato de 40 páginas — jurídico/contábil · ★★☆
Kit: contrato fictício em PDF + 3 PDFs para juntar. Resumir por cláusulas, extrair datas e
valores para tabela, juntar/dividir PDFs. Conceito: conferir SEMPRE na fonte (alucinação dita
com todas as letras).

### 08 · 📣 Um texto vira dez — marketing/comunicação · ★☆☆
Kit: `release-produto.txt`. Gerar posts por canal (Instagram, LinkedIn, e-mail), tabela-calendário,
tom de voz consistente via arquivo de instruções (primeiro contato com CLAUDE.md, sem dizer o nome
técnico ainda: "o caderninho de regras").

### 09 · 🧑‍🏫 A prova que se monta sozinha — educação · ★★☆
Kit: `apostila-capitulo.txt`. Gerar quiz com gabarito comentado, versões A/B embaralhadas,
lista de presença formatada. Conceito: iterar ("agora mais difícil", "troque a questão 3").

### 10 · 🌐 Seu cantinho na internet — todos · ★★★ (momento UAU de fechamento)
Do zero: página pessoal/currículo/cardápio em HTML, aberta no navegador ao vivo, iterada por
conversa ("põe uma foto", "muda a cor"). Conceito: o ciclo pedir→ver→ajustar é o superpoder.

## Ato 3 — Fechamento

### 11 · 🧭 E agora? Segurança, hábitos e a máquina do tempo
Hábitos: pasta de trabalho dedicada, pedir plano antes, revisar antes de aprovar, desconfiar
de números (conferir na fonte). Limites honestos: alucina, erra, custa dinheiro/limite de uso.
O caderninho de regras (CLAUDE.md) oficializado. **Git = máquina do tempo** (opcional,
apresentado como "peça ao Claude que ele instala e configura pra você"). Onde continuar.

## Kit da Oficina (`assets/kit/`)
Zip único `kit-oficina.zip` + pastas individuais por prática. Todos os dados são FICTÍCIOS
(nomes, CPFs inválidos por design, valores inventados). Gerar via script `tools/gerar_kit.py`
para reprodutibilidade.
