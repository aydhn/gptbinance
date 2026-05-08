import pytest
from app.model_plane.thresholds import ThresholdPolicyRegistry
from app.model_plane.models import ThresholdPolicy
from app.model_plane.enums import ThresholdClass
from app.model_plane.exceptions import ThresholdPolicyViolation


def test_threshold_registry():
    registry = ThresholdPolicyRegistry()
    policy = ThresholdPolicy(
        policy_id="tp_1",
        model_id="m1",
        threshold_class=ThresholdClass.DECISION,
        value=0.8,
        description="test",
    )
    registry.register_policy(policy)
    assert registry.get_policy("tp_1") == policy
    assert len(registry.get_policies_for_model("m1")) == 1


def test_threshold_validation():
    registry = ThresholdPolicyRegistry()
    policy = ThresholdPolicy(
        policy_id="tp_1",
        model_id="m1",
        threshold_class=ThresholdClass.DECISION,
        value=0.8,
        description="test",
    )
    registry.register_policy(policy)

    assert registry.validate_threshold_usage("m1", "tp_1") is True
    assert registry.validate_threshold_usage("m1", None) is True
    assert registry.validate_threshold_usage("m1", "tp_missing") is False
    assert registry.validate_threshold_usage("m2", "tp_1") is False


def test_threshold_missing_fields():
    registry = ThresholdPolicyRegistry()
    with pytest.raises(ThresholdPolicyViolation):
        registry.register_policy(
            ThresholdPolicy(
                policy_id="",
                model_id="m1",
                threshold_class=ThresholdClass.DECISION,
                value=0.8,
                description="test",
            )
        )
