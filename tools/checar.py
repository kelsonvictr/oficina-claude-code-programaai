#!/usr/bin/env python3
"""
Checagem rápida das regras da casa em todo HTML do material.

    python3 tools/checar.py            # tudo
    python3 tools/checar.py index.html # arquivos específicos

Verifica:
  1. Ligaduras — classes com fonte mono que não desativam liga/clig/calt
  2. Símbolos unicode proibidos no texto visível (-> virou seta, != virou ≠ ...)
  3. < > & não escapados dentro de <pre>
  4. Datas de semestre/ano letivo (material é reaproveitado todo semestre)
  5. Classes usadas no HTML que não existem em CSS nenhum (órfãs)
  6. goTo('x') / href="#x" apontando para id inexistente
  7. Colisão de nome: classe usada como modificador que também é componente
"""
import re, sys, os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SHARED = RAIZ / 'shared'

PROIBIDOS = {'→': '->', '⇒': '=>', '≠': '!=',
             '≥': '>=', '≤': '<=', '⟶': '->', '↘': '▪ (marcador neutro)'}

# ← e » são permitidos: são navegação decorativa, não operador copiável.
# Ver context/04-design-system.md.

problemas = []


def erro(arq, tipo, msg):
    problemas.append((arq, tipo, msg))


def css_de(texto):
    """Classes definidas + as regras completas, para checar ligaduras."""
    return set(re.findall(r'\.([a-zA-Z][\w-]*)', texto))


def blocos_css(texto):
    """[(seletor, corpo)] de cada regra, sem comentários grudados no seletor."""
    texto = re.sub(r'/\*.*?\*/', ' ', texto, flags=re.S)
    return [(sel.strip(), corpo)
            for sel, corpo in re.findall(r'([^{}]+)\{([^{}]*)\}', texto)]


def checar(arq: Path):
    try:
        nome = str(arq.relative_to(RAIZ))
    except ValueError:
        nome = str(arq)
    html = arq.read_text(encoding='utf-8')

    # --- separa <style> inline e o resto ---
    estilos_inline = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    corpo = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.S)
    corpo = re.sub(r'<script[^>]*>.*?</script>', '', corpo, flags=re.S)

    css_compartilhado = '\n'.join(
        p.read_text(encoding='utf-8') for p in sorted(SHARED.glob('*.css'))
    )
    css_total = css_compartilhado + '\n' + estilos_inline

    # 1) ligaduras
    kill = re.compile(r'font-feature-settings\s*:\s*["\']liga["\']\s*0', re.I)
    # cobertos pela regra global no topo do styles.css
    global_kill = set()
    for seletor, regra in blocos_css(css_compartilhado):
        if kill.search(regra):
            global_kill.update(s.strip() for s in seletor.split(','))
    for seletor, regra in blocos_css(css_total):
        alvo = seletor.strip()
        if re.search(r'font-family\s*:[^;]*(mono|JetBrains)', regra, re.I):
            coberto = alvo in global_kill or alvo.split()[-1] in global_kill
            if not kill.search(regra) and not coberto:
                erro(nome, 'ligaduras',
                     f'{alvo} usa fonte mono sem desativar liga/clig/calt')

    # 2) símbolos proibidos no texto visível
    for simbolo, correto in PROIBIDOS.items():
        for m in re.finditer(re.escape(simbolo), corpo):
            ctx = corpo[max(0, m.start() - 45):m.start() + 45].replace('\n', ' ')
            erro(nome, 'unicode',
                 f'"{simbolo}" (devia ser "{correto}") em: ...{ctx.strip()}...')

    # 3) escape dentro de <pre>
    for pre in re.findall(r'<pre[^>]*>(.*?)</pre>', html, re.S):
        limpo = re.sub(r'<span[^>]*>|</span>|<br\s*/?>', '', pre)
        for m in re.finditer(r'[<>]|&(?!(amp|lt|gt|quot|#\d+|nbsp);)', limpo):
            ctx = limpo[max(0, m.start() - 35):m.start() + 35].replace('\n', ' ')
            erro(nome, 'escape',
                 f'"{m.group()}" cru dentro de <pre>: ...{ctx.strip()}...')

    # 4) datas de semestre
    # "dados de um semestre completo" é conteúdo legítimo; datar o CURSO não é
    data_letiva = (r'\b20[2-9]\d\.[12]\b'                      # 2026.1
                   r'|semestre\s+letivo'
                   r'|\b(?:neste|nesse|deste|desse|no\s+pr[óo]ximo|no\s+atual)\s+semestre\b'
                   r'|semestre\s+de\s+20\d\d'
                   r'|\b(?:turma|per[ií]odo|ano\s+letivo|aula)\w*\s+'
                   r'(?:de\s+)?20[2-9]\d\b'                        # "turma de 2027"
                   r'|\b20[3-9]\d\b')                              # ano futuro nu
    for m in re.finditer(data_letiva, corpo, re.I):
        erro(nome, 'data-semestre',
             f'"{m.group()}" — o material é reaproveitado, não datar')

    # 5) classes órfãs
    definidas = css_de(css_total)
    usadas = set()
    for attr in re.findall(r'class="([^"]*)"', html):
        usadas.update(c for c in attr.split() if c)
    for c in sorted(usadas - definidas):
        erro(nome, 'classe-orfa', f'.{c} usada no HTML e não definida em CSS nenhum')

    # 6) âncoras quebradas
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    for alvo in re.findall(r"goTo\(\s*'([^']+)'\s*\)", html) + re.findall(r'href="#([^"]+)"', html):
        if alvo not in ids:
            erro(nome, 'ancora', f'aponta para #{alvo}, que não existe no arquivo')

    # 7) colisão modificador x componente
    #    ex.: <span class="chat-msg tela"> quando .tela é componente próprio
    componentes = {'sim', 'timeline', 'card', 'quiz', 'concept', 'analogy',
                   'terminal', 'checklist', 'tela', 'precisa', 'armadilha'}
    for attr in re.findall(r'class="([^"]*)"', html):
        cs = attr.split()
        if len(cs) > 1:
            for c in cs[1:]:
                if c in componentes:
                    erro(nome, 'colisao',
                         f'"{c}" é componente, mas está sendo usado como modificador '
                         f'em class="{attr}" — o CSS do componente vai vazar')


alvos = [Path(a) for a in sys.argv[1:]] or sorted(RAIZ.glob('**/*.html'))
alvos = [a if a.is_absolute() else RAIZ / a for a in alvos]
alvos = [a for a in alvos if 'node_modules' not in str(a)]

for a in alvos:
    checar(a)

if not problemas:
    print(f'✅ {len(alvos)} arquivo(s) sem problemas.')
    sys.exit(0)

atual = None
for arq, tipo, msg in problemas:
    if arq != atual:
        print(f'\n📄 {arq}')
        atual = arq
    print(f'   [{tipo}] {msg}')
print(f'\n❌ {len(problemas)} problema(s) em {len(alvos)} arquivo(s).')
sys.exit(1)
