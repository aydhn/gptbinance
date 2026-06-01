
def check_override_use_accountability(override_id: str, approver_ref: str = None, reviewer_ref: str = None):
    if not approver_ref or not reviewer_ref:
        return {"status": "caution", "message": "Immunity override asserted while accountable chain missing."}
    return {"status": "success", "override": override_id}
