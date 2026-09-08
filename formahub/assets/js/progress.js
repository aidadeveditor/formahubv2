/* ============================================================
   Formahub — progression, thème et interactions (V7)
   Vanilla JS, sans dépendance. Chargé sur toutes les pages ;
   chaque bloc s'auto-désactive si la page ne le concerne pas.
   ============================================================ */

const STORAGE_KEY = 'formahub-progress';
const LAST_SEEN_KEY = 'formahub-last-module';
const CHECKLIST_KEY = 'formahub-checklists';
const INSCRIPTIONS_KEY = 'formahub-inscriptions';

/* ---------- Utilitaires de stockage ---------- */

function safeGet(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch (e) {
    return fallback;
  }
}

function safeSet(key, value) {
  try {
    localStorage.setItem(key, typeof value === 'string' ? value : JSON.stringify(value));
  } catch (e) {
    /* stockage indisponible (navigation privée) : on continue sans persistance */
  }
}

function getProgress() {
  return safeGet(STORAGE_KEY, {}) || {};
}

function completedModuleIds() {
  const data = getProgress();
  return Object.keys(data).filter(k => data[k] && data[k].completed);
}

/* ---------- Marquer un module terminé ---------- */

function markModuleComplete(moduleId) {
  const data = getProgress();
  const already = !!(data[moduleId] && data[moduleId].completed);
  if (already) {
    delete data[moduleId];
  } else {
    data[moduleId] = { completed: true, date: new Date().toISOString() };
  }
  safeSet(STORAGE_KEY, data);
  updateUIProgress();
  queueSync();
  showToast(already ? '↩️ Module remis « à faire ».' : '🎉 Module validé, bravo !');
}

/* ---------- Mise à jour de l'affichage ---------- */

function updateUIProgress() {
  const completedKeys = completedModuleIds();
  let doneTotal = 0;
  let moduleTotal = 0;
  let formationsDone = 0;
  let formationsStarted = 0;

  document.querySelectorAll('[data-formation-slug]').forEach(el => {
    const slug = el.dataset.formationSlug;
    const total = parseInt(el.dataset.totalModules, 10) || 1;
    const completed = completedKeys.filter(k => k.startsWith(`formation-${slug}-module-`)).length;
    const pct = Math.round((completed / total) * 100);

    doneTotal += completed;
    moduleTotal += total;
    if (completed === total) formationsDone += 1;
    else if (completed > 0) formationsStarted += 1;

    const fill = el.querySelector('.progress-bar-fill');
    if (fill) {
      fill.style.width = pct + '%';
      fill.setAttribute('aria-valuenow', String(pct));
    }

    const label = el.querySelector('.progress-text');
    if (label) label.textContent = `${completed}/${total} terminés (${pct}%)`;

    const badge = el.querySelector('.status-badge');
    if (badge) {
      if (completed === total) {
        badge.className = 'badge badge-success status-badge';
        badge.textContent = '✓ Terminé';
      } else if (completed > 0) {
        badge.className = 'badge badge-progress status-badge';
        badge.textContent = `En cours · ${completed}/${total}`;
      } else {
        badge.className = 'badge badge-neutral status-badge';
        badge.textContent = 'Non commencé';
      }
    }

    // État de la carte, utilisé par les filtres
    el.dataset.state = completed === total ? 'done' : (completed > 0 ? 'progress' : 'todo');
    el.classList.toggle('is-done', completed === total);

    // Bouton d'accès : « reprendre » au premier module non terminé
    const cta = el.querySelector('[data-cta]');
    if (cta) {
      let next = 1;
      for (let i = 1; i <= total; i++) {
        if (!completedKeys.includes(`formation-${slug}-module-${i}`)) { next = i; break; }
        next = Math.min(i + 1, total);
      }
      cta.href = `formations/${slug}/module-${next}/index.html`;
      if (completed === total) cta.textContent = 'Revoir la formation ↻';
      else if (completed > 0) cta.textContent = `Reprendre au module ${next} →`;
      else cta.textContent = 'Commencer la formation →';
    }
  });

  updateDashboard(doneTotal, moduleTotal, formationsDone, formationsStarted);
  updateResumeBar();

  // Bouton « terminé » sur une page module
  const completeBtn = document.getElementById('btn-mark-complete');
  if (completeBtn && completeBtn.dataset.moduleId) {
    const data = getProgress();
    const done = !!(data[completeBtn.dataset.moduleId] && data[completeBtn.dataset.moduleId].completed);
    completeBtn.className = done ? 'btn btn-success' : 'btn btn-primary';
    completeBtn.textContent = done ? '✓ Module validé — annuler' : 'Marquer le module comme terminé ✓';
  }
}

