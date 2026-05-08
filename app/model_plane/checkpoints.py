from typing import Dict, List, Optional
from datetime import datetime, timezone, timedelta
from app.model_plane.models import ModelCheckpointRecord
from app.model_plane.exceptions import InvalidCheckpointRecordError


class ModelCheckpointRegistry:
    def __init__(self, stale_threshold_days: int = 30):
        self._checkpoints: Dict[str, ModelCheckpointRecord] = {}
        self.stale_threshold_days = stale_threshold_days

    def register_checkpoint(self, checkpoint: ModelCheckpointRecord) -> None:
        if not checkpoint.checkpoint_id:
            raise InvalidCheckpointRecordError("Checkpoint ID is required.")
        if not checkpoint.model_id:
            raise InvalidCheckpointRecordError("Model ID is required.")
        if not checkpoint.artifact or not checkpoint.artifact.checksum:
            raise InvalidCheckpointRecordError("Valid artifact is required.")

        self._checkpoints[checkpoint.checkpoint_id] = checkpoint

    def get_checkpoint(self, checkpoint_id: str) -> Optional[ModelCheckpointRecord]:
        return self._checkpoints.get(checkpoint_id)

    def get_checkpoints_for_model(self, model_id: str) -> List[ModelCheckpointRecord]:
        return [c for c in self._checkpoints.values() if c.model_id == model_id]

    def evaluate_freshness(self, checkpoint_id: str) -> bool:
        """Returns True if the checkpoint is stale."""
        checkpoint = self.get_checkpoint(checkpoint_id)
        if not checkpoint:
            raise InvalidCheckpointRecordError(f"Checkpoint {checkpoint_id} not found.")

        now = datetime.now(timezone.utc)
        # Assuming checkpoint.created_at is UTC aware, if not we'd need to force it.
        age = now - checkpoint.created_at

        is_stale = age > timedelta(days=self.stale_threshold_days)
        checkpoint.is_stale = is_stale
        return is_stale
