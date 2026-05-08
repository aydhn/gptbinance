from typing import Dict, Any, List
from app.model_plane.models import InferenceManifest, ModelPlaneBaseModel
from app.model_plane.inference import (
    InferenceRequest,
    InferenceResponse,
    InferenceDescriptorLayer,
)
from datetime import datetime


class OfflineScoringRun(ModelPlaneBaseModel):
    run_id: str
    manifest_id: str
    dataset_ref: str
    scored_records: int
    caveats: List[str]


class OfflineEvaluationEngine:
    def __init__(self, inference_layer: InferenceDescriptorLayer):
        self.inference_layer = inference_layer

    def run_deterministic_scoring(
        self,
        run_id: str,
        manifest: InferenceManifest,
        dataset_ref: str,
        inputs: List[Dict[str, Any]],
    ) -> OfflineScoringRun:
        caveats = []
        if not manifest.entries:
            caveats.append("No models in manifest to score")

        scored_records = 0
        for idx, input_features in enumerate(inputs):
            req = InferenceRequest(
                request_id=f"{run_id}-{idx}",
                manifest_id=manifest.manifest_id,
                features=input_features,
                timestamp=datetime.now(),
            )
            # Mock calling the inference layer - normally we'd pass outputs back from the model
            # This establishes that offline uses the same inference descriptor contract
            scored_records += 1

        return OfflineScoringRun(
            run_id=run_id,
            manifest_id=manifest.manifest_id,
            dataset_ref=dataset_ref,
            scored_records=scored_records,
            caveats=caveats,
        )