/* ---------- Tableau de bord de l'accueil ---------- */

function updateDashboard(done, total, formationsDone, formationsStarted) {
  const ring = document.getElementById('global-ring');
  if (!ring || !total) return;

  const pct = Math.round((done / total) * 100);
  ring.style.setProperty('--pct', String(pct));
  ring.setAttribute('aria-valuenow', String(pct));
  const ringLabel = ring.querySelector('span');
  if (ringLabel) ringLabel.textContent = pct + '%';

  const set = (id, value) => {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  };
  set('stat-done', `${done}/${total}`);
  set('stat-formations', `${formationsDone}/${document.querySelectorAll('[data-formation-slug]').length}`);
  set('stat-progress', String(formationsStarted));

  // Temps restant estimé, à partir des durées déclarées sur les cartes
  let minutesLeft = 0;
  document.querySelectorAll('[data-formation-slug]').forEach(el => {
    const mins = parseInt(el.dataset.minutes, 10);
    const totalMods = parseInt(el.dataset.totalModules, 10) || 1;
    if (!mins) return;
    const completedKeys = completedModuleIds();
    const slug = el.dataset.formationSlug;
    const completed = completedKeys.filter(k => k.startsWith(`formation-${slug}-module-`)).length;
    minutesLeft += Math.round(mins * (1 - completed / totalMods));
  });
  const h = Math.floor(minutesLeft / 60);
  const m = minutesLeft % 60;
  set('stat-time', h > 0 ? `${h} h ${String(m).padStart(2, '0')}` : `${m} min`);
}

/* ---------- Bandeau « reprendre où j'en étais » ---------- */

function updateResumeBar() {
  const bar = document.getElementById('resume-bar');
  if (!bar) return;
  const last = safeGet(LAST_SEEN_KEY, null);
  if (!last || !last.href || !last.title) {
    bar.hidden = true;
    return;
  }
  bar.hidden = false;
  const title = bar.querySelector('.resume-title');
  const link = bar.querySelector('.resume-link');
  if (title) title.textContent = last.title;
  if (link) link.href = last.href;
}

function rememberCurrentModule() {
  const btn = document.getElementById('btn-mark-complete');
  if (!btn || !btn.dataset.moduleId) return;
  const h1 = document.querySelector('.module-header h1');
  const formation = document.querySelector('.module-header .breadcrumb span');
  const parts = btn.dataset.moduleId.replace(/^formation-/, '').split('-module-');
  if (parts.length !== 2) return;
  safeSet(LAST_SEEN_KEY, {
    href: `formations/${parts[0]}/module-${parts[1]}/index.html`,
    title: (formation ? formation.textContent.trim() + ' — ' : '') + (h1 ? h1.textContent.trim() : 'Module'),
    date: new Date().toISOString()
  });
}

/* ---------- Thème clair / sombre ---------- */

function initThemeToggle() {
  let saved = null;
  try { saved = localStorage.getItem('theme-preference'); } catch (e) { /* ignore */ }
  if (!saved) {
    saved = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  applyTheme(saved);

  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.setAttribute('aria-label', 'Basculer entre le mode clair et le mode sombre');
    btn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      applyTheme(current === 'dark' ? 'light' : 'dark');
      safeSet('theme-preference', document.documentElement.getAttribute('data-theme'));
    });
  });
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.textContent = theme === 'dark' ? '☀️ Mode clair' : '🌙 Mode sombre';
  });
}

/* Application immédiate pour éviter le flash blanc au chargement */
(function preTheme() {
  try {
    const saved = localStorage.getItem('theme-preference');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
    else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.documentElement.setAttribute('data-theme', 'dark');
    }
  } catch (e) { /* ignore */ }
})();

/* ---------- Recherche et filtres du catalogue ---------- */

