/* =========================================================
   Oficina Claude Code — para quem nunca programou
   shared/scripts.js — sidebar, progresso, scroll-reveal, quiz,
   toggler, fluxos autoplay, sequências data-seq, terminal,
   linha do tempo, carimbo de mito, copiar prompt.

   Regra da casa: TUDO dispara sozinho quando entra na tela
   (IntersectionObserver). O aluno nunca precisa achar um "play";
   botão só existe para REPETIR.
   ========================================================= */

/* ---------- Toggler (revelar resposta) ---------- */
function toggleSection(headerEl){
  const body   = headerEl.nextElementSibling;
  const isOpen = headerEl.classList.toggle('open');
  if (body) body.classList.toggle('open', isOpen);
}

/* ---------- Sidebar ---------- */
function openSidebar(){
  document.querySelector('.sidebar-nav')?.classList.add('open');
  document.querySelector('.sidebar-overlay')?.classList.add('open');
}
function closeSidebar(){
  document.querySelector('.sidebar-nav')?.classList.remove('open');
  document.querySelector('.sidebar-overlay')?.classList.remove('open');
}
function goTo(id){
  closeSidebar();
  document.getElementById(id)?.scrollIntoView({behavior:'smooth',block:'start'});
}

/* ---------- Barra de progresso de leitura ---------- */
function updateProgress(){
  const bar = document.querySelector('.progress-bar');
  if (!bar) return;
  const h   = document.documentElement;
  const max = h.scrollHeight - h.clientHeight;
  bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
}

/* ---------- Helper: roda uma função quando o elemento aparece ----------
   Usado também pelos simuladores inline de cada capítulo:
   onView(el, () => rodarSimulacao())                                  */
function onView(el, fn, opts){
  if (!el) return;
  const obs = new IntersectionObserver((entries, o) => {
    for (const e of entries){
      if (e.isIntersecting){
        o.unobserve(e.target);
        fn(e.target);
      }
    }
  }, Object.assign({threshold:0.25, rootMargin:'0px 0px -40px 0px'}, opts||{}));
  obs.observe(el);
}

/* ---------- Helper: adiciona uma classe ao entrar na tela ---------- */
function revealOnView(selector, cls, opts){
  document.querySelectorAll(selector).forEach(el => {
    onView(el, () => el.classList.add(cls || 'visible'), opts);
  });
}

/* ---------- Scroll reveal das seções ---------- */
function initScrollReveal(){
  revealOnView('.step-section', 'visible', {threshold:0, rootMargin:'0px 0px -60px 0px'});
}

/* ---------- Carimbo "MITO" ---------- */
function initReveals(){
  revealOnView('.mito-real',  'visible', {threshold:0.35});
}

/* ---------- Linha do tempo: itens entram em cascata ----------
   Observa cada ITEM, nunca a linha inteira: uma timeline longa
   (vários milhares de px) jamais alcança um threshold de 0,15 do
   próprio tamanho, e os itens ficariam invisíveis para sempre.
   O escalonamento acontece por proximidade: itens que entram na
   mesma leva ganham um atraso crescente.                        */
function initTimelines(){
  document.querySelectorAll('.timeline').forEach(tl => {
    const itens = [...tl.querySelectorAll('.tl-item')];
    let leva = 0, ultimoDisparo = 0;
    const obs = new IntersectionObserver((entries, o) => {
      for (const e of entries){
        if (!e.isIntersecting) continue;
        o.unobserve(e.target);
        const agora = Date.now();
        leva = (agora - ultimoDisparo < 400) ? leva + 1 : 0;
        ultimoDisparo = agora;
        const alvo = e.target;
        setTimeout(() => alvo.classList.add('on'), Math.min(leva, 6) * 180);
      }
    }, {threshold:0.02, rootMargin:'0px 0px -30px 0px'});
    itens.forEach(li => obs.observe(li));
  });
}

/* ---------- Fluxos autoplay ---------- */
function initAutoplayFlows(){
  revealOnView('.flow-container.autoplay', 'run', {threshold:0.25});
}

/* ---------- Quiz ---------- */
function checkQuiz(btn, isCorrect){
  const quiz = btn.closest('.quiz');
  if (!quiz) return;
  quiz.querySelectorAll('.quiz-opt').forEach(o => {
    o.disabled = true;
    o.classList.remove('correct','wrong');
  });
  btn.classList.add(isCorrect ? 'correct' : 'wrong');
  if (!isCorrect){
    quiz.querySelector('.quiz-opt[data-correct="true"]')?.classList.add('correct');
  }
  const fb = quiz.querySelector('.quiz-feedback');
  if (fb){
    const okText  = fb.dataset.correct || '🎉 Boa! Você acertou.';
    const errText = fb.dataset.wrong   || '😬 Quase! Olha a explicação:';
    const expl    = fb.dataset.explain || '';
    fb.innerHTML = isCorrect
      ? `<strong class="correct">${okText}</strong> ${expl ? '— ' + expl : ''}`
      : `<strong class="wrong">${errText}</strong> ${expl ? '— ' + expl : ''}`;
    fb.classList.add('show');
  }
  if (isCorrect) confettiAt(btn);
}

