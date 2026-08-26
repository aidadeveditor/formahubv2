// Formahub V2 - Quiz Engine dynamique
async function loadQuiz(quizPath, containerId, moduleId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  container.innerHTML = '<p class="text-muted">Chargement du questionnaire d\'auto-évaluation...</p>';

  try {
    const res = await fetch(quizPath);
    if (!res.ok) throw new Error('Impossible de charger le questionnaire');
    const quiz = await res.json();

    renderQuiz(quiz, container, moduleId);
  } catch (err) {
    container.innerHTML = `<div class="card" style="border-color: var(--danger); padding: 16px;">
      <p style="color: var(--danger); margin: 0;">Erreur de chargement du quiz (${err.message}). Vérifiez le chemin : <code>${quizPath}</code></p>
    </div>`;
  }
}

function renderQuiz(quiz, container, moduleId) {
  const answers = {};

  const html = `
    <div class="quiz-header">
      <div>
        <h3 style="margin: 0;">Auto-évaluation formative</h3>
        <small style="color: var(--text-muted);">Version ${quiz.version} • Revalidé le ${quiz.last_verified} • ${quiz.questions.length} questions</small>
      </div>
      <span class="badge badge-neutral" id="quiz-status-badge">0/${quiz.questions.length} répondues</span>
    </div>

    <form id="quiz-form-${quiz.module_id}">
      ${quiz.questions.map((q, idx) => `
        <fieldset class="quiz-question" data-qid="${q.id}" id="q-block-${q.id}">
          <legend>Question ${idx + 1} sur ${quiz.questions.length}</legend>
          <p style="font-weight: 600; margin: 8px 0 14px 0;">${q.question}</p>
          <div class="quiz-choices">
            ${q.choices.map(c => `
              <label class="quiz-choice" data-key="${c.key}">
                <input type="radio" name="${q.id}" value="${c.key}">
                <span><strong>${c.key.toUpperCase()}.</strong> ${c.text}</span>
              </label>
            `).join('')}
          </div>
          <div class="quiz-feedback" id="feedback-${q.id}" hidden></div>
        </fieldset>
      `).join('')}

      <div id="quiz-result-summary" hidden class="quiz-summary-card">
        <div>
          <h4 style="margin: 0 0 4px 0;" id="quiz-score-title">Score final : -</h4>
          <p style="margin: 0; color: var(--text-muted); font-size: 0.9rem;" id="quiz-score-desc"></p>
        </div>
        <button type="button" class="btn btn-primary" id="btn-validate-completion">Enregistrer ma progression</button>
      </div>
    </form>
  `;

  container.innerHTML = html;

  const form = document.getElementById(`quiz-form-${quiz.module_id}`);
  const statusBadge = document.getElementById('quiz-status-badge');
  const summaryEl = document.getElementById('quiz-result-summary');
  const scoreTitle = document.getElementById('quiz-score-title');
  const scoreDesc = document.getElementById('quiz-score-desc');
  const btnSave = document.getElementById('btn-validate-completion');

  quiz.questions.forEach(q => {
    const inputs = form.querySelectorAll(`input[name="${q.id}"]`);
    inputs.forEach(input => {
      input.addEventListener('change', () => {
        answers[q.id] = input.value;
        const fieldset = document.getElementById(`q-block-${q.id}`);
        const feedbackEl = document.getElementById(`feedback-${q.id}`);

        // Highlight active choice
        fieldset.querySelectorAll('.quiz-choice').forEach(lbl => {
          lbl.classList.toggle('is-selected', lbl.dataset.key === input.value);
        });

        const isCorrect = input.value === q.correct_answer;
        fieldset.classList.remove('correct', 'incorrect');
        fieldset.classList.add(isCorrect ? 'correct' : 'incorrect');

        feedbackEl.innerHTML = `<strong>${isCorrect ? '✓ Bonne réponse !' : '✗ Réponse incorrecte.'}</strong><br>${q.feedback}`;
        feedbackEl.hidden = false;

        // Update answered count
        const answeredCount = Object.keys(answers).length;
        statusBadge.textContent = `${answeredCount}/${quiz.questions.length} répondues`;
        if (answeredCount === quiz.questions.length) {
          statusBadge.className = 'badge badge-success';

          // Calculate score
          let correctCount = 0;
          quiz.questions.forEach(item => {
            if (answers[item.id] === item.correct_answer) correctCount++;
          });

          const scorePct = Math.round((correctCount / quiz.questions.length) * 100);
          summaryEl.hidden = false;
          scoreTitle.textContent = `Score obtenu : ${correctCount}/${quiz.questions.length} (${scorePct}%)`;

          if (scorePct >= 75) {
            scoreDesc.textContent = "Excellent travail ! Vous maîtrisez les concepts clés de ce module.";
            btnSave.className = "btn btn-primary";
            btnSave.textContent = "Valider et terminer le module";
          } else {
            scoreDesc.textContent = "Prenez le temps de relire les explications ci-dessus pour consolider vos acquis.";
            btnSave.className = "btn btn-secondary";
            btnSave.textContent = "Enregistrer la tentative";
          }

          btnSave.onclick = () => {
            if (typeof markModuleComplete === 'function') {
              markModuleComplete(moduleId || quiz.module_id, scorePct);
              btnSave.textContent = "✓ Progression enregistrée !";
              btnSave.disabled = true;
            }
          };
        }
      });
    });
  });
}
