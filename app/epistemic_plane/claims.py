from typing import List

def check_epistemic_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases:
        cautions.append("assurance-sounding claim without claim/evidence/surveillance basis explicit caution")
    return cautions

def evaluate_accountability_claim_accountability(claim_id: str, has_subject_duty_basis: bool = False):
    if not has_subject_duty_basis:
        return {'status': 'caution', 'message': 'Accountability-sounding claim without subject/duty/breach basis.'}
    return {'status': 'success'}


# Incentive Plane Integration
class EpistemicClaimsIncentiveIntegration:
    incentive_plane_evidence_refs: list = []

def incentive_sounding_claim_without_basis():
    return {"caution": "incentive-sounding claim without subject/target/formula/gaming basis"}
