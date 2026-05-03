from typing import List, Dict, Optional
from app.knowledge.models import ReadinessQuiz, QuizResult
from app.knowledge.enums import QuizVerdict
from datetime import datetime, timezone


class QuizRegistry:
    def __init__(self):
        self._quizzes: Dict[str, ReadinessQuiz] = {}
        self._results: List[QuizResult] = []

    def register_quiz(self, quiz: ReadinessQuiz) -> None:
        self._quizzes[quiz.quiz_id] = quiz

    def get_quiz(self, quiz_id: str) -> Optional[ReadinessQuiz]:
        return self._quizzes.get(quiz_id)

    def record_result(self, result: QuizResult) -> None:
        self._results.append(result)

    def evaluate_quiz(
        self, quiz_id: str, operator_id: str, answers: List[int]
    ) -> QuizResult:
        quiz = self.get_quiz(quiz_id)
        if not quiz:
            raise ValueError("Quiz not found")

        correct = 0
        for i, q in enumerate(quiz.questions):
            if i < len(answers) and answers[i] == q.correct_option_index:
                correct += 1

        score = (correct / len(quiz.questions)) * 100 if quiz.questions else 0.0

        verdict = QuizVerdict.FAIL
        if score >= quiz.passing_score:
            verdict = QuizVerdict.PASS
        elif score >= (quiz.passing_score - 10):
            verdict = QuizVerdict.CAUTION

        result = QuizResult(
            quiz_id=quiz_id,
            operator_id=operator_id,
            score=score,
            verdict=verdict,
            taken_at=datetime.now(timezone.utc),
        )
        self.record_result(result)
        return result

    def get_results_for_operator(self, operator_id: str) -> List[QuizResult]:
        return [r for r in self._results if r.operator_id == operator_id]


quiz_registry = QuizRegistry()
