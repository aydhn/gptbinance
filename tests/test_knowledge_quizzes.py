import pytest
from app.knowledge.models import ReadinessQuiz, QuizQuestion
from app.knowledge.enums import QuizVerdict
from app.knowledge.quizzes import QuizRegistry


def test_quiz_evaluation():
    q_reg = QuizRegistry()
    q = ReadinessQuiz(
        quiz_id="Q-001",
        module_id="M-001",
        title="Test Quiz",
        passing_score=100.0,
        questions=[
            QuizQuestion(
                question_id="1", text="A?", options=["A", "B"], correct_option_index=0
            )
        ],
    )
    q_reg.register_quiz(q)

    res = q_reg.evaluate_quiz("Q-001", "u1", [0])
    assert res.verdict == QuizVerdict.PASS
    assert res.score == 100.0

    res_fail = q_reg.evaluate_quiz("Q-001", "u2", [1])
    assert res_fail.verdict == QuizVerdict.FAIL
    assert res_fail.score == 0.0
