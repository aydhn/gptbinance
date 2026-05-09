# Equivalence
from app.experiment_plane.models import ExperimentEquivalenceReport
from app.experiment_plane.enums import EquivalenceVerdict


def check_equivalence(experiment_id: str) -> ExperimentEquivalenceReport:
    return ExperimentEquivalenceReport(
        verdict=EquivalenceVerdict.EQUIVALENT,
        divergence_sources=[],
        proof_notes="Placeholder equivalence",
    )
