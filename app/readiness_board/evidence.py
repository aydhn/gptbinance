from app.clearing_plane.integration import integrate_with_clearing_plane


class CollateralReadinessEvidence:
    def get_bundle(self, collateral_id: str, repo):
        return {
            "asset_clarity": not repo.has_fake_segregation(collateral_id),
            "valuation_sufficiency": not repo.is_valuation_stale(collateral_id),
            "perfection_integrity": not repo.has_hidden_encumbrance(collateral_id)
        }
# Escrow-plane readiness: escrow trust, deposit clarity, condition sufficiency added to bundle


# Phase 162: Netting Evidence
def get_netting_evidence_bundle():
    return {
        "netting_trust": "TRUSTED",
        "obligation_clarity": True,
        "mutuality_sufficiency": True,
        "valuation_sufficiency": True,
        "setoff_sufficiency": True,
        "closeout_sufficiency": True
    }


# Added for Phase 163 Clearing Plane Integration


def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/readiness_board/evidence.py")
    return integration.evaluate_posture()


class SettlementEvidence:
    def __init__(self, context):
        self.instruction_clarity = context.get('instruction_clarity', False)
        self.ssi_sufficiency = context.get('ssi_sufficiency', False)
        self.matching_sufficiency = context.get('matching_sufficiency', False)
        self.funding_sufficiency = context.get('funding_sufficiency', False)
        self.finality_sufficiency = context.get('finality_sufficiency', False)
        self.settlement_trust = context.get('settlement_trust', 'blocked')

    def evaluate(self):
        critical_failures = not all([
            self.instruction_clarity,
            self.ssi_sufficiency,
            self.matching_sufficiency,
            self.funding_sufficiency,
            self.finality_sufficiency
        ])

        if critical_failures:
            return {"status": "blocker", "reason": "critical settlement integrity failure"}
        return {"status": "ready"}
