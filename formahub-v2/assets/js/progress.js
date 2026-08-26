const STORAGE_KEY = 'formahub-progress';
const USER_ID_KEY = 'formahub-user-id';

function getUserId() {
  let id = localStorage.getItem(USER_ID_KEY);
  if (!id) {
    id = (typeof crypto !== 'undefined' && crypto.randomUUID) ? crypto.randomUUID() : 'user-' + Date.now();
    localStorage.setItem(USER_ID_KEY, id);
  }
  return id;
}

function getProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  } catch(e) {
    return {};
  }
}

function markModuleComplete(moduleId, score = null) {
  const data = getProgress();
  data[moduleId] = { 
    completed: true, 
    score: score,
    date: new Date().toISOString() 
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  updateUIProgress();
  queueSync();
}

function updateUIProgress() {
  const data = getProgress();
  const completedCount = Object.keys(data).filter(k => data[k] && data[k].completed).length;
  const totalModules = 25;
  const pct = Math.round((completedCount / totalModules) * 100);

  const fillEl = document.getElementById('global-progress-fill');
  const textEl = document.getElementById('global-progress-text');
  if (fillEl) fillEl.style.width = pct + '%';
  if (textEl) textEl.textContent = `${completedCount}/${totalModules} modules (${pct}%)`;

  // Update specific module badges if on page
  document.querySelectorAll('[data-module-badge]').forEach(badge => {
    const mId = badge.dataset.moduleBadge;
    if (data[mId] && data[mId].completed) {
      badge.className = 'badge badge-success';
      badge.textContent = data[mId].score !== null ? `✓ Validé (${data[mId].score}%)` : '✓ Terminé';
    }
  });
}

function initThemeToggle() {
  const saved = localStorage.getItem('theme-preference') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  document.querySelectorAll('.theme-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme-preference', next);
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
      body: localStorage.getItem(STORAGE_KEY)
    });
    localStorage.setItem('last-sync', new Date().toISOString());
  } catch (e) {
    console.warn('Sync KV différé ou mode hors-ligne');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  updateUIProgress();
});
window.addEventListener('online', syncProgressToCloud);
