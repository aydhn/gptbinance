import pytest
from app.model_plane.contracts import InferenceContractRegistry
from app.model_plane.models import InferenceContract, OutputSchema
from app.model_plane.enums import OutputClass
from app.model_plane.exceptions import InvalidInferenceContractError


def test_contract_registry_valid():
    registry = InferenceContractRegistry()
    schema = OutputSchema(output_class=OutputClass.SCALAR_SCORE, description="Test")
    contract = InferenceContract(
        contract_id="contract_1",
        model_id="model_1",
        required_feature_manifest_id="manifest_1",
        expected_output_schema=schema,
        requires_calibration=True,
        requires_uncertainty=False,
        supports_abstention=True,
    )
    registry.register_contract(contract)
    assert registry.get_contract("contract_1") == contract
    assert registry.get_contract_for_model("model_1") == contract


def test_contract_registry_missing_fields():
    registry = InferenceContractRegistry()
    schema = OutputSchema(output_class=OutputClass.SCALAR_SCORE, description="Test")
    with pytest.raises(InvalidInferenceContractError):
        registry.register_contract(
            InferenceContract(
                contract_id="",
                model_id="model_1",
                required_feature_manifest_id="manifest_1",
                expected_output_schema=schema,
                requires_calibration=True,
                requires_uncertainty=False,
                supports_abstention=True,
            )
        )


def test_validate_contract_compliance():
    registry = InferenceContractRegistry()
    schema1 = OutputSchema(output_class=OutputClass.SCALAR_SCORE, description="Test")
    contract = InferenceContract(
        contract_id="contract_1",
        model_id="model_1",
        required_feature_manifest_id="manifest_1",
        expected_output_schema=schema1,
        requires_calibration=True,
        requires_uncertainty=False,
        supports_abstention=True,
    )
    registry.register_contract(contract)

    # Valid compliance
    violations = registry.validate_contract_compliance(contract, "manifest_1", schema1)
    assert len(violations) == 0

    # Invalid manifest
    violations = registry.validate_contract_compliance(contract, "manifest_2", schema1)
    assert len(violations) == 1

    # Invalid output class
    schema2 = OutputSchema(output_class=OutputClass.BINARY_CLASS, description="Test")
    violations = registry.validate_contract_compliance(contract, "manifest_1", schema2)
    assert len(violations) == 1
