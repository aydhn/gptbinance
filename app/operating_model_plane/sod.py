from app.operating_model_plane.models import RoleRef, SegregationOfDutiesRecord
from app.operating_model_plane.exceptions import SegregationOfDutiesViolation

def evaluate_sod(proposer: RoleRef, approver: RoleRef) -> SegregationOfDutiesRecord:
    is_violated = (proposer.role_id == approver.role_id)
    record = SegregationOfDutiesRecord(
        record_id=f"sod_{proposer.role_id}_{approver.role_id}",
        proposer_role=proposer,
        approver_role=approver,
        is_violated=is_violated
    )
    if is_violated:
        raise SegregationOfDutiesViolation(f"Self-approval conflict detected for role {proposer.role_id}")
    return record
