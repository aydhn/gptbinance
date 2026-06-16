from typing import List
from datetime import datetime
from app.collateral_plane.models import CollateralTrustVerdict
from app.collateral_plane.enums import TrustVerdictType

class TrustedCollateralVerdictEngine:
    def __init__(self, repository):
        self.repository = repository

    def evaluate(self, collateral_id: str) -> CollateralTrustVerdict:
        cautions = []
        # Mocking integrity checks for the verdict
        asset_clarity = True
        eligibility_sufficiency = True
        valuation_sufficiency = True
        perfection_integrity = True
        liquidation_sufficiency = True

        # Check for hidden liens
        if self.repository.has_hidden_encumbrance(collateral_id):
            perfection_integrity = False
            cautions.append("Hidden lien detected. Collateral perfection is compromised.")

        # Check stale valuation
        if self.repository.is_valuation_stale(collateral_id):
            valuation_sufficiency = False
            cautions.append("Stale valuation detected. Haircuts and advance rates cannot be trusted.")

        if self.repository.has_fake_segregation(collateral_id):
            asset_clarity = False
            cautions.append("Fake segregation detected. Rehypothecation risk present.")

        verdict = TrustVerdictType.TRUSTED
        if not perfection_integrity or not valuation_sufficiency:
            verdict = TrustVerdictType.DEGRADED
        if cautions:
            verdict = TrustVerdictType.REVIEW_REQUIRED

        return CollateralTrustVerdict(
            collateral_id=collateral_id,
            verdict=verdict,
            asset_clarity=asset_clarity,
            eligibility_sufficiency=eligibility_sufficiency,
            valuation_sufficiency=valuation_sufficiency,
            perfection_integrity=perfection_integrity,
            liquidation_sufficiency=liquidation_sufficiency,
            cautions=cautions,
            timestamp=datetime.utcnow()
        )
