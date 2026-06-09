
def check_adjudication_proof_sufficiency(cannibalization_id: str, adjudication_id: str) -> dict:
    if not adjudication_id:
        return {"safe": False, "caution": "Explicit caution: cannibalization signal treated liability outcome without adjudication posture"}
    return {"safe": True, "cannibalization_id": cannibalization_id, "adjudication_id": adjudication_id}
