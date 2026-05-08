from typing import Dict, Any, List
from app.model_plane.models import ModelPlaneBaseModel
import uuid


class ModelQualityVerdict(ModelPlaneBaseModel):
    verdict_id: str
    model_id: str
    missing_output_rate: float
    abstention_rate: float
    is_acceptable: bool
    warnings: List[str]


class ModelQualityEvaluator:
    def evaluate_quality(
        self, model_id: str, total_runs: int, missing_outputs: int, abstentions: int
    ) -> ModelQualityVerdict:
        warnings = []
        missing_rate = missing_outputs / total_runs if total_runs > 0 else 0.0
        abstention_rate = abstentions / total_runs if total_runs > 0 else 0.0

        is_acceptable = True

        if missing_rate > 0.05:
            is_acceptable = False
            warnings.append(f"Missing output rate {missing_rate:.2f} is too high")

        if abstention_rate > 0.2:
            is_acceptable = False
            warnings.append(
                f"Abstention rate {abstention_rate:.2f} is unstable/too high"
            )

        return ModelQualityVerdict(
            verdict_id=str(uuid.uuid4()),
            model_id=model_id,
            missing_output_rate=missing_rate,
            abstention_rate=abstention_rate,
            is_acceptable=is_acceptable,
            warnings=warnings,
        )
