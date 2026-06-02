from typing import List

def check_finality_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        cautions.append("final label under stale or degraded assurance explicit caution")
    return cautions

def assert_final_safe_accountability(case_id: str, accountability_restitution_resolved: bool):
    """
    Checks if a final closure is safe under the Accountability Plane (Phase 135).
    """
    if not accountability_restitution_resolved:
        return {"status": "caution", "message": "Final label requested under open accountability/restitution gap."}
    return {"status": "finalized"}
