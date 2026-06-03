class CanonApproval:
    meta_governance_authority_ref: str = None

def approval_resilience_check(approval_id):
    return {"status": "caution", "message": "Resilience action by actor lacking reserve or degrade authority explicit caution"}

# Added for Phase 141 - Viability Plane
def check_viability_authority(): return 'explicit caution if action by actor lacking subsidy/burden authority'
