from typing import List
from .models import OpportunityOutcome


class MissedOpportunityDiagnostics:
    """
    Analyzes missed (blocked or skipped) opportunities.
    """

    def summarize_missed(self, outcomes: List[OpportunityOutcome]) -> dict:
        """
        Generates a summary of missed opportunity classes.
        """
        summary = {
            "good_block_candidate": 0,
            "missed_alpha_candidate": 0,
            "blocked_and_likely_saved_loss": 0,
            "indeterminate": 0,
            "unsafe_to_judge": 0,
        }

        for outcome in outcomes:
            verdict_name = outcome.verdict.value
            if verdict_name in summary:
                summary[verdict_name] += 1

        return summary
