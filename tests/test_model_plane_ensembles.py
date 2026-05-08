import pytest
from app.model_plane.ensembles import EnsembleGovernance
from app.model_plane.models import EnsemblePolicy, ModelRef
from app.model_plane.enums import EnsembleClass
from app.model_plane.exceptions import ModelPlaneError


def test_ensemble_registry():
    gov = EnsembleGovernance()
    policy = EnsemblePolicy(
        policy_id="ens_1",
        ensemble_class=EnsembleClass.WEIGHTED_AVERAGE,
        model_refs=[
            ModelRef(model_id="m1", version="1"),
            ModelRef(model_id="m2", version="1"),
        ],
        weights=[0.6, 0.4],
        description="test",
    )
    gov.register_policy(policy)
    assert gov.get_policy("ens_1") == policy


def test_ensemble_validation():
    gov = EnsembleGovernance()

    # Valid
    policy1 = EnsemblePolicy(
        policy_id="ens_1",
        ensemble_class=EnsembleClass.WEIGHTED_AVERAGE,
        model_refs=[ModelRef(model_id="m1", version="1")],
        weights=[1.0],
        description="test",
    )
    gov.register_policy(policy1)
    assert gov.validate_ensemble_consistency("ens_1") is True

    # Invalid weights
    policy2 = EnsemblePolicy(
        policy_id="ens_2",
        ensemble_class=EnsembleClass.WEIGHTED_AVERAGE,
        model_refs=[ModelRef(model_id="m1", version="1")],
        weights=[0.6, 0.4],
        description="test",
    )
    gov.register_policy(policy2)
    assert gov.validate_ensemble_consistency("ens_2") is False


def test_ensemble_missing_fields():
    gov = EnsembleGovernance()
    with pytest.raises(ModelPlaneError):
        gov.register_policy(
            EnsemblePolicy(
                policy_id="",
                ensemble_class=EnsembleClass.WEIGHTED_AVERAGE,
                model_refs=[ModelRef(model_id="m1", version="1")],
                description="test",
            )
        )
