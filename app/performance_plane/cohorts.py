from decimal import Decimal
from typing import List
from app.performance_plane.models import CohortContribution
from app.performance_plane.enums import CohortClass


class CohortAnalyzer:
    @staticmethod
    def create_contribution(
        cohort_class: CohortClass,
        cohort_id: str,
        value: Decimal,
        currency: str,
        caveats: List[str] = None,
    ) -> CohortContribution:
        return CohortContribution(
            cohort_class=cohort_class,
            cohort_id=cohort_id,
            contribution_value=value,
            currency=currency,
            caveats=caveats or [],
        )
