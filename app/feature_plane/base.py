from typing import List, Dict, Optional
from app.feature_plane.models import FeatureDefinition, DatasetContract


class FeatureRegistryBase:
    def register(self, feature: FeatureDefinition) -> None:
        raise NotImplementedError

    def get(self, feature_id: str) -> Optional[FeatureDefinition]:
        raise NotImplementedError

    def list_all(self) -> List[FeatureDefinition]:
        raise NotImplementedError


class PointInTimeValidatorBase:
    def validate(self, manifest_id: str, as_of: str) -> bool:
        raise NotImplementedError


class EquivalenceEvaluatorBase:
    def evaluate(self, manifest_a: str, manifest_b: str) -> bool:
        raise NotImplementedError


class DatasetContractEvaluatorBase:
    def evaluate(self, contract: DatasetContract, snapshot_id: str) -> bool:
        raise NotImplementedError
