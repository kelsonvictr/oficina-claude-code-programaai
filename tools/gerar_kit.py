#!/usr/bin/env python3
"""
Gera o Kit da Oficina em assets/kit/ — arquivos de treino 100% fictícios.

    python3 tools/gerar_kit.py

Determinístico (random.seed fixo): rodar de novo produz o mesmo kit.
Só usa a biblioteca padrão. Nomes, valores e pessoas são inventados;
qualquer semelhança é coincidência. O zip final (kit-oficina.zip) é o
que o participante baixa no Cap 03.

Estrutura gerada:
  kit/
    bagunca/                  Prática 04 — ~40 arquivos mistos e mal nomeados
    planilha/gastos-2025.csv  Prática 05 — 300 lançamentos com sujeira proposital
    declaracoes/              Prática 06 — participantes.csv + modelo-declaracao.txt
    contrato/                 Prática 07 — contrato PDF de 40 págs + 3 anexos
    marketing/                Prática 08 — release-produto.txt
    professor/                Prática 09 — apostila-capitulo.txt
  kit-oficina.zip
"""
import base64
import csv
import io
import random
import shutil
import zipfile
from pathlib import Path

random.seed(42)

RAIZ = Path(__file__).resolve().parent.parent
KIT = RAIZ / 'assets' / 'kit'
PASTA = KIT / 'kit'

# ─────────────────────────────────────────────────────────────
# Imagens mínimas válidas (1x1 px) — o conteúdo não importa,
# só a extensão e o fato de abrirem sem erro.
# ─────────────────────────────────────────────────────────────
JPEG_1PX = base64.b64decode(
    '/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRof'
    'Hh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAABAAEBAREA/8QAFAAB'
    'AAAAAAAAAAAAAAAAAAAACf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/2gAIAQEAAD8AVN//2Q==')
PNG_1PX = base64.b64decode(
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA'
    '60e6kgAAAABJRU5ErkJggg==')


# ─────────────────────────────────────────────────────────────
# Mini-gerador de PDF (Helvetica, WinAnsi) — o suficiente para
# PDFs de treino que abrem em qualquer leitor.
# ─────────────────────────────────────────────────────────────
def _pdf_escape(linha: str) -> bytes:
    txt = linha.replace('\\', r'\\').replace('(', r'\(').replace(')', r'\)')
    return txt.encode('cp1252', errors='replace')


def make_pdf(caminho: Path, paginas):
    """paginas: lista de páginas; cada página é uma lista de linhas (str)."""
    objetos = []          # (num, bytes) — numerados a partir de 1

    def add(corpo: bytes) -> int:
        objetos.append(corpo)
        return len(objetos)

    n_font = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica '
                 b'/Encoding /WinAnsiEncoding >>')
    nums_paginas = []
    # reservamos o obj /Pages depois; primeiro conteúdos e páginas
    conteudos = []
    for linhas in paginas:
        fluxo = io.BytesIO()
        fluxo.write(b'BT /F1 11 Tf 50 800 Td 15 TL\n')
        for linha in linhas:
            fluxo.write(b'(' + _pdf_escape(linha) + b') Tj T*\n')
        fluxo.write(b'ET')
        dados = fluxo.getvalue()
        n_cont = add(b'<< /Length ' + str(len(dados)).encode() + b' >>\nstream\n'
                     + dados + b'\nendstream')
        conteudos.append(n_cont)

    n_pages = len(objetos) + len(paginas) + 1   # número que o obj /Pages terá
    for n_cont in conteudos:
        n_pg = add(f'<< /Type /Page /Parent {n_pages} 0 R '
                   f'/MediaBox [0 0 595 842] '
                   f'/Resources << /Font << /F1 {n_font} 0 R >> >> '
                   f'/Contents {n_cont} 0 R >>'.encode())
        nums_paginas.append(n_pg)

    kids = ' '.join(f'{n} 0 R' for n in nums_paginas)
    add(f'<< /Type /Pages /Kids [{kids}] /Count {len(nums_paginas)} >>'.encode())
    n_cat = add(f'<< /Type /Catalog /Pages {n_pages} 0 R >>'.encode())

    saida = io.BytesIO()
    saida.write(b'%PDF-1.4\n')
    offsets = [0]
    for i, corpo in enumerate(objetos, start=1):
        offsets.append(saida.tell())
        saida.write(f'{i} 0 obj\n'.encode() + corpo + b'\nendobj\n')
    inicio_xref = saida.tell()
    saida.write(f'xref\n0 {len(objetos) + 1}\n'.encode())
    saida.write(b'0000000000 65535 f \n')
    for off in offsets[1:]:
        saida.write(f'{off:010d} 00000 n \n'.encode())
    saida.write(f'trailer\n<< /Size {len(objetos) + 1} /Root {n_cat} 0 R >>\n'
                f'startxref\n{inicio_xref}\n%%EOF'.encode())
    caminho.write_bytes(saida.getvalue())


