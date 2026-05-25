from app.settlement_plane.models import BeneficiaryClosureRecord

def evaluate_beneficiary_closure(closure: BeneficiaryClosureRecord):
    if closure.closure_type == "erasure":
        return {"status": "caution", "closure_id": closure.id, "warning": "Beneficiary erasure detected"}
    return {"status": "valid", "closure_id": closure.id, "beneficiary_id": closure.beneficiary_id}
