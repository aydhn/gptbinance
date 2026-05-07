from typing import Dict, Optional, List
from app.feature_plane.models import DatasetContract
from app.feature_plane.exceptions import InvalidDatasetContractError


class DatasetContractRegistry:
    def __init__(self):
        self._contracts: Dict[str, DatasetContract] = {}

    def register(self, contract: DatasetContract) -> None:
        if not contract.contract_id:
            raise InvalidDatasetContractError("Contract must have an ID")
        self._contracts[contract.contract_id] = contract

    def get(self, contract_id: str) -> Optional[DatasetContract]:
        return self._contracts.get(contract_id)

    def list_all(self) -> List[DatasetContract]:
        return list(self._contracts.values())
