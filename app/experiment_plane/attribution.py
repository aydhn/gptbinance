# Comparative Attribution
from app.experiment_plane.models import ComparativeAttributionReport


def generate_attribution(experiment_id: str) -> ComparativeAttributionReport:
    return ComparativeAttributionReport(
        report_id=f"attr_{experiment_id}",
        signal_quality_diff=0.0,
        allocation_diff=0.0,
        execution_diff=0.0,
        risk_block_diff=0.0,
        fee_funding_carry_diff=0.0,
        residual_diff=0.0,
        proof_notes="Placeholder attribution",
    )
