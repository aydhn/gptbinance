import uuid
from typing import Dict, Any, List
from datetime import datetime, timezone
from app.model_plane.models import InferenceEquivalenceReport
from app.model_plane.enums import EquivalenceVerdict


class InferenceEquivalenceEvaluator:
    def compare(
        self,
        model_id: str,
        offline_outputs: Dict[str, Any],
        runtime_outputs: Dict[str, Any],
    ) -> InferenceEquivalenceReport:
        differences = []

        for k, v_offline in offline_outputs.items():
            if k not in runtime_outputs:
                differences.append(f"Output {k} missing in runtime")
                continue

            v_runtime = runtime_outputs[k]
            if v_offline != v_runtime:
                differences.append(
                    f"Mismatch on {k}: offline={v_offline}, runtime={v_runtime}"
                )

        for k in runtime_outputs.keys():
            if k not in offline_outputs:
                differences.append(f"Output {k} missing in offline")

        verdict = EquivalenceVerdict.EQUIVALENT
        if differences:
            verdict = EquivalenceVerdict.MAJOR_DIVERGENCE

        return InferenceEquivalenceReport(
            report_id=str(uuid.uuid4()),
            model_id=model_id,
            evaluated_at=datetime.now(timezone.utc),
            verdict=verdict,
            differences=differences,
            proof_notes=f"Compared {len(offline_outputs)} outputs",
        )
