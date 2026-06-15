from app.indemnity_plane.models import ReimbursementRecord
def evaluate_reimbursement(indemnity_id: str, reimbursement_class: str) -> ReimbursementRecord:
    return ReimbursementRecord(indemnity_id=indemnity_id, reimbursement_class=reimbursement_class)