# ─────────────────────────────────────────────────────────────
# PRÁTICA 04 — a pasta bagunçada
# ─────────────────────────────────────────────────────────────
def gerar_bagunca():
    pasta = PASTA / 'bagunca'
    pasta.mkdir(parents=True, exist_ok=True)

    def txt(nome, conteudo):
        (pasta / nome).write_text(conteudo, encoding='utf-8')

    # fotos (jpg/png mínimos)
    for n in range(8274, 8282):
        (pasta / f'IMG_{n}.jpg').write_bytes(JPEG_1PX)
    (pasta / 'cópia de IMG_8274.jpg').write_bytes(JPEG_1PX)      # duplicada
    (pasta / 'foto perfil nova (1).jpg').write_bytes(JPEG_1PX)
    (pasta / 'WhatsApp Image at 09.12.45.jpeg').write_bytes(JPEG_1PX)
    (pasta / 'print_tela.png').write_bytes(PNG_1PX)
    (pasta / 'Captura de Tela às 14.33.10.png').write_bytes(PNG_1PX)
    (pasta / 'logo-final-AGORA-VAI.png').write_bytes(PNG_1PX)
    (pasta / 'logo-final-AGORA-VAI (2).png').write_bytes(PNG_1PX)  # duplicada

    # textos
    relatorio = ('Relatório de atividades do trimestre\n\n'
                 '1. Atendimentos realizados: 312\n'
                 '2. Pendências: 8\n'
                 '3. Observações: aguardando retorno do fornecedor.\n')
    txt('relatorio final.txt', relatorio)
    txt('relatorio final FINAL.txt', relatorio)                   # duplicado
    txt('relatorio final FINAL (2).txt', relatorio)               # duplicado
    txt('anotações reunião.txt',
        'Reunião de equipe\n- Revisar orçamento\n- Confirmar fornecedor de café\n'
        '- Próxima reunião: quinta-feira\n')
    txt('anotacoes reuniao (cópia).txt',
        'Reunião de equipe\n- Revisar orçamento\n- Confirmar fornecedor de café\n'
        '- Próxima reunião: quinta-feira\n')                      # duplicado disfarçado
    txt('lista de compras.txt', 'café\naçúcar\npapel A4\ngrampeador\npost-its\n')
    txt('senha do wifi.txt',
        'Wi-Fi do escritório: Escritorio_2andar\nSenha: troque-me-depois-123\n'
        '(fictícia, claro — mas guarde senhas num lugar seguro, hein?)\n')
    txt('rascunho email chefe.txt',
        'Assunto: Proposta de melhoria\n\nOlá, tudo bem?\n\n'
        'Segue em anexo a proposta que conversamos... (terminar depois!!!)\n')
    txt('ideias.txt', 'ideia 1: automatizar os relatórios\nideia 2: ver aquele curso\n')
    txt('sem título.txt', 'aaa teste\n')
    txt('sem título (2).txt', 'teste de novo\n')

    # planilhas
    txt('orçamento móveis.csv',
        'item;quantidade;valor_unitario\nmesa;2;450,00\ncadeira;6;280,00\n'
        'armário;1;790,00\n')
    txt('contatos exportados.csv',
        'nome;telefone;email\nAna Beltrão;83 90000-0001;ana@example.com\n'
        'Carlos Nunes;83 90000-0002;carlos@example.com\n'
        'Marina Souza;83 90000-0003;marina@example.com\n')
    txt('vendas_marco.csv',
        'dia;produto;quantidade;total\n03;garrafa térmica;4;996,00\n'
        '07;caneca;12;348,00\n15;garrafa térmica;2;498,00\n21;mochila;3;897,00\n')

    # PDFs pequenos
    make_pdf(pasta / 'scan0001.pdf',
             [['Documento digitalizado', '', 'Página única de um scan antigo.',
               'Conteúdo ilegível de propósito — é só um arquivo de treino.']])
    make_pdf(pasta / 'scan0002.pdf',
             [['Documento digitalizado (2)', '', 'Outro scan perdido na pasta.']])
    make_pdf(pasta / 'boleto condominio.pdf',
             [['BOLETO — CONDOMÍNIO EDIFÍCIO PRIMAVERA (FICTÍCIO)', '',
               'Valor: R$ 412,00', 'Vencimento: dia 10', 'Unidade: 302-B']])
    make_pdf(pasta / 'manual-cafeteira.pdf',
             [['MANUAL DA CAFETEIRA TURBO 3000 (FICTÍCIA)', '',
               '1. Coloque água no reservatório.', '2. Coloque o pó no filtro.',
               '3. Aperte o botão. Pronto.'],
              ['GARANTIA', '', 'Este produto fictício tem garantia eterna,',
               'pois não existe.']])
    make_pdf(pasta / 'comprovante pix.pdf',
             [['COMPROVANTE DE TRANSFERÊNCIA (FICTÍCIO)', '',
               'Valor: R$ 89,90', 'Para: Livraria Boa Página',
               'Identificador: TREINO-0001']])
    print(f'  bagunca/: {len(list(pasta.iterdir()))} arquivos')


