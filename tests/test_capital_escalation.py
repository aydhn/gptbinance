from app.capital.escalation import escalation_engine
from app.capital.evidence import build_evidence_bundle
from datetime import datetime, timezone


def test_strict_escalation_evaluator():
    now = datetime.now(timezone.utc)
    bundle = build_evidence_bundle(
        refs={"qualification_pass": "1", "ledger_clean": "2", "stress_pass": "3"},
        timestamps={"qualification_pass": now, "ledger_clean": now, "stress_pass": now},
    )

    # testnet_zero -> canary_micro
    res = escalation_engine.check_escalation_readiness(
        "testnet_zero", "canary_micro", bundle
    )
    assert res.readiness.is_ready is True

    # missing evidence
    bundle_missing = build_evidence_bundle({}, {})
    res_missing = escalation_engine.check_escalation_readiness(
        "testnet_zero", "canary_micro", bundle_missing
    )
    assert res_missing.readiness.is_ready is False