function initCatalogue() {
  const grid = document.querySelector('.catalogue-grid');
  if (!grid) return;
  const search = document.getElementById('catalogue-search');
  const filters = document.querySelectorAll('[data-state-filter]');
  const empty = document.getElementById('catalogue-empty');
  let activeState = 'all';

  function apply() {
    const q = (search && search.value || '').trim().toLowerCase();
    let visible = 0;
    grid.querySelectorAll('.card').forEach(card => {
      const text = card.textContent.toLowerCase();
      const matchText = !q || text.includes(q);
      const matchState = activeState === 'all' || card.dataset.state === activeState;
      const show = matchText && matchState;
      card.classList.toggle('is-hidden', !show);
      if (show) visible++;
    });
    if (empty) empty.hidden = visible > 0;
  }

  if (search) {
    search.addEventListener('input', apply);
    document.addEventListener('keydown', e => {
      if (e.key === '/' && document.activeElement !== search &&
          !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)) {
        e.preventDefault();
        search.focus();
        search.select();
      }
      if (e.key === 'Escape' && document.activeElement === search) {
        search.value = '';
        apply();
        search.blur();
      }
    });
  }

  filters.forEach(btn => {
    btn.addEventListener('click', () => {
      filters.forEach(b => {
        b.classList.toggle('active', b === btn);
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
      });
      activeState = btn.dataset.stateFilter;
      apply();
    });
  });

  window.formahubApplyFilters = apply;
  apply();
}

/* ---------- Mise en page de lecture des modules ---------- */

const SECTIONS_KEY = 'formahub-sections';

/* Blocs qui deviennent leur propre volet repliable */
const STANDALONE = '.case-box, .checklist-box, .glossary-box, .takeaway-box, .resources-box';

function initModuleLayout() {
  const content = document.querySelector('.module-content');
  if (!content) return;
  if (content.querySelectorAll('h2').length < 2) return;

  // Colonne de lecture : contenu + quiz + navigation à gauche, sommaire à droite
  const parent = content.parentNode;
  const body = document.createElement('div');
  body.className = 'module-body';
  const main = document.createElement('div');
  main.className = 'module-main';
  const aside = document.createElement('aside');
  aside.className = 'module-toc';

  parent.insertBefore(body, content);
  body.appendChild(aside);
  body.appendChild(main);
  ['.module-content', '.quiz-section', '.module-nav'].forEach(sel => {
    const node = parent.querySelector(':scope > ' + sel);
    if (node) main.appendChild(node);
  });

  foldQuiz();

  const folds = buildFolds(content);
  const refreshCount = buildFoldToolbar(content, folds);
  const syncToc = buildToc(aside, folds);
  addSectionStepper(folds);
  restoreReadState(folds);
  refreshCount();
  syncToc();
  openFromHash(folds);
}

/* ---------- Le quiz aussi est replié par défaut ---------- */

function foldQuiz() {
  const section = document.querySelector('.quiz-section');
  if (!section) return;
  const heading = section.querySelector(':scope > h2');
  const container = section.querySelector('#quiz-container');
  if (!heading || !container) return;

  const fold = document.createElement('details');
  fold.className = 'section-fold quiz-fold';
  fold.id = 'quiz';
  fold.innerHTML =
    '<summary><span class="fold-mark" aria-hidden="true"></span>' +
    '<span class="fold-title"></span>' +
    '<span class="fold-meta">auto-évaluation</span></summary>' +
    '<div class="fold-body"></div>';
  fold.querySelector('.fold-title').textContent = heading.textContent.trim();

  section.insertBefore(fold, heading);
  const foldBody = fold.querySelector('.fold-body');

  // Tout ce qui précède le bouton « terminé » entre dans le volet
  let node = fold.nextSibling;
  while (node) {
    const next = node.nextSibling;
    if (node.nodeType === 1 && node.querySelector && node.querySelector('#btn-mark-complete')) break;
    foldBody.appendChild(node);
    node = next;
  }
  heading.remove();

  fold.addEventListener('toggle', () => { if (fold.open) fold.classList.add('is-read'); });
}

/* ---------- Découpage du module en volets repliables ---------- */

function estimateMinutes(node) {
  const words = (node.textContent || '').trim().split(/\s+/).length;
  return Math.max(1, Math.round(words / 200));
}

function makeFold(title, index) {
  const d = document.createElement('details');
  d.className = 'section-fold';
  d.id = 'section-' + index;
  d.innerHTML =
    '<summary><span class="fold-mark" aria-hidden="true"></span>' +
    '<span class="fold-title"></span>' +
    '<span class="fold-meta"></span></summary>' +
    '<div class="fold-body"></div>';
  d.querySelector('.fold-title').textContent = title;
  return d;
}

