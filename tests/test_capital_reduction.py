from app.capital.reduction import evaluate_reduction_needs
from app.capital.enums import ReductionVerdict


def test_reduction_needs():
    usage = {"total_deployed": 10.0, "loss_intraday": 0.0}
    res1 = evaluate_reduction_needs("canary_micro", usage)
    assert res1.verdict == ReductionVerdict.HOLD

    res2 = evaluate_reduction_needs("canary_micro", usage, external_alerts=5)
    assert res2.verdict == ReductionVerdict.REDUCE

    res3 = evaluate_reduction_needs("canary_micro", usage, reconciliation_mismatch=True)
    assert res3.verdict == ReductionVerdict.FREEZE
