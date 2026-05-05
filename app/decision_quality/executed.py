from typing import List
from .models import OpportunityOutcome


class ExecutedOpportunityDiagnostics:
    """
    Analyzes executed opportunities.
    """

    def summarize_executed(self, outcomes: List[OpportunityOutcome]) -> dict:
        """
        Generates a summary of executed opportunity classes.
        """
        summary = {
            "executed_well": 0,
            "executed_poorly": 0,
            "indeterminate": 0,
            "unsafe_to_judge": 0,
        }

        for outcome in outcomes:
            verdict_name = outcome.verdict.value
            if verdict_name in summary:
                summary[verdict_name] += 1

        return summary
