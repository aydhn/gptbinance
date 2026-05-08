from app.simulation_plane.models import SimulationEquivalenceReport
from app.simulation_plane.enums import SimulationMode, EquivalenceVerdict


class EquivalenceEvaluator:
    def evaluate(
        self, run_id: str, target_mode: SimulationMode, divergence_sources: list[str]
    ) -> SimulationEquivalenceReport:
        if divergence_sources:
            verdict = EquivalenceVerdict.PARTIAL_EQUIVALENCE
        else:
            verdict = EquivalenceVerdict.EQUIVALENT

        return SimulationEquivalenceReport(
            run_id=run_id,
            compare_to_mode=target_mode,
            verdict=verdict,
            divergence_sources=divergence_sources,
            caveats=["Equivalence evaluation is subject to assumption alignment."],
        )
