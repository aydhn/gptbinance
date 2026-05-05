from typing import Dict, Any, Optional
from app.data_governance.models import DatasetRef, SchemaVersionRef, LineageNode


class FeatureRepository:
    def __init__(self):
        self._features = {}

    def save_feature_set(
        self,
        feature_id: str,
        version: str,
        data: Any,
        schema_ref: SchemaVersionRef,
        lineage: Optional[LineageNode] = None,
    ):
        self._features[f"{feature_id}:{version}"] = {
            "data": data,
            "schema_ref": schema_ref,
            "lineage": lineage,
        }

    def get_feature_set(self, feature_id: str, version: str) -> Dict[str, Any]:
        return self._features.get(f"{feature_id}:{version}")
