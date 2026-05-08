from typing import List
from app.performance_plane.models import CohortContribution
from app.performance_plane.enums import CohortClass


class ContributionAggregator:
    @staticmethod
    def rollup(
        contributions: List[CohortContribution], target_cohort_class: CohortClass
    ) -> dict:
        summary = {}
        for c in contributions:
            if c.cohort_class == target_cohort_class:
                if c.cohort_id not in summary:
                    summary[c.cohort_id] = 0.0
                summary[c.cohort_id] += float(c.contribution_value)

        return summary