function buildFolds(content) {
  const children = Array.from(content.children);
  const chunks = [];
  let current = null;

  children.forEach(node => {
    if (node.tagName === 'H2') {
      current = { type: 'section', title: node.textContent.trim(), heading: node, nodes: [] };
      chunks.push(current);
      return;
    }
    if (node.matches && node.matches(STANDALONE)) {
      const h3 = node.querySelector(':scope > h3');
      chunks.push({ type: 'box', title: h3 ? h3.textContent.trim() : 'Section', box: node, heading: h3 });
      current = null;
      return;
    }
    if (current) current.nodes.push(node);
    // sinon (intro, objectifs) : reste visible en haut de page
  });

  const folds = [];
  chunks.forEach((chunk, i) => {
    const index = i + 1;
    let fold;

    if (chunk.type === 'section') {
      fold = makeFold(chunk.title, index);
      content.insertBefore(fold, chunk.heading);
      const foldBody = fold.querySelector('.fold-body');
      chunk.nodes.forEach(n => foldBody.appendChild(n));
      chunk.heading.remove();
    } else {
      // Le bloc garde son habillage pastel et devient lui-même repliable
      fold = document.createElement('details');
      fold.className = chunk.box.className + ' section-fold is-box';
      fold.id = 'section-' + index;
      const summary = document.createElement('summary');
      summary.innerHTML = '<span class="fold-mark" aria-hidden="true"></span>' +
        '<span class="fold-title"></span><span class="fold-meta"></span>';
      summary.querySelector('.fold-title').textContent = chunk.title;
      const foldBody = document.createElement('div');
      foldBody.className = 'fold-body';
      if (chunk.heading) chunk.heading.remove();
      while (chunk.box.firstChild) foldBody.appendChild(chunk.box.firstChild);
      fold.appendChild(summary);
      fold.appendChild(foldBody);
      chunk.box.replaceWith(fold);
    }

    fold.querySelector('.fold-meta').textContent = '~' + estimateMinutes(fold) + ' min';
    folds.push(fold);
  });

  return folds;
}

/* ---------- Barre de contrôle des volets ---------- */

function buildFoldToolbar(content, folds) {
  const bar = document.createElement('div');
  bar.className = 'fold-toolbar';
  bar.innerHTML =
    '<span class="fold-count"></span>' +
    '<button type="button" class="btn btn-ghost btn-sm" data-fold-action="expand">Tout déplier</button>' +
    '<button type="button" class="btn btn-ghost btn-sm" data-fold-action="collapse">Tout replier</button>';
  content.insertBefore(bar, folds[0]);

  const count = bar.querySelector('.fold-count');
  function refresh() {
    const read = folds.filter(f => f.classList.contains('is-read')).length;
    count.textContent = `${folds.length} sections · ${read} lue${read > 1 ? 's' : ''}`;
  }

  bar.addEventListener('click', e => {
    const action = e.target.dataset && e.target.dataset.foldAction;
    if (!action) return;
    folds.forEach(f => { f.open = action === 'expand'; });
    if (action === 'expand') folds.forEach(markRead);
    refresh();
  });

  folds.forEach(fold => {
    fold.addEventListener('toggle', () => {
      if (fold.open) { markRead(fold); refresh(); }
    });
  });

  refresh();
  return refresh;
}

function markRead(fold) {
  if (fold.classList.contains('is-read')) return;
  fold.classList.add('is-read');
  const store = safeGet(SECTIONS_KEY, {}) || {};
  const page = store[location.pathname] || {};
  page[fold.id] = true;
  store[location.pathname] = page;
  safeSet(SECTIONS_KEY, store);
}

function restoreReadState(folds) {
  const store = safeGet(SECTIONS_KEY, {}) || {};
  const page = store[location.pathname] || {};
  folds.forEach(f => { if (page[f.id]) f.classList.add('is-read'); });
  // Tout est replié au chargement : la page se lit d'abord comme le plan du module
}

