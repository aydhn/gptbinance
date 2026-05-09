# Comparisons and contracts
from app.experiment_plane.models import ComparisonContract


def build_standard_contract(contract_id: str) -> ComparisonContract:
    return ComparisonContract(contract_id=contract_id)
