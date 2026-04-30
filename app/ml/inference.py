from app.ml.models import InferenceRequest, InferenceResult
from app.ml.enums import InferenceVerdict
import uuid


class InferenceEngine:
    def predict(self, request: InferenceRequest) -> InferenceResult:
        # check model active, drift, missing
        return InferenceResult(
            request_id=str(uuid.uuid4()),
            run_id=request.run_id,
            raw_score=0.75,
            calibrated_score=0.70,
            verdict=InferenceVerdict.PASS,
            caution_flags=[],
        )
