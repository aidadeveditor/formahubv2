/**
 * Formahub — Moteur de Quiz Dynamique (quiz-engine.js)
 * Conforme au cahier des charges Formahub V3
 */

function renderQuiz(quizData, container) {
  const { module_id, questions } = quizData;
  let userAnswers = {};

  let html = `
    <div class="quiz-wrapper" data-module="${module_id}">
      <div class="quiz-header">
        <h3 class="quiz-title">Auto-évaluation formative</h3>
        <p class="quiz-subtitle">${questions.length} questions pour valider vos acquis</p>
      </div>
      <div class="quiz-questions">
  `;

  questions.forEach((q, idx) => {
    html += `
      <div class="quiz-question-card" id="card-${q.id}">
        <p class="quiz-question-text"><span class="q-num">Q${idx + 1}.</span> ${q.question}</p>
        <div class="quiz-choices" role="radiogroup" aria-label="Question ${idx + 1}">
          ${q.choices.map(c => `
            <button type="button" 
                    class="quiz-choice-btn" 
                    data-qid="${q.id}" 
                    data-key="${c.key}" 
                    data-correct="${q.correct_answer}">
              <span class="choice-key">${c.key.toUpperCase()}</span>
              <span class="choice-text">${c.text}</span>
            </button>
          `).join('')}
        </div>
        <div class="quiz-feedback" id="feedback-${q.id}" style="display:none;" aria-live="polite">
          <p class="feedback-text">${q.feedback}</p>
        </div>
      </div>
    `;
  });

  html += `
      </div>
      <div class="quiz-actions" style="margin-top: 1.5rem; text-align: center;">
        <div id="quiz-score-display" style="display:none; font-weight:600; margin-bottom:1rem; font-size:1.1rem; color:#1e293b;"></div>
        <button type="button" id="btn-save-progress" class="btn btn-primary" style="display:none; padding:0.6rem 1.2rem; background:#2563eb; color:#fff; border:none; border-radius:6px; font-weight:600; cursor:pointer;">
          Enregistrer ma progression
        </button>
      </div>
    </div>
  `;

  container.innerHTML = html;

  container.querySelectorAll('.quiz-choice-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const qid = btn.getAttribute('data-qid');
      const selectedKey = btn.getAttribute('data-key');
      const correctKey = btn.getAttribute('data-correct');

      if (userAnswers[qid]) return;
      userAnswers[qid] = selectedKey;

      const card = document.getElementById(`card-${qid}`);
      const buttons = card.querySelectorAll('.quiz-choice-btn');
      const feedbackEl = document.getElementById(`feedback-${qid}`);

      buttons.forEach(b => {
        b.disabled = true;
        const bKey = b.getAttribute('data-key');
        if (bKey === correctKey) {
          b.classList.add('choice-correct');
        } else if (bKey === selectedKey && selectedKey !== correctKey) {
          b.classList.add('choice-incorrect');
        }
      });

      feedbackEl.style.display = 'block';

      if (Object.keys(userAnswers).length === questions.length) {
        let correctCount = 0;
        questions.forEach(q => {
          if (userAnswers[q.id] === q.correct_answer) correctCount++;
        });

        const scorePct = Math.round((correctCount / questions.length) * 100);
        const scoreDisplay = document.getElementById('quiz-score-display');
        const saveBtn = document.getElementById('btn-save-progress');

        scoreDisplay.innerHTML = `Score : <strong>${scorePct}%</strong> (${correctCount}/${questions.length} bonnes réponses)`;
        scoreDisplay.style.display = 'block';
        saveBtn.style.display = 'inline-block';

        saveBtn.addEventListener('click', () => {
          localStorage.setItem(`formahub_module_${module_id}`, JSON.stringify({
            completed: true,
            score: scorePct,
            completedAt: new Date().toISOString()
          }));
          saveBtn.innerText = '✓ Progression enregistrée !';
          saveBtn.disabled = true;
        });
      }
    });
  });
}