/* ---------- Confete ---------- */
function confettiAt(el){
  const rect = el.getBoundingClientRect();
  const burst = document.createElement('div');
  burst.className = 'confetti-burst';
  burst.style.left = (rect.left + rect.width/2) + 'px';
  burst.style.top  = (rect.top  + rect.height/2) + 'px';
  const colors = ['#d97757','#4ade80','#f7b731','#a78bfa','#4ecdc4','#ff6b6b'];
  for (let i=0;i<24;i++){
    const p = document.createElement('span');
    p.className = 'piece';
    p.style.background = colors[i % colors.length];
    const angle = (Math.PI*2) * (i/24);
    const dist  = 80 + Math.random()*70;
    p.style.setProperty('--cx', (Math.cos(angle)*dist) + 'px');
    p.style.setProperty('--cy', (Math.sin(angle)*dist + 80) + 'px');
    p.style.animationDelay = (Math.random()*0.1) + 's';
    burst.appendChild(p);
  }
  document.body.appendChild(burst);
  setTimeout(()=>burst.remove(), 1600);
}

/* ---------- Terminal typewriter ---------- */
function initTerminals(){
  document.querySelectorAll('.terminal[data-typewriter]').forEach(t => {
    onView(t, () => playTerminal(t), {threshold:0.3});
  });
}
function playTerminal(term){
  const lines = term.querySelectorAll('.typed');
  let i = 0;
  (function next(){
    if (i >= lines.length) return;
    const span = lines[i];
    const text = span.dataset.text || '';
    let pos = 0;
    span.textContent = '';
    const tick = setInterval(()=>{
      span.textContent = text.slice(0, ++pos);
      if (pos >= text.length){
        clearInterval(tick);
        i++;
        setTimeout(next, 380);
      }
    }, 28 + Math.random()*15);
  })();
}

/* ---------- Sequências automáticas (data-seq) ----------
   <div data-seq="2000">
     <div data-seq-step>...</div>        recebe .active um por vez
     <div data-seq-frame="0">...</div>   recebe .on no quadro N
   </div>
   data-seq-step aceita lista de quadros ("2,5,8") para o
   destaque VOLTAR — essencial em ciclos iterativos.
   data-seq-cumulative: quadros já mostrados FICAM visíveis
   (conversas do .chat-claude vão se acumulando e recomeçam
   quando a sequência volta ao quadro 0).                     */
function initSeqLoops(){
  document.querySelectorAll('[data-seq]').forEach(box => {
    onView(box, () => playSeqLoop(box), {threshold:0.2});
  });
}
function playSeqLoop(box){
  const steps  = [...box.querySelectorAll('[data-seq-step]')];
  const frames = [...box.querySelectorAll('[data-seq-frame]')];
  const declarados = steps
    .map(s => (s.dataset.seqStep || '').split(',').map(n => parseInt(n)).filter(n => !isNaN(n)))
    .flat();
  const count = Math.max(
    steps.length,
    frames.length,
    declarados.length ? Math.max(...declarados) + 1 : 0
  );
  if (!count) return;
  const delay = parseInt(box.dataset.seq) || 1600;
  const cumulative = box.hasAttribute('data-seq-cumulative');
  let i = 0;
  function tick(){
    steps.forEach((s, idx) => {
      const quadros = (s.dataset.seqStep || '').split(',')
        .map(n => parseInt(n)).filter(n => !isNaN(n));
      s.classList.toggle('active', quadros.length ? quadros.includes(i) : idx === i);
    });
    frames.forEach(f => {
      const n = parseInt(f.dataset.seqFrame);
      f.classList.toggle('on', cumulative ? n <= i : n === i);
    });
    i = (i + 1) % count;
  }
  tick();
  setInterval(tick, delay);
}

/* ---------- Copiar prompt (botão 📋 dos .prompt-card) ----------
   Clipboard API primeiro; fallback com textarea+execCommand
   porque em file:// o navegador pode negar o clipboard.      */
function copiarPrompt(btn){
  const pre = btn.closest('.prompt-card')?.querySelector('pre');
  if (!pre) return;
  const texto = pre.innerText;
  const feito = () => {
    const original = btn.textContent;
    btn.textContent = '✅ copiado!';
    btn.classList.add('copiado');
    setTimeout(() => {
      btn.textContent = original;
      btn.classList.remove('copiado');
    }, 2200);
  };
  const fallback = () => {
    const ta = document.createElement('textarea');
    ta.value = texto;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); feito(); } catch(e){ /* sem clipboard: nada a fazer */ }
    ta.remove();
  };
  if (navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(texto).then(feito).catch(fallback);
  } else {
    fallback();
  }
}

/* ---------- Setup ---------- */
document.addEventListener('DOMContentLoaded', () => {
  initScrollReveal();
  initReveals();
  initTimelines();
  initAutoplayFlows();
  initSeqLoops();
  initTerminals();
  updateProgress();

  window.addEventListener('scroll', updateProgress, {passive:true});
  document.querySelector('.sidebar-overlay')?.addEventListener('click', closeSidebar);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSidebar(); });
});

/* expõe o que é usado em onclick inline e nos simuladores dos capítulos */
window.toggleSection = toggleSection;
window.openSidebar   = openSidebar;
window.closeSidebar  = closeSidebar;
window.goTo          = goTo;
window.checkQuiz     = checkQuiz;
window.confettiAt    = confettiAt;
window.onView        = onView;
window.copiarPrompt  = copiarPrompt;
