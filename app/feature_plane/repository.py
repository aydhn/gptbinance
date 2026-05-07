from typing import Optional
from app.feature_plane.models import FeatureDefinition, DatasetContract
from app.feature_plane.features import CanonicalFeatureRegistry
from app.feature_plane.contracts import DatasetContractRegistry


class FeaturePlaneRepository:
    def __init__(self):
        self.feature_registry = CanonicalFeatureRegistry()
        self.contract_registry = DatasetContractRegistry()

    def get_feature(self, feature_id: str) -> Optional[FeatureDefinition]:
        return self.feature_registry.get(feature_id)

    def get_contract(self, contract_id: str) -> Optional[DatasetContract]:
        return self.contract_registry.get(contract_id)
