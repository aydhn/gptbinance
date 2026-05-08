from typing import Dict, List, Any
from app.model_plane.models import InferenceManifest
from app.model_plane.exceptions import ModelPlaneError


class ModelResolutionReport:
    def __init__(self):
        self.resolved_components: Dict[str, Any] = {}
        self.blockers: List[str] = []
        self.proof_notes: List[str] = []


class ModelResolutionEngine:
    def resolve_manifest(self, manifest: InferenceManifest) -> ModelResolutionReport:
        report = ModelResolutionReport()

        if not manifest.entries:
            report.blockers.append("Manifest contains no entries")

        for entry in manifest.entries:
            model_id = entry.model_ref.model_id
            report.resolved_components[model_id] = {
                "checkpoint_id": entry.checkpoint_id,
                "threshold_policy_id": entry.threshold_policy_id,
                "abstention_policy_id": entry.abstention_policy_id,
            }
            if not entry.threshold_policy_id:
                report.proof_notes.append(
                    f"No threshold policy specified for {model_id}, relying on default/raw output"
                )

        if manifest.ensemble_policy_id:
            report.proof_notes.append(
                f"Ensemble policy {manifest.ensemble_policy_id} is active"
            )

        return report
