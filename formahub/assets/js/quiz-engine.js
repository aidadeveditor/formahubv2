/* ============================================================
   Formahub — moteur de quiz (V6)
   Feedback immédiat, score en direct, barre de progression.
   ============================================================ */

async function loadQuiz(quizPath, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  try {
    const res = await fetch(quizPath);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const quiz = await res.json();
    const questions = quiz.questions || [];
    if (!questions.length) return;

    const answered = new Map();

    // Barre de progression du quiz, insérée avant les questions
    const progress = document.createElement('div');
    progress.className = 'quiz-progress';
    progress.innerHTML =
      '<span class="quiz-score">0 / ' + questions.length + '</span>' +
      '<div class="progress-bar"><div class="progress-bar-fill"></div></div>' +
      '<span class="quiz-status">À démarrer</span>';
    container.parentNode.insertBefore(progress, container);

    container.innerHTML = questions.map((q, i) => `
      <fieldset class="quiz-question" data-qid="${q.id}">
        <legend>Question ${i + 1} : ${q.question}</legend>
        ${(q.choices || []).map(c => `
          <label class="quiz-choice">
            <input type="radio" name="${q.id}" value="${c.key}">
            <span><strong>${String(c.key).toUpperCase()}.</strong> ${c.text}</span>
          </label>
        `).join('')}
        <div class="quiz-feedback" hidden></div>
      </fieldset>
    `).join('');

    container.querySelectorAll('input[type=radio]').forEach(input => {
      input.addEventListener('change', () => {
        handleAnswer(input, quiz);
        updateQuizProgress(progress, questions, answered, input);
      });
    });
  } catch (err) {
    console.error('Erreur chargement quiz:', err);
    container.innerHTML =
      '<div class="pitfall-box"><h4>⚠️ Quiz indisponible</h4>' +
      '<p>Le fichier du quiz n\'a pas pu être chargé. Ouvrez la page via un serveur local ' +
      '(<code>python -m http.server</code>) plutôt qu\'en double-cliquant le fichier.</p></div>';
  }
}

function handleAnswer(input, quiz) {
  const fieldset = input.closest('.quiz-question');
  const qid = fieldset.dataset.qid;
  const question = quiz.questions.find(q => q.id === qid);
  const feedbackEl = fieldset.querySelector('.quiz-feedback');
  const isCorrect = input.value === question.correct_answer;

  fieldset.classList.toggle('correct', isCorrect);
  fieldset.classList.toggle('incorrect', !isCorrect);
  fieldset.dataset.result = isCorrect ? 'ok' : 'ko';

  feedbackEl.innerHTML =
    `<strong>${isCorrect ? '✓ Réponse exacte !' : '✗ Réponse incorrecte.'}</strong> ${question.feedback || ''}`;
  feedbackEl.hidden = false;
  feedbackEl.style.opacity = '0';
  feedbackEl.style.transition = 'opacity 0.2s ease';
  requestAnimationFrame(() => { feedbackEl.style.opacity = '1'; });
}

function updateQuizProgress(progress, questions, answered, input) {
  const fieldset = input.closest('.quiz-question');
  answered.set(fieldset.dataset.qid, fieldset.dataset.result === 'ok');

  const done = answered.size;
  const good = Array.from(answered.values()).filter(Boolean).length;
  const pct = Math.round((done / questions.length) * 100);

  progress.querySelector('.quiz-score').textContent = `${good} / ${questions.length}`;
  progress.querySelector('.progress-bar-fill').style.width = pct + '%';

  const status = progress.querySelector('.quiz-status');
  if (done < questions.length) {
    status.textContent = `${done}/${questions.length} répondues`;
  } else {
    const ratio = good / questions.length;
    status.textContent = ratio === 1 ? '🏆 Sans faute !'
      : ratio >= 0.7 ? '👍 Acquis'
      : '📖 À revoir';
  }
}
