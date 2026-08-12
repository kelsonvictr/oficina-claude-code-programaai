/* =========================================================
   Oficina Claude Code — para quem nunca programou
   shared/motion-fx.js — camada de animações com Motion (motion.dev)
   Carregado como <script type="module">. Se a CDN falhar, o site
   continua funcionando (as animações de CSS já cobrem o básico).

   Uso no HTML:
   - [data-motion="rise"]   -> sobe + fade quando entra na tela
   - [data-motion="pop"]    -> "pula" ao entrar
   - [data-motion="float"]  -> flutua em loop (suave)
   - .flow-packet           -> item que viaja ao longo de um offset-path
   ========================================================= */
const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;

(async () => {
  if (reduce) return;
  let M;
  try {
    M = await import('https://cdn.jsdelivr.net/npm/motion@11/+esm');
  } catch (e) {
    console.warn('[motion-fx] Motion não carregou; usando fallback CSS.', e);
    return;
  }
  const { animate, inView, stagger } = M;

  /* versões novas do motion passam um IntersectionObserverEntry pro callback
     do inView (não o elemento) — normaliza pra funcionar nas duas */
  const asEl = (x) => (x instanceof Element ? x : x?.target);

  /* entrada: sobe + fade, com stagger nos filhos marcados */
  inView('[data-motion="rise"]', (raw) => {
    const el = asEl(raw); if (!el) return;
    const kids = el.querySelectorAll('[data-motion-child]');
    if (kids.length) {
      animate(kids, { opacity: [0, 1], transform: ['translateY(24px)', 'translateY(0px)'] },
        { duration: 0.6, delay: stagger(0.08), easing: [0.22, 1, 0.36, 1] });
    } else {
      animate(el, { opacity: [0, 1], transform: ['translateY(24px)', 'translateY(0px)'] },
        { duration: 0.6, easing: [0.22, 1, 0.36, 1] });
    }
    return () => {};
  }, { margin: '0px 0px -10% 0px' });

  /* pop ao entrar */
  inView('[data-motion="pop"]', (raw) => {
    const el = asEl(raw); if (!el) return;
    animate(el, { transform: ['scale(0.7)', 'scale(1)'], opacity: [0, 1] },
      { duration: 0.5, easing: [0.34, 1.56, 0.64, 1] });
    return () => {};
  });

  /* flutuar em loop */
  document.querySelectorAll('[data-motion="float"]').forEach((el, i) => {
    animate(el, { transform: ['translateY(0px)', 'translateY(-10px)', 'translateY(0px)'] },
      { duration: 3 + (i % 3) * 0.4, repeat: Infinity, easing: 'ease-in-out' });
  });

  /* itens viajando ao longo de uma linha (offset-path) */
  document.querySelectorAll('.flow-packet').forEach((el, i) => {
    animate(el, { offsetDistance: ['0%', '100%'], opacity: [0, 1, 1, 0] },
      { duration: 2.2, repeat: Infinity, delay: i * 0.6, easing: 'linear' });
  });
})();
