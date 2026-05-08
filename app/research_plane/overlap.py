from app.research_plane.models import ResearchItem, ResearchOverlapReport
from app.research_plane.enums import OverlapSeverity
from typing import List


class OverlapDetector:
    def detect_overlap(
        self, primary_item: ResearchItem, all_items: List[ResearchItem]
    ) -> ResearchOverlapReport:
        overlapping_refs = []
        severity = OverlapSeverity.LOW

        if primary_item.question:
            for item in all_items:
                if item.research_id != primary_item.research_id and item.question:
                    if (
                        primary_item.question.text.lower().strip()
                        == item.question.text.lower().strip()
                    ):
                        overlapping_refs.append(item.research_id)
                        severity = OverlapSeverity.CRITICAL

        # Further logic for hypothesis mechanism overlap could be added here

        description = "No overlap detected."
        if overlapping_refs:
            description = f"Overlap detected with {len(overlapping_refs)} items."

        return ResearchOverlapReport(
            report_id=f"ov_{primary_item.research_id}",
            primary_hypothesis_ref=(
                primary_item.hypotheses[0].hypothesis_id
                if primary_item.hypotheses
                else "unknown"
            ),
            overlapping_hypothesis_refs=overlapping_refs,
            severity=severity,
            description=description,
        )
