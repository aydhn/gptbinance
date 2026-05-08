import pytest
from app.model_plane.abstention import AbstentionPolicyHandler
from app.model_plane.models import AbstentionPolicy, UncertaintyRecord
from app.model_plane.enums import UncertaintyClass
from app.model_plane.exceptions import ModelPlaneError
from datetime import datetime


def test_abstention_policy_registry():
    handler = AbstentionPolicyHandler()
    policy = AbstentionPolicy(
        policy_id="ab_1",
        model_id="m1",
        allow_reject=True,
        min_confidence_required=0.8,
        fallback_strategy="zero_weight",
    )
    handler.register_policy(policy)
    assert handler.get_policy("ab_1") == policy


def test_evaluate_abstention_degraded_truth():
    handler = AbstentionPolicyHandler()
    policy = AbstentionPolicy(
        policy_id="ab_1",
        model_id="m1",
        allow_reject=True,
        min_confidence_required=0.8,
        fallback_strategy="zero_weight",
    )
    handler.register_policy(policy)

    unc_record = UncertaintyRecord(
        record_id="unc1",
        checkpoint_id="chk1",
        evaluated_at=datetime.now(),
        uncertainty_class=UncertaintyClass.HIGH_CONFIDENCE,
        summary={},
    )

    should_abstain, reasons = handler.evaluate_abstention(
        "ab_1", unc_record, market_truth_degraded=True
    )
    assert should_abstain is True
    assert "Market truth is degraded" in reasons


def test_evaluate_abstention_low_confidence():
    handler = AbstentionPolicyHandler()
    policy = AbstentionPolicy(
        policy_id="ab_1",
        model_id="m1",
        allow_reject=True,
        min_confidence_required=0.8,
        fallback_strategy="zero_weight",
    )
    handler.register_policy(policy)

    unc_record = UncertaintyRecord(
        record_id="unc1",
        checkpoint_id="chk1",
        evaluated_at=datetime.now(),
        uncertainty_class=UncertaintyClass.LOW_CONFIDENCE,
        summary={},
    )

    should_abstain, reasons = handler.evaluate_abstention(
        "ab_1", unc_record, market_truth_degraded=False
    )
    assert should_abstain is True
    assert "Low confidence" in reasons


def test_evaluate_abstention_no_uncertainty_record():
    handler = AbstentionPolicyHandler()
    policy = AbstentionPolicy(
        policy_id="ab_1",
        model_id="m1",
        allow_reject=True,
        min_confidence_required=0.8,
        fallback_strategy="zero_weight",
    )
    handler.register_policy(policy)

    should_abstain, reasons = handler.evaluate_abstention(
        "ab_1", None, market_truth_degraded=False
    )
    assert should_abstain is True
    assert "No uncertainty record found" in reasons
