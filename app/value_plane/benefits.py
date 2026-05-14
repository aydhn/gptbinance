from typing import Dict, List, Optional
from app.value_plane.models import BenefitHypothesis
from app.value_plane.exceptions import InvalidBenefitHypothesis

class BenefitRegistry:
    def __init__(self):
        self._benefits: Dict[str, BenefitHypothesis] = {}

    def register(self, benefit: BenefitHypothesis):
        if not benefit.description:
            raise InvalidBenefitHypothesis("Benefit must have a description")
        self._benefits[benefit.benefit_id] = benefit

    def get(self, benefit_id: str) -> Optional[BenefitHypothesis]:
        return self._benefits.get(benefit_id)

    def list_all(self) -> List[BenefitHypothesis]:
        return list(self._benefits.values())

benefit_registry = BenefitRegistry()
