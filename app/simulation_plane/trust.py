from app.simulation_plane.models import SimulationTrustVerdict
from app.simulation_plane.enums import TrustVerdict
from app.simulation_plane.base import TrustEvaluatorBase
from typing import Dict


class TrustedVerdictEngine(TrustEvaluatorBase):
    def evaluate(
        self, run_id: str, factors: Dict[str, str] = None
    ) -> SimulationTrustVerdict:
        if factors is None:
            factors = {"data_truth": "ok", "assumptions": "explicit"}

        verdict = TrustVerdict.TRUSTED
        # Very simple rules for demonstration
        if "leakage" in str(factors).lower():
            verdict = TrustVerdict.BLOCKED
        elif "hidden_assumption" in str(factors).lower():
            verdict = TrustVerdict.CAUTION

        return SimulationTrustVerdict(
            run_id=run_id,
            verdict=verdict,
            factors=factors,
            caveats=[
                "Trust breakdown mandatory. Evaluated data truth, feature integrity, assumption transparency."
            ],
        )
