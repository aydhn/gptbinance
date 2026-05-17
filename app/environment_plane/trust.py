from app.environment_plane.models import EnvironmentTrustVerdict, EnvironmentObject
from app.environment_plane.enums import TrustVerdict
from app.environment_plane.base import TrustEvaluatorBase
from typing import Dict

class BasicTrustEvaluator(TrustEvaluatorBase):
    def evaluate(self, env: EnvironmentObject) -> EnvironmentTrustVerdict:
        breakdown: Dict[str, str] = {}
        verdict = TrustVerdict.TRUSTED

        if env.drifts:
            verdict = TrustVerdict.CAUTION
            breakdown["drifts"] = f"Found {len(env.drifts)} drift records"

        if env.contaminations:
            verdict = TrustVerdict.BLOCKED
            breakdown["contaminations"] = f"Found {len(env.contaminations)} contamination records"

        if env.rot_records:
            if verdict != TrustVerdict.BLOCKED:
                verdict = TrustVerdict.DEGRADED
            breakdown["rot"] = f"Found {len(env.rot_records)} rot records"

        if not breakdown:
            breakdown["status"] = "Clean environment posture"

        return EnvironmentTrustVerdict(verdict=verdict, breakdown=breakdown)
