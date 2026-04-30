from app.governance.promotion import PromotionEvaluator
from app.governance.candidate_assembler import CandidateAssembler
from app.governance.rollback import RollbackManager


def test_promotion_blocked_without_rollback():
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {})
    evaluator = PromotionEvaluator()
    report = evaluator.evaluate(bundle)
    assert report.readiness.value == "blocked"


def test_promotion_ready_with_rollback():
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {})

    rm = RollbackManager()
    ref = rm.prepare_rollback_ref(bundle)  # Mock using itself
    bundle.rollback_ref = ref

    evaluator = PromotionEvaluator()
    report = evaluator.evaluate(bundle)
    assert report.readiness.value == "ready"
