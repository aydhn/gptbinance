import uuid
from typing import List
from datetime import datetime, timezone
from app.model_plane.models import ServingSkewReport
from app.model_plane.exceptions import ServingEquivalenceError


class ServingSkewEvaluator:
    def evaluate_skew(
        self,
        model_id: str,
        training_schema: str,
        serving_schema: str,
        threshold_diff: bool = False,
    ) -> ServingSkewReport:
        suspected_causes = []

        if training_schema != serving_schema:
            suspected_causes.append("Schema mismatch between training and serving")

        if threshold_diff:
            suspected_causes.append("Threshold policy mismatch detected")

        skew_detected = len(suspected_causes) > 0

        return ServingSkewReport(
            report_id=str(uuid.uuid4()),
            model_id=model_id,
            evaluated_at=datetime.now(timezone.utc),
            skew_detected=skew_detected,
            suspected_causes=suspected_causes,
        )
