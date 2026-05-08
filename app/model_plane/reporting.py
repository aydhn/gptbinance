from typing import Dict, Any, List
from app.model_plane.models import (
    ModelDefinition,
    ModelCheckpointRecord,
    InferenceManifest,
    InferenceContract,
)


class ModelPlaneReporting:
    @staticmethod
    def format_model_registry_summary(models: List[ModelDefinition]) -> str:
        summary = "--- Model Registry Summary ---\n"
        for m in models:
            summary += f"Model ID: {m.model_id} | Class: {m.model_class.value} | Domain: {m.domain.value} | Exp: {m.is_experimental}\n"
        return summary

    @staticmethod
    def format_checkpoint_summary(checkpoints: List[ModelCheckpointRecord]) -> str:
        summary = "--- Checkpoint Summary ---\n"
        for c in checkpoints:
            summary += f"Checkpoint: {c.checkpoint_id} | Model: {c.model_id} | Stale: {c.is_stale}\n"
        return summary

    @staticmethod
    def format_inference_manifest(manifest: InferenceManifest) -> str:
        summary = f"--- Inference Manifest: {manifest.manifest_id} ---\n"
        for entry in manifest.entries:
            summary += f"  - Model: {entry.model_ref.model_id} | Checkpoint: {entry.checkpoint_id}\n"
        return summary

    @staticmethod
    def format_contracts_summary(contracts: List[InferenceContract]) -> str:
        summary = "--- Inference Contracts ---\n"
        for c in contracts:
            summary += f"Contract: {c.contract_id} | Model: {c.model_id} | Expected Output: {c.expected_output_schema.output_class.value}\n"
        return summary
