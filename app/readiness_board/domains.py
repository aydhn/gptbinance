class CollateralIntegrityDomain:
    def evaluate(self, evidence_bundle):
        if not evidence_bundle.get("perfection_integrity"):
            return "BLOCKER: Perfection compromised"
        return "READY"
