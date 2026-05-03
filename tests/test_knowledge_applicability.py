import pytest
from datetime import datetime, timezone
from app.knowledge.models import Runbook, KnowledgeOwner, ApplicabilityRule
from app.knowledge.enums import DocumentStatus, ApplicabilityVerdict
from app.knowledge.applicability import RunbookApplicabilityEngine


def test_applicability():
    engine = RunbookApplicabilityEngine()
    rb = Runbook(
        item_id="RB-001",
        title="Test RB",
        description="Desc",
        owner=KnowledgeOwner(owner_id="u1", team="ops"),
        status=DocumentStatus.PUBLISHED,
        last_reviewed_at=datetime.now(timezone.utc),
        applicability_rules=[
            ApplicabilityRule(
                rule_id="R1", description="Live only", target_profiles=["live"]
            )
        ],
    )

    assert engine.evaluate(rb, {"profile": "live"}) == ApplicabilityVerdict.APPLICABLE
    assert engine.evaluate(rb, {"profile": "paper"}) == ApplicabilityVerdict.CAUTION

    rb.status = DocumentStatus.DEPRECATED
    assert engine.evaluate(rb, {"profile": "live"}) == ApplicabilityVerdict.BLOCKED
