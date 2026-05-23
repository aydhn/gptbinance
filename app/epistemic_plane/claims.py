class ClaimsIntegration:
    def evaluate_claims(self):
        # “fixed”, “made whole”, “remediated”, “fully compensated” claimleri remedy-plane sufficiency refs gerektirsin
        pass


def verify_rights_claim_basis(claim_assertion: str, holder_id: str, rights_registry) -> str:
    if not rights_registry.has_basis(holder_id, claim_assertion):
        return "explicit caution: rights-sounding claim without holder/beneficiary evidence"
    return "trusted"