/* Enchaînement d'une section à la suivante */
function addSectionStepper(folds) {
  folds.forEach((fold, i) => {
    const next = folds[i + 1];
    const quiz = document.getElementById('quiz');
    const target = next || quiz;
    if (!target) return;

    const nav = document.createElement('div');
    nav.className = 'fold-next';
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn-outline btn-sm';
    btn.textContent = next
      ? 'Section suivante : ' + shorten(next.querySelector('.fold-title').textContent)
      : 'Passer au quiz →';
    btn.addEventListener('click', () => {
      fold.open = false;
      target.open = true;
      markRead(target);
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    nav.appendChild(btn);
    fold.querySelector('.fold-body').appendChild(nav);
  });
}

function shorten(text) {
  const clean = text.replace(/^\d+\.\s*/, '').trim();
  return (clean.length > 42 ? clean.slice(0, 40).trimEnd() + '…' : clean) + ' →';
}

function openFromHash(folds) {
  const id = location.hash.replace('#', '');
  if (!id) return;
  const target = folds.find(f => f.id === id);
  if (!target) return;
  target.open = true;
  requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
}

/* ---------- Sommaire latéral ---------- */

function buildToc(aside, folds) {
  const details = document.createElement('details');
  details.className = 'toc';
  details.open = window.innerWidth > 1060;
  details.innerHTML = '<summary>🧭 Sommaire du module</summary><ol class="toc-list"></ol>';
  const list = details.querySelector('.toc-list');

  folds.forEach(fold => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#' + fold.id;
    a.textContent = fold.querySelector('.fold-title').textContent;
    a.dataset.target = fold.id;
    a.addEventListener('click', e => {
      e.preventDefault();
      fold.open = true;
      markRead(fold);
      fold.scrollIntoView({ behavior: 'smooth', block: 'start' });
      history.replaceState(null, '', '#' + fold.id);
    });
    li.appendChild(a);
    list.appendChild(li);
  });

  aside.appendChild(details);

  if ('IntersectionObserver' in window) {
    const links = Array.from(list.querySelectorAll('a'));
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        links.forEach(l => l.classList.toggle('is-current', l.dataset.target === entry.target.id));
      });
    }, { rootMargin: '-12% 0px -75% 0px', threshold: 0 });
    folds.forEach(f => observer.observe(f));
  }

  // Reflète l'état « lu » dans le sommaire
  function sync() {
    folds.forEach(fold => {
      const link = list.querySelector('[data-target="' + fold.id + '"]');
      if (link) link.classList.toggle('is-read', fold.classList.contains('is-read'));
    });
  }
  folds.forEach(fold => fold.addEventListener('toggle', sync));
  return sync;
}

/* ---------- Barre de progression de lecture ---------- */

function initReadProgress() {
  if (!document.querySelector('.module-content')) return;
  const bar = document.createElement('div');
  bar.className = 'read-progress';
  bar.innerHTML = '<span></span>';
  document.body.appendChild(bar);
  const fill = bar.firstElementChild;

  let ticking = false;
  function update() {
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    const pct = max > 0 ? Math.min(100, (h.scrollTop / max) * 100) : 0;
    fill.style.width = pct + '%';
    ticking = false;
  }
  window.addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  update();
}

/* ---------- Checklists cochables et mémorisées ---------- */

function initChecklists() {
  const lists = document.querySelectorAll('ul.checklist');
  if (!lists.length) return;
  const pageKey = location.pathname;
  const store = safeGet(CHECKLIST_KEY, {}) || {};
  const state = store[pageKey] || {};

  lists.forEach((list, li) => {
    list.querySelectorAll('li').forEach((item, ii) => {
      const key = li + ':' + ii;
      item.setAttribute('role', 'checkbox');
      item.tabIndex = 0;
      const setChecked = (checked) => {
        item.classList.toggle('is-checked', checked);
        item.setAttribute('aria-checked', checked ? 'true' : 'false');
      };
      setChecked(!!state[key]);
      const toggle = () => {
        const next = !item.classList.contains('is-checked');
        setChecked(next);
        state[key] = next;
        store[pageKey] = state;
        safeSet(CHECKLIST_KEY, store);
      };
      item.addEventListener('click', toggle);
      item.addEventListener('keydown', e => {
        if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); toggle(); }
      });
    });
  });
}

/* ---------- Suivi des inscriptions aux formations externes ---------- */
/* Alimente la colonne « Inscription » de ressources-externes.html et de
   formations-espagne.html. Chaque ligne porte un identifiant stable
   (data-ins-id) et trois états : à faire, inscrite, terminée — avec la
   date d'inscription. Stocké dans le navigateur, comme les checklists. */

const INS_STATES = ['todo', 'inscrite', 'terminee'];

function getInscriptions() {
  const data = safeGet(INSCRIPTIONS_KEY, {}) || {};
  return (typeof data === 'object' && !Array.isArray(data)) ? data : {};
}

function todayISO() {
  const d = new Date();
  return new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 10);
}

function formatDateFR(iso) {
  if (!iso) return '';
  const p = iso.split('-');
  return p.length === 3 ? p[2] + '/' + p[1] + '/' + p[0] : iso;
}

