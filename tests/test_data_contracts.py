import pytest
from app.data_governance import DataContractRegistry, DataContract, ContractType, SchemaVersionRef, InvalidDataContractError

def test_data_contract_registration():
    registry = DataContractRegistry()
    contract = DataContract(
        contract_id="c1",
        contract_type=ContractType.RAW,
        schema_ref=SchemaVersionRef(schema_id="s1", version="v1"),
        required_fields=["id"],
        optional_fields=["notes"],
        unique_keys=["id"],
        description="Test contract"
    )
    registry.register_contract(contract)
    assert registry.get_contract("c1").contract_id == "c1"

def test_data_contract_duplicate():
    registry = DataContractRegistry()
    contract = DataContract(
        contract_id="c1",
        contract_type=ContractType.RAW,
        schema_ref=SchemaVersionRef(schema_id="s1", version="v1"),
        required_fields=[],
        optional_fields=[],
        unique_keys=[],
        description=""
    )
    registry.register_contract(contract)
    with pytest.raises(InvalidDataContractError):
         registry.register_contract(contract)