# ─────────────────────────────────────────────────────────────
# PRÁTICA 05 — a planilha de gastos
# ─────────────────────────────────────────────────────────────
def gerar_gastos():
    pasta = PASTA / 'planilha'
    pasta.mkdir(parents=True, exist_ok=True)

    categorias = {
        'Alimentação': ['restaurante', 'lanche da tarde', 'padaria', 'delivery jantar',
                        'almoço com cliente', 'sorveteria'],
        'Mercado': ['compra do mês', 'feira', 'hortifruti', 'açougue', 'mercadinho'],
        'Transporte': ['combustível', 'aplicativo de corrida', 'estacionamento',
                       'ônibus', 'pedágio'],
        'Moradia': ['energia elétrica', 'água', 'internet', 'gás', 'condomínio'],
        'Saúde': ['farmácia', 'consulta', 'exame', 'academia'],
        'Lazer': ['cinema', 'streaming', 'show', 'livraria', 'passeio fim de semana'],
        'Educação': ['curso online', 'material escolar', 'mensalidade curso de inglês'],
    }
    # variações sujas de grafia por categoria (o "problema" da prática)
    def sujar(cat):
        formas = [cat, cat, cat, cat.lower(), cat.upper(),
                  cat.lower().replace('ç', 'c').replace('ã', 'a')]
        return random.choice(formas)

    faixas = {'Alimentação': (18, 140), 'Mercado': (45, 620), 'Transporte': (8, 260),
              'Moradia': (60, 780), 'Saúde': (25, 480), 'Lazer': (15, 220),
              'Educação': (40, 460)}

    linhas = []
    for mes in range(1, 13):
        for _ in range(25):
            cat = random.choice(list(categorias))
            dia = random.randint(1, 28)
            desc = random.choice(categorias[cat])
            lo, hi = faixas[cat]
            valor = round(random.uniform(lo, hi), 2)
            linhas.append([f'{dia:02d}/{mes:02d}/2025', desc, sujar(cat),
                           f'{valor:.2f}'.replace('.', ',')])

    # sujeira proposital: 5 duplicatas exatas, 6 categorias vazias, 1 valor absurdo
    for linha in random.sample(linhas, 5):
        linhas.append(list(linha))
    for linha in random.sample(linhas, 6):
        linha[2] = ''
    linhas.append(['17/08/2025', 'jantar de aniversário', 'Alimentação', '4890,00'])

    linhas.sort(key=lambda l: (l[0][6:], l[0][3:5], l[0][:2]))
    with open(pasta / 'gastos-2025.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['data', 'descricao', 'categoria', 'valor'])
        w.writerows(linhas)
    print(f'  planilha/gastos-2025.csv: {len(linhas)} lançamentos')


# ─────────────────────────────────────────────────────────────
# PRÁTICA 06 — declarações em lote
# ─────────────────────────────────────────────────────────────
NOMES = ['Ana Clara Beltrão', 'Bruno Cavalcanti', 'Camila Duarte', 'Diego Ferreira',
         'Elisa Fontes', 'Fábio Guimarães', 'Gabriela Holanda', 'Heitor Lins',
         'Isadora Maia', 'João Pedro Nóbrega', 'Karina Oliveira', 'Lucas Pontes',
         'Mariana Queiroz', 'Nícolas Ramos', 'Olívia Santana', 'Paulo Tavares',
         'Quésia Uchoa', 'Rafael Vasconcelos', 'Sofia Wanderley', 'Tiago Ximenes',
         'Úrsula Azevedo', 'Vicente Barros', 'Wesley Cordeiro', 'Yasmin Dantas',
         'Arthur Espínola', 'Beatriz Farias', 'Caio Galvão', 'Daniela Henriques',
         'Emanuel Iglesias', 'Flávia Julião']


def gerar_declaracoes():
    pasta = PASTA / 'declaracoes'
    pasta.mkdir(parents=True, exist_ok=True)

    cursos = [('Oficina de Comunicação Escrita', 20),
              ('Curso de Atendimento ao Público', 40),
              ('Introdução à Organização de Arquivos', 12)]
    with open(pasta / 'participantes.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['matricula', 'nome', 'curso', 'carga_horaria'])
        for i, nome in enumerate(NOMES, start=1):
            curso, carga = random.choice(cursos)
            w.writerow([f'AUR-{i:04d}', nome, curso, carga])

    (pasta / 'modelo-declaracao.txt').write_text(
        'DECLARAÇÃO DE PARTICIPAÇÃO\n'
        '\n'
        'Declaramos, para os devidos fins, que {{NOME}} (matrícula {{MATRICULA}})\n'
        'participou do curso "{{CURSO}}", promovido pelo Instituto Aurora de\n'
        'Capacitação, com carga horária total de {{CARGA_HORARIA}} horas,\n'
        'tendo cumprido todas as atividades previstas.\n'
        '\n'
        'Esta declaração é emitida a pedido da pessoa interessada.\n'
        '\n'
        '______________________________________\n'
        'Coordenação de Cursos — Instituto Aurora de Capacitação\n'
        '(instituição fictícia, criada para esta oficina)\n',
        encoding='utf-8')
    print(f'  declaracoes/: {len(NOMES)} participantes + modelo')


# ─────────────────────────────────────────────────────────────
# PRÁTICA 07 — o contrato de 40 páginas
# ─────────────────────────────────────────────────────────────
ORDINAIS = ['PRIMEIRA', 'SEGUNDA', 'TERCEIRA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÉTIMA',
            'OITAVA', 'NONA', 'DÉCIMA', 'DÉCIMA PRIMEIRA', 'DÉCIMA SEGUNDA',
            'DÉCIMA TERCEIRA', 'DÉCIMA QUARTA', 'DÉCIMA QUINTA', 'DÉCIMA SEXTA',
            'DÉCIMA SÉTIMA', 'DÉCIMA OITAVA', 'DÉCIMA NONA', 'VIGÉSIMA']


def gerar_contrato():
    pasta = PASTA / 'contrato'
    pasta.mkdir(parents=True, exist_ok=True)

    temas = [
        ('DO OBJETO', ['O presente contrato tem por objeto a prestação de serviços',
                       'de manutenção preventiva e corretiva dos equipamentos de',
                       'refrigeração da CONTRATANTE, conforme Anexo A.']),
        ('DO PRAZO', ['O contrato vigorará pelo prazo de 24 (vinte e quatro) meses,',
                      'contados da data de assinatura, prorrogável por igual período',
                      'mediante termo aditivo.']),
        ('DO VALOR', ['Pelos serviços, a CONTRATANTE pagará à CONTRATADA o valor',
                      'mensal de R$ 7.350,00 (sete mil, trezentos e cinquenta reais),',
                      'com vencimento todo dia 5 (cinco) de cada mês.']),
        ('DO REAJUSTE', ['O valor mensal será reajustado anualmente pela variação',
                         'do IPCA acumulado nos 12 (doze) meses anteriores.']),
        ('DA MULTA POR RESCISÃO', ['A rescisão imotivada por qualquer das partes',
                                   'implicará multa de R$ 14.700,00 (catorze mil e',
                                   'setecentos reais), equivalente a duas mensalidades.']),
        ('DA GARANTIA', ['Os serviços executados terão garantia de 3 (três) meses,',
                         'contados da conclusão de cada atendimento.']),
        ('DA CONFIDENCIALIDADE', ['As partes manterão sigilo sobre informações trocadas',
                                  'durante a vigência e por 5 (cinco) anos após o término.']),
        ('DO ATENDIMENTO', ['Chamados urgentes serão atendidos em até 6 (seis) horas',
                            'úteis; chamados comuns, em até 2 (dois) dias úteis.']),
        ('DAS OBRIGAÇÕES DA CONTRATADA', ['Executar os serviços com pessoal habilitado,',
                                          'fornecer relatório mensal de atividades e manter',
                                          'seguro de responsabilidade civil vigente.']),
        ('DAS OBRIGAÇÕES DA CONTRATANTE', ['Garantir acesso às instalações, comunicar',
                                           'defeitos em até 48 (quarenta e oito) horas e',
                                           'efetuar os pagamentos nos prazos ajustados.']),
        ('DO FORO', ['Fica eleito o foro da Comarca de João Pessoa/PB para dirimir',
                     'quaisquer controvérsias oriundas do presente instrumento.']),
    ]
    enchimento = [
        'Parágrafo primeiro. As condições aqui previstas aplicam-se a todas as',
        'unidades da CONTRATANTE relacionadas no Anexo B, incluindo eventuais',
        'filiais inauguradas durante a vigência, desde que comunicadas por escrito.',
        'Parágrafo segundo. A tolerância de qualquer das partes quanto ao',
        'descumprimento de obrigação não implicará novação ou renúncia de direito.',
        'Parágrafo terceiro. As comunicações entre as partes serão feitas por',
        'escrito, preferencialmente por meio eletrônico, com confirmação de leitura.',
    ]

    paginas = [[
        'CONTRATO DE PRESTAÇÃO DE SERVIÇOS Nº 041/TREINO',
        '',
        'CONTRATANTE: Supermercados Bom Preço do Vale Ltda. (fictícia)',
        'CONTRATADA: RefriTec Manutenção e Serviços ME (fictícia)',
        '',
        'As partes acima identificadas celebram o presente contrato de',
        'prestação de serviços, que se regerá pelas cláusulas seguintes.',
        '',
        'AVISO: documento inteiramente fictício, gerado para treino de',
        'leitura de PDF na Oficina Claude Code. Não possui valor legal.',
    ]]
    clausula = 0
    while len(paginas) < 40:
        tema, corpo = temas[clausula % len(temas)]
        num = ORDINAIS[clausula % len(ORDINAIS)]
        pagina = [f'CLÁUSULA {num} — {tema}', ''] + corpo + ['']
        while len(pagina) < 44:
            pagina.append(enchimento[len(pagina) % len(enchimento)])
        paginas.append(pagina)
        clausula += 1
    paginas.append(['E, por estarem justas e contratadas, as partes assinam o',
                    'presente instrumento em duas vias de igual teor.',
                    '', 'João Pessoa/PB.', '',
                    '________________________________  (CONTRATANTE)',
                    '', '________________________________  (CONTRATADA)'])
    make_pdf(pasta / 'contrato-prestacao-servicos.pdf', paginas)

    make_pdf(pasta / 'anexo-a-equipamentos.pdf',
             [['ANEXO A — RELAÇÃO DE EQUIPAMENTOS', '',
               '01. Câmara fria de laticínios — setor 2',
               '02. Câmara fria de congelados — setor 2',
               '03. Balcões refrigerados (8 unidades) — setor 1',
               '04. Ilhas de congelados (4 unidades) — setor 3',
               '05. Ar-condicionado central — administração']])
    make_pdf(pasta / 'anexo-b-unidades.pdf',
             [['ANEXO B — UNIDADES ATENDIDAS', '',
               'Unidade Centro — Rua das Acácias, 120',
               'Unidade Sul — Av. dos Ipês, 4550',
               'Unidade Norte — Rod. BR-000, km 12']])
    make_pdf(pasta / 'anexo-c-precos-avulsos.pdf',
             [['ANEXO C — TABELA DE PREÇOS AVULSOS', '',
               'Visita técnica extra ................ R$ 380,00',
               'Hora técnica adicional .............. R$ 190,00',
               'Plantão de fim de semana ............ R$ 620,00']])
    print(f'  contrato/: {len(paginas)} páginas + 3 anexos')


# ─────────────────────────────────────────────────────────────
# PRÁTICA 08 — marketing
# ─────────────────────────────────────────────────────────────
def gerar_marketing():
    pasta = PASTA / 'marketing'
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / 'release-produto.txt').write_text(
        'RELEASE PARA IMPRENSA — AURORA TERMO 500 (produto fictício)\n'
        '\n'
        'A Aurora Casa & Escritório apresenta a Termo 500, sua nova garrafa\n'
        'térmica inteligente. Desenvolvida durante dois anos com engenheiros\n'
        'de materiais, a Termo 500 mantém bebidas quentes por 12 horas e\n'
        'geladas por 24 horas, e traz um pequeno visor de temperatura na tampa.\n'
        '\n'
        'PRINCIPAIS CARACTERÍSTICAS\n'
        '- Capacidade: 500 ml\n'
        '- Visor de temperatura na tampa (bateria dura 2 anos)\n'
        '- Aço inox com parede tripla e acabamento fosco\n'
        '- 6 cores: grafite, areia, verde-mata, terracota, azul-noite e branco\n'
        '- Tampa com trava antivazamento testada em 10 mil ciclos\n'
        '- Livre de BPA\n'
        '\n'
        'PREÇO E DISPONIBILIDADE\n'
        'A Termo 500 chega às lojas no próximo mês por R$ 249,00, com\n'
        'pré-venda no site oficial a R$ 219,00 e frete grátis na primeira semana.\n'
        '\n'
        'CITAÇÃO\n'
        '"A gente queria acabar com aquele gole de café frio traiçoeiro das\n'
        '15h. O visor conta a verdade antes de você abrir a garrafa", afirma\n'
        'Helena Vasques, diretora de produto da Aurora (executiva fictícia).\n'
        '\n'
        'SOBRE A AURORA\n'
        'Fundada em João Pessoa, a Aurora Casa & Escritório cria objetos de\n'
        'uso diário com foco em durabilidade. A empresa (fictícia) emprega\n'
        '120 pessoas e exporta para 4 países.\n'
        '\n'
        'CONTATO DE IMPRENSA\n'
        'imprensa@aurora-exemplo.com.br — (83) 90000-0000\n',
        encoding='utf-8')
    print('  marketing/release-produto.txt')


# ─────────────────────────────────────────────────────────────
# PRÁTICA 09 — professor
# ─────────────────────────────────────────────────────────────
def gerar_professor():
    pasta = PASTA / 'professor'
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / 'apostila-capitulo.txt').write_text(
        'APOSTILA DE EDUCAÇÃO FINANCEIRA — CAPÍTULO 3\n'
        'JUROS COMPOSTOS NO DIA A DIA\n'
        '\n'
        '3.1 O QUE SÃO JUROS COMPOSTOS\n'
        'Juros compostos são juros calculados sobre o valor inicial MAIS os\n'
        'juros já acumulados. É o famoso "juros sobre juros". Nos juros\n'
        'simples, o cálculo é sempre sobre o valor inicial; nos compostos,\n'
        'a base de cálculo cresce a cada período.\n'
        '\n'
        'Exemplo: R$ 1.000,00 aplicados a 1% ao mês.\n'
        '- Mês 1: 1.000,00 + 10,00 = 1.010,00\n'
        '- Mês 2: 1.010,00 + 10,10 = 1.020,10\n'
        '- Mês 3: 1.020,10 + 10,20 = 1.030,30\n'
        'A diferença parece pequena no início, mas cresce rápido com o tempo.\n'
        '\n'
        '3.2 A FÓRMULA\n'
        'M = C x (1 + i)^t, onde:\n'
        'M = montante final, C = capital inicial, i = taxa por período,\n'
        't = número de períodos. A taxa entra em forma decimal (1% = 0,01).\n'
        '\n'
        '3.3 ONDE OS JUROS COMPOSTOS APARECEM A FAVOR\n'
        '- Poupança e investimentos de renda fixa\n'
        '- Reinvestimento de dividendos\n'
        '- Aportes mensais constantes (o tempo é o melhor amigo do investidor)\n'
        '\n'
        '3.4 ONDE ELES APARECEM CONTRA\n'
        '- Rotativo do cartão de crédito (taxas mensais altíssimas)\n'
        '- Cheque especial\n'
        '- Parcelamentos longos com juros embutidos\n'
        'Regra prática: dívida cara cresce mais rápido que investimento seguro.\n'
        'Por isso, quitar dívidas caras costuma vir antes de investir.\n'
        '\n'
        '3.5 O EFEITO DO TEMPO\n'
        'Dobrar o TEMPO de uma aplicação rende mais que dobrar o VALOR\n'
        'aplicado, quando o prazo é longo. Uma aproximação útil é a "regra\n'
        'dos 72": dividir 72 pela taxa anual dá uma estimativa de quantos\n'
        'anos o dinheiro leva para dobrar (a 8% ao ano: 72 / 8 = 9 anos).\n'
        '\n'
        '3.6 RESUMO DO CAPÍTULO\n'
        '- Juros compostos incidem sobre capital + juros acumulados.\n'
        '- A fórmula do montante é M = C x (1 + i)^t.\n'
        '- O tempo é o fator mais poderoso da fórmula.\n'
        '- O mesmo mecanismo que multiplica investimentos multiplica dívidas.\n'
        '- Regra dos 72: estimativa rápida do tempo para dobrar um valor.\n'
        '\n'
        'EXERCÍCIOS PROPOSTOS (para a próxima aula)\n'
        '1. Calcule o montante de R$ 500,00 a 2% ao mês por 3 meses.\n'
        '2. Pela regra dos 72, em quanto tempo dobra um valor a 6% ao ano?\n'
        '3. Cite duas situações em que os juros compostos jogam contra você.\n',
        encoding='utf-8')
    print('  professor/apostila-capitulo.txt')


# ─────────────────────────────────────────────────────────────
def main():
    if PASTA.exists():
        shutil.rmtree(PASTA)
    PASTA.mkdir(parents=True)
    print('Gerando o Kit da Oficina…')
    gerar_bagunca()
    gerar_gastos()
    gerar_declaracoes()
    gerar_contrato()
    gerar_marketing()
    gerar_professor()

    zip_path = KIT / 'kit-oficina.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for arq in sorted(PASTA.rglob('*')):
            if arq.is_file():
                z.write(arq, arq.relative_to(KIT))
    tamanho = zip_path.stat().st_size / 1024
    print(f'  kit-oficina.zip: {tamanho:.0f} KB')
    print('✅ Kit pronto em assets/kit/')


if __name__ == '__main__':
    main()
