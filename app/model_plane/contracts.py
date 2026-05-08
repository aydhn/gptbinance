from typing import Dict, List, Optional
from app.model_plane.models import InferenceContract, OutputSchema
from app.model_plane.exceptions import InvalidInferenceContractError


class InferenceContractRegistry:
    def __init__(self):
        self._contracts: Dict[str, InferenceContract] = {}

    def register_contract(self, contract: InferenceContract) -> None:
        if not contract.contract_id:
            raise InvalidInferenceContractError("Contract ID is required.")
        if not contract.model_id:
            raise InvalidInferenceContractError("Model ID is required.")
        if not contract.required_feature_manifest_id:
            raise InvalidInferenceContractError(
                "Required feature manifest ID is required."
            )
        if not contract.expected_output_schema:
            raise InvalidInferenceContractError("Expected output schema is required.")

        self._contracts[contract.contract_id] = contract

    def get_contract(self, contract_id: str) -> Optional[InferenceContract]:
        return self._contracts.get(contract_id)

    def get_contract_for_model(self, model_id: str) -> Optional[InferenceContract]:
        for contract in self._contracts.values():
            if contract.model_id == model_id:
                return contract
        return None

    def validate_contract_compliance(
        self,
        contract: InferenceContract,
        provided_manifest_id: str,
        actual_output: OutputSchema,
    ) -> List[str]:
        violations = []
        if contract.required_feature_manifest_id != provided_manifest_id:
            violations.append(
                f"Expected manifest {contract.required_feature_manifest_id}, got {provided_manifest_id}."
            )

        if contract.expected_output_schema.output_class != actual_output.output_class:
            violations.append(
                f"Expected output class {contract.expected_output_schema.output_class}, got {actual_output.output_class}."
            )

        return violations
