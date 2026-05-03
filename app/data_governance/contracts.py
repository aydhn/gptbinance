from typing import Dict, List, Optional
from app.data_governance.models import DataContract, SchemaVersionRef
from app.data_governance.exceptions import InvalidDataContractError

class DataContractRegistry:
    def __init__(self):
        self._contracts: Dict[str, DataContract] = {}

    def register_contract(self, contract: DataContract) -> None:
        if contract.contract_id in self._contracts:
            raise InvalidDataContractError(f"Contract {contract.contract_id} already exists")
        self._contracts[contract.contract_id] = contract

    def get_contract(self, contract_id: str) -> DataContract:
        if contract_id not in self._contracts:
            raise InvalidDataContractError(f"Contract {contract_id} not found")
        return self._contracts[contract_id]

    def list_contracts(self) -> List[DataContract]:
        return list(self._contracts.values())
