async function loadQuiz(quizPath, containerId) {
  try {
    const res = await fetch(quizPath);
    const quiz = await res.json();
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = quiz.questions.map((q, i) => `
      <fieldset class="quiz-question" data-qid="${q.id}">
        <legend>Question ${i + 1} : ${q.question}</legend>
        ${q.choices.map(c => `
          <label class="quiz-choice">
            <input type="radio" name="${q.id}" value="${c.key}">
            <span><strong>${c.key.toUpperCase()}.</strong> ${c.text}</span>
          </label>
        `).join('')}
        <div class="quiz-feedback" hidden></div>
      </fieldset>
    `).join('');

    container.querySelectorAll('input[type=radio]').forEach(input => {
      input.addEventListener('change', () => handleAnswer(input, quiz));
    });
  } catch (err) {
    console.error('Erreur chargement quiz:', err);
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

  feedbackEl.innerHTML = `<strong>${isCorrect ? '✓ Réponse exacte !' : '✗ Réponse incorrecte.'}</strong> ${question.feedback}`;
  feedbackEl.hidden = false;
  feedbackEl.style.opacity = '0';
  feedbackEl.style.transition = 'opacity 0.2s ease';
  requestAnimationFrame(() => { feedbackEl.style.opacity = '1'; });
}