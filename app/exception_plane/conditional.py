from typing import List, Tuple
from app.collateral_plane.repository import CollateralRepository

class ConditionalExceptionEligibilityIntegrator:
    def __init__(self, repo: CollateralRepository):
        self.repo = repo

    def evaluate_posture(self, collateral_id: str) -> Tuple[bool, List[str]]:
        cautions = []
        is_secured = True

        if not collateral_id:
            cautions.append("conditional posture treated eligible collateral without collateral posture explicit caution")
            return False, cautions

        # Evaluate base defects preventing this plane from trusting collateral
        if self.repo.has_hidden_encumbrance(collateral_id):
            cautions.append(f"Hidden encumbrance invalidates exception_plane assumptions.")
            is_secured = False

        if self.repo.is_valuation_stale(collateral_id):
            cautions.append(f"Stale valuation renders exception_plane support illusory.")
            is_secured = False

        if self.repo.has_fake_segregation(collateral_id):
            cautions.append(f"Fake segregation compromises exception_plane recovery.")
            is_secured = False

        if not is_secured:
            cautions.append("conditional posture treated eligible collateral without collateral posture explicit caution")

        return is_secured, cautions
