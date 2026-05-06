from typing import Any
from app.postmortems.models import CounterfactualAssessment
from typing import List


class CounterfactualAnalyzer:
    def analyze(
        self, root_causes: Any, contributors: Any
    ) -> List[CounterfactualAssessment]:
        assessments = []
        if root_causes:
            assessments.append(
                CounterfactualAssessment(
                    scenario="If root cause was mitigated",
                    assessment="likely_reduce_blast_radius",
                )
            )
        if not assessments:
            assessments.append(
                CounterfactualAssessment(
                    scenario="General analysis", assessment="insufficient_evidence"
                )
            )
        return assessments
