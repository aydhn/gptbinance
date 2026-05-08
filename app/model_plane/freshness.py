from typing import Dict, Any
from app.model_plane.checkpoints import ModelCheckpointRegistry
from app.model_plane.calibration import CalibrationManager


class ModelFreshnessEvaluator:
    def __init__(
        self,
        checkpoint_registry: ModelCheckpointRegistry,
        calibration_manager: CalibrationManager,
    ):
        self.checkpoint_registry = checkpoint_registry
        self.calibration_manager = calibration_manager

    def evaluate_all(self, checkpoint_id: str) -> Dict[str, Any]:
        results = {
            "checkpoint_stale": False,
            "calibration_stale": False,
            "warnings": [],
        }

        try:
            results["checkpoint_stale"] = self.checkpoint_registry.evaluate_freshness(
                checkpoint_id
            )
        except Exception as e:
            results["warnings"].append(f"Checkpoint freshness eval failed: {str(e)}")

        cal_record = self.calibration_manager.get_latest_for_checkpoint(checkpoint_id)
        if cal_record:
            results[
                "calibration_stale"
            ] = self.calibration_manager.check_calibration_freshness(cal_record)
        else:
            results["warnings"].append("No calibration record found")
            results["calibration_stale"] = True

        return results
