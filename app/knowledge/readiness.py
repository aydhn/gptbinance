from typing import Dict, Any, List
from datetime import datetime, timezone
from app.knowledge.models import OperatorReadinessRecord
from app.knowledge.enums import ReadinessLevel, QuizVerdict
from app.knowledge.quizzes import quiz_registry


class OperatorReadinessEvaluator:
    def __init__(self, expiry_days: int = 180):
        self.expiry_days = expiry_days

    def evaluate(
        self, operator_id: str, role: str, context: Dict[str, Any] = None
    ) -> OperatorReadinessRecord:
        results = quiz_registry.get_results_for_operator(operator_id)

        # Advisory checks
        # Assuming we have required quizzes for roles (mocked here)
        required_quizzes = (
            ["QZ-OPS-001", "QZ-SEC-001"] if role == "ops" else ["QZ-BASE-001"]
        )

        passed_quizzes = set()
        stale_reasons = []
        now = datetime.now(timezone.utc)

        for res in results:
            if res.verdict == QuizVerdict.PASS:
                if (now - res.taken_at).days > self.expiry_days:
                    stale_reasons.append(f"Quiz {res.quiz_id} expired.")
                else:
                    passed_quizzes.add(res.quiz_id)

        level = ReadinessLevel.READY
        for req in required_quizzes:
            if req not in passed_quizzes:
                stale_reasons.append(f"Missing required quiz: {req}")
                level = (
                    ReadinessLevel.CAUTION
                )  # Advisory, so caution instead of hard fail usually

        if len(stale_reasons) > len(required_quizzes):
            level = ReadinessLevel.EXPIRED

        if context and context.get("major_release_change"):
            stale_reasons.append(
                "Major release change detected. Re-evaluation advised."
            )
            level = ReadinessLevel.CAUTION

        return OperatorReadinessRecord(
            operator_id=operator_id,
            role=role,
            readiness_level=level,
            completed_quizzes=list(passed_quizzes),
            stale_readiness_reasons=stale_reasons,
            last_evaluated_at=now,
        )


readiness_evaluator = OperatorReadinessEvaluator()
