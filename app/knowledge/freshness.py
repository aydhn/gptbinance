from datetime import datetime, timezone
from typing import Dict, Any, List
from app.knowledge.models import KnowledgeItem, FreshnessReport, StalenessWarning
from app.knowledge.enums import FreshnessSeverity
from app.knowledge.catalog import catalog_registry


class FreshnessEngine:
    def __init__(self, review_cadence_days: int = 90):
        self.review_cadence_days = review_cadence_days

    def evaluate(
        self, item: KnowledgeItem, context: Dict[str, Any] = None
    ) -> FreshnessReport:
        now = datetime.now(timezone.utc)
        days_since_review = (now - item.last_reviewed_at).days
        warnings: List[StalenessWarning] = []
        severity = FreshnessSeverity.HEALTHY

        if days_since_review > self.review_cadence_days:
            severity = FreshnessSeverity.STALE
            warnings.append(
                StalenessWarning(
                    reason=f"Item has not been reviewed in {days_since_review} days (cadence: {self.review_cadence_days})."
                )
            )

        # We could also check context for linked component changes etc.
        if context and context.get("linked_component_changed"):
            severity = FreshnessSeverity.WARNING
            warnings.append(
                StalenessWarning(
                    reason="Linked component schema/version has changed since last review."
                )
            )

        return FreshnessReport(
            item_id=item.item_id,
            severity=severity,
            warnings=warnings,
            last_reviewed_at=item.last_reviewed_at,
            days_since_review=days_since_review,
        )

    def evaluate_all(self) -> List[FreshnessReport]:
        reports = []
        for item in catalog_registry.list_all():
            reports.append(self.evaluate(item))
        return reports


freshness_engine = FreshnessEngine()
