const STORAGE_KEY = 'formahub-progress';
const USER_ID_KEY = 'formahub-user-id';

function getUserId() {
  let id = localStorage.getItem(USER_ID_KEY);
  if (!id) {
    id = typeof crypto !== 'undefined' && crypto.randomUUID ? crypto.randomUUID() : 'user-' + Date.now();
    localStorage.setItem(USER_ID_KEY, id);
  }
  return id;
}

function getProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  } catch (e) {
    return {};
  }
}

function markModuleComplete(moduleId) {
  const data = getProgress();
  data[moduleId] = { completed: true, date: new Date().toISOString() };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  updateUIProgress();
  queueSync();
}

function updateUIProgress() {
  const data = getProgress();
  const completedKeys = Object.keys(data).filter(k => data[k] && data[k].completed);

  // Update progress bars on dashboard
  document.querySelectorAll('[data-formation-slug]').forEach(el => {
    const slug = el.dataset.formationSlug;
    const total = parseInt(el.dataset.totalModules, 10) || 1;
    const completed = completedKeys.filter(k => k.startsWith(`formation-${slug}`)).length;
    const pct = Math.round((completed / total) * 100);

    const fill = el.querySelector('.progress-bar-fill');
    if (fill) fill.style.width = pct + '%';

    const label = el.querySelector('.progress-text');
    if (label) label.textContent = `${completed}/${total} terminés (${pct}%)`;

    const badge = el.querySelector('.status-badge');
    if (badge) {
      if (completed === total) {
        badge.className = 'badge badge-success status-badge';
        badge.textContent = 'Terminé';
      } else if (completed > 0) {
        badge.className = 'badge badge-progress status-badge';
        badge.textContent = `${completed}/${total} modules`;
      } else {
        badge.className = 'badge badge-neutral status-badge';
        badge.textContent = 'Non commencé';
      }
    }
  });

  // Update complete button if on module page
  const completeBtn = document.getElementById('btn-mark-complete');
  if (completeBtn && completeBtn.dataset.moduleId) {
    const modId = completeBtn.dataset.moduleId;
    if (data[modId] && data[modId].completed) {
      completeBtn.className = 'btn btn-success';
      completeBtn.innerHTML = '✓ Module validé';
    }
  }
}

function initThemeToggle() {
  const saved = localStorage.getItem('theme-preference') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.innerHTML = saved === 'dark' ? '☀️ Mode Clair' : '🌙 Mode Sombre';
    btn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme-preference', next);
      btn.innerHTML = next === 'dark' ? '☀️ Mode Clair' : '🌙 Mode Sombre';
    });
  });
}

let syncTimeout = null;
function queueSync() {
  clearTimeout(syncTimeout);
  syncTimeout = setTimeout(syncProgressToCloud, 2000);
}

async function syncProgressToCloud() {
  if (!navigator.onLine) return;
  try {
    const userId = getUserId();
    await fetch(`/api/progress/${userId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: localStorage.getItem(STORAGE_KEY) || '{}'
    });
    localStorage.setItem('last-sync', new Date().toISOString());
  } catch (e) {
    console.warn('Sync cloud différée (hors ligne ou sans Worker).');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  updateUIProgress();

  const completeBtn = document.getElementById('btn-mark-complete');
  if (completeBtn && completeBtn.dataset.moduleId) {
    completeBtn.addEventListener('click', () => {
      markModuleComplete(completeBtn.dataset.moduleId);
    });
  }
});
window.addEventListener('online', syncProgressToCloud);