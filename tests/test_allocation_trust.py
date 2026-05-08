from app.allocation.trust import TrustEvaluator
from app.allocation.enums import TrustVerdict


def test_trust():
    evaluator = TrustEvaluator()
    rep1 = evaluator.evaluate(signals_healthy=True, budgets_healthy=True)
    assert rep1.verdict == TrustVerdict.TRUSTED

    rep2 = evaluator.evaluate(signals_healthy=False, budgets_healthy=True)
    assert rep2.verdict == TrustVerdict.CAUTION

    rep3 = evaluator.evaluate(signals_healthy=True, budgets_healthy=False)
    assert rep3.verdict == TrustVerdict.DEGRADED
