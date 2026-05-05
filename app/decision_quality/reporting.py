from typing import List
from datetime import datetime, timezone
import uuid
from .models import (
    DecisionQualitySummary,
    OpportunityQualityReport,
    OpportunityOutcome,
    DecisionFrictionRecord,
    BlockReasonRecord,
)
from .attribution import FrictionAttributor


class DecisionQualityReporter:
    """
    Generates structured reports for decision quality.
    """

    def __init__(self):
        self.attributor = FrictionAttributor()

    def generate_summary(
        self,
        total_opportunities: int,
        executed_count: int,
        blocked_count: int,
        skipped_count: int,
        suppressed_count: int,
        block_reasons: List[BlockReasonRecord],
        frictions: List[DecisionFrictionRecord],
    ) -> DecisionQualitySummary:
        """
        Creates a high-level decision quality summary.
        """
        top_blocks = {}
        for br in block_reasons:
            val = br.reason_class.value
            top_blocks[val] = top_blocks.get(val, 0) + 1

        top_frictions = self.attributor.aggregate_friction(frictions)

        return DecisionQualitySummary(
            timestamp=datetime.now(timezone.utc),
            total_opportunities=total_opportunities,
            executed_count=executed_count,
            blocked_count=blocked_count,
            skipped_count=skipped_count,
            suppressed_count=suppressed_count,
            top_block_reasons=top_blocks,
            top_frictions=top_frictions,
            findings=[],  # In a real implementation, findings would be generated here
        )

    def generate_report(
        self, summary: DecisionQualitySummary, outcomes: List[OpportunityOutcome]
    ) -> OpportunityQualityReport:
        """
        Generates a full opportunity quality report.
        """
        return OpportunityQualityReport(
            report_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            opportunities=outcomes,
            summary=summary,
        )