function initInscriptions() {
  const cells = Array.prototype.slice.call(document.querySelectorAll('td.ins-cell'));
  if (!cells.length) return;
  const store = getInscriptions();
  const summary = document.getElementById('ins-summary');

  function refreshSummary() {
    if (!summary) return;
    let ins = 0, fin = 0;
    cells.forEach(cell => {
      const st = (store[cell.dataset.insId] || {}).statut;
      if (st === 'inscrite') ins++;
      else if (st === 'terminee') fin++;
    });
    summary.textContent = ins + (ins > 1 ? ' inscriptions en cours' : ' inscription en cours')
      + ' · ' + fin + (fin > 1 ? ' terminées' : ' terminée');
  }

  cells.forEach(cell => {
    const id = cell.dataset.insId;
    const row = cell.closest('tr');
    const select = cell.querySelector('.ins-status');
    const dateInput = cell.querySelector('.ins-date');
    const dateLabel = cell.querySelector('.ins-date-label');
    if (!id || !select || !dateInput) return;

    const entry = store[id] || {};
    select.value = INS_STATES.indexOf(entry.statut) > 0 ? entry.statut : 'todo';
    if (entry.date) dateInput.value = entry.date;

    function paint() {
      const current = select.value;
      const active = current !== 'todo';
      dateInput.hidden = !active;
      if (dateLabel) dateLabel.hidden = !active;
      cell.classList.toggle('is-inscrite', current === 'inscrite');
      cell.classList.toggle('is-terminee', current === 'terminee');
      if (row) {
        row.dataset.ins = current;
        row.classList.toggle('row-inscrite', active);
      }
    }

    function save() {
      if (select.value === 'todo') delete store[id];
      else store[id] = { statut: select.value, date: dateInput.value || '' };
      safeSet(INSCRIPTIONS_KEY, store);
      refreshSummary();
      if (typeof window.formahubApplyFilters === 'function') window.formahubApplyFilters();
    }

    select.addEventListener('change', () => {
      if (select.value !== 'todo' && !dateInput.value) dateInput.value = todayISO();
      paint();
      save();
      if (select.value === 'inscrite') {
        showToast('📝 Inscription notée au ' + formatDateFR(dateInput.value) + '.');
      } else if (select.value === 'terminee') {
        showToast('🎓 Formation marquée terminée.');
      } else {
        showToast('↩️ Ligne remise à « pas encore inscrite ».');
      }
    });

    dateInput.addEventListener('change', save);
    paint();
  });

  refreshSummary();
}

/* ---------- Retour en haut, en-tête collant, toasts ---------- */

function initToTop() {
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'to-top';
  btn.setAttribute('aria-label', 'Revenir en haut de la page');
  btn.textContent = '↑';
  document.body.appendChild(btn);
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  const header = document.querySelector('.site-header');
  let ticking = false;
  function onScroll() {
    const y = window.scrollY;
    btn.classList.toggle('is-visible', y > 420);
    if (header) header.classList.toggle('is-stuck', y > 8);
    ticking = false;
  }
  window.addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();
}

let toastTimer = null;
function showToast(message) {
  let toast = document.querySelector('.toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  requestAnimationFrame(() => toast.classList.add('is-visible'));
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('is-visible'), 3200);
}

/* ---------- Synchronisation cloud ---------- */
/* Depuis la V7, elle est entièrement portée par sync.js : la progression
   part sous un identifiant dérivé du code secret et chiffrée avec lui.
   Ici on se contente de signaler qu'il y a du nouveau à sauvegarder. */

function queueSync() {
  if (typeof window.formahubQueueBackup === 'function') window.formahubQueueBackup();
}

/* ---------- Amorçage ---------- */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initCatalogue();
  rememberCurrentModule();
  updateUIProgress();
  initModuleLayout();
  initReadProgress();
  initChecklists();
  initInscriptions();
  initToTop();

  const completeBtn = document.getElementById('btn-mark-complete');
  if (completeBtn && completeBtn.dataset.moduleId) {
    completeBtn.addEventListener('click', () => markModuleComplete(completeBtn.dataset.moduleId));
  }

  // Les filtres dépendent des états calculés par updateUIProgress
  if (typeof window.formahubApplyFilters === 'function') window.formahubApplyFilters();
});

/* ---------- Points d'entrée partagés avec audio.js, offline.js et sync.js ---------- */

window.formahubToast = showToast;
window.updateUIProgress = updateUIProgress;
window.markRead = markRead;

