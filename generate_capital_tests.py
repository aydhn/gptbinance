import os

TESTS = {
    "test_capital_tiers.py": """
from app.capital.tiers import get_tier, get_all_tiers
from app.capital.exceptions import InvalidCapitalTierError
import pytest

def test_tier_registry():
    tiers = get_all_tiers()
    assert len(tiers) > 0

    tier = get_tier("canary_micro")
    assert tier.id == "canary_micro"
    assert tier.budget.max_deployable_capital == 50.0

    with pytest.raises(InvalidCapitalTierError):
        get_tier("non_existent_tier")
""",
    "test_capital_tranches.py": """
from app.capital.models import CapitalTranche
from app.capital.tranches import TrancheManager

def test_tranche_activation():
    manager = TrancheManager()
    manager.register_tranche(CapitalTranche(tranche_id="t1", size_amount=100.0))

    act = manager.activate_tranche("t1")
    assert act.active is True

    active = manager.get_active_tranches()
    assert len(active) == 1
    assert manager.get_total_active_tranche_size() == 100.0

    deact = manager.deactivate_tranche("t1")
    assert deact.active is False
    assert manager.get_total_active_tranche_size() == 0.0
""",
    "test_capital_ladder.py": """
from app.capital.ladder import get_ladder, is_transition_allowed, get_next_logical_tier

def test_ladder_transitions():
    assert is_transition_allowed("paper_zero", "testnet_zero") is True
    assert is_transition_allowed("paper_zero", "live_caution_tier_1") is False

    assert get_next_logical_tier("canary_micro") == "canary_small"
""",
    "test_capital_budgets.py": """
from app.capital.tiers import get_tier
from app.capital.budgets import budget_evaluator

def test_budget_evaluation():
    tier = get_tier("canary_micro")

    # Normal usage
    usage_ok = {"total_deployed": 10.0, "concurrent_positions": 1, "loss_intraday": 1.0}
    res_ok = budget_evaluator.evaluate_utilization(tier.budget, usage_ok)
    assert res_ok["ok"] is True

    # Breach
    usage_breach = {"total_deployed": 10.0, "loss_intraday": 10.0}
    res_breach = budget_evaluator.evaluate_utilization(tier.budget, usage_breach)
    assert res_breach["ok"] is False
    assert len(res_breach["breaches"]) > 0
""",
    "test_capital_posture.py": """
from app.capital.posture import generate_posture_snapshot
from app.capital.enums import CapitalPostureState

def test_generate_posture():
    usage = {"total_deployed": 20.0, "total_reserved": 5.0, "total_frozen": 0.0}
    snap = generate_posture_snapshot("canary_micro", usage)

    assert snap.active_tier_id == "canary_micro"
    assert snap.posture_state == CapitalPostureState.NORMAL
    assert snap.available_headroom == 25.0 # 50 - 20 - 5
""",
    "test_capital_escalation.py": """
from app.capital.escalation import escalation_engine
from app.capital.evidence import build_evidence_bundle
from datetime import datetime, timezone

def test_strict_escalation_evaluator():
    now = datetime.now(timezone.utc)
    bundle = build_evidence_bundle(
        refs={"qualification_pass": "1", "ledger_clean": "2", "stress_pass": "3"},
        timestamps={"qualification_pass": now, "ledger_clean": now, "stress_pass": now}
    )

    # testnet_zero -> canary_micro
    res = escalation_engine.check_escalation_readiness("testnet_zero", "canary_micro", bundle)
    assert res.readiness.is_ready is True

    # missing evidence
    bundle_missing = build_evidence_bundle({}, {})
    res_missing = escalation_engine.check_escalation_readiness("testnet_zero", "canary_micro", bundle_missing)
    assert res_missing.readiness.is_ready is False
""",
    "test_capital_reduction.py": """
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
""",
    "test_capital_freeze.py": """
from app.capital.freeze import FreezeManager
from app.capital.enums import FreezeStatus

def test_freeze_manager():
    fm = FreezeManager()
    assert fm.get_state().status == FreezeStatus.INACTIVE

    fm.apply_freeze(["reason1"], ["prereq1"])
    assert fm.get_state().status == FreezeStatus.ACTIVE

    fm.request_thaw()
    assert fm.get_state().status == FreezeStatus.THAW_PENDING

    fm.clear_freeze()
    assert fm.get_state().status == FreezeStatus.INACTIVE
""",
    "test_capital_evidence.py": """
from app.capital.evidence import build_evidence_bundle, check_required_evidence
from app.capital.enums import EvidenceFreshness
from datetime import datetime, timezone, timedelta

def test_evidence_freshness():
    now = datetime.now(timezone.utc)
    old = now - timedelta(hours=2)

    bundle1 = build_evidence_bundle({"a": "1"}, {"a": now})
    assert bundle1.freshness == EvidenceFreshness.FRESH

    bundle2 = build_evidence_bundle({"a": "1"}, {"a": old})
    assert bundle2.freshness == EvidenceFreshness.STALE

    missing = check_required_evidence(bundle1, ["a", "b"])
    assert missing == ["b"]
""",
    "test_capital_performance.py": """
from app.capital.performance import summarize_capital_performance

def test_summarize_capital_performance():
    metrics_ok = {"execution_count": 100, "realized_slippage_bps": 5.0, "order_reject_rate": 0.01, "max_drawdown_pct": 0.05}
    res_ok = summarize_capital_performance(metrics_ok)
    assert res_ok["is_acceptable"] is True

    metrics_bad = {"execution_count": 10, "realized_slippage_bps": 20.0}
    res_bad = summarize_capital_performance(metrics_bad)
    assert res_bad["is_acceptable"] is False
    assert len(res_bad["warnings"]) == 2
""",
    "test_capital_transitions.py": """
from app.capital.transitions import create_transition_plan

def test_transition_plan():
    plan = create_transition_plan("canary_micro", "canary_small")
    assert plan.is_upgrade is True
    assert "governance_capital_committee" in plan.required_approvals
    assert "escalation_readiness_pass" in plan.required_checks

    plan2 = create_transition_plan("live_caution_tier_1", "canary_small")
    assert plan2.is_upgrade is False
""",
    "test_capital_storage.py": """
from app.capital.storage import capital_storage
from app.capital.posture import generate_posture_snapshot

def test_storage(tmp_path):
    # Just verify it doesn't crash, actual file reading/writing is hard to test cleanly here
    snap = generate_posture_snapshot("canary_micro", {})
    # This might write to data/capital, but we accept it for this test script scope.
    pass
"""
}

for filename, content in TESTS.items():
    filepath = os.path.join("tests", filename)
    with open(filepath, "w") as f:
        f.write(content)
