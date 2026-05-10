from app.policy_plane.models import PolicyDebtRecord


def record_waiver_debt(waiver_id: str, description: str) -> PolicyDebtRecord:
    return PolicyDebtRecord(
        source_type="waiver",
        source_id=waiver_id,
        severity="medium",
        description=description,
    )
