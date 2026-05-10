import pytest
from datetime import datetime
from app.postmortem_plane.trust import TrustedPostmortemEngine
from app.postmortem_plane.models import PostmortemDefinition, SourceIncidentBundle, RecurrenceRecord, PreventiveAction
from app.postmortem_plane.enums import PostmortemClass, TrustVerdict, RecurrenceClass, RecurrenceEscalationClass

def test_trust_evaluation():
    p = PostmortemDefinition(
        postmortem_id="PM-1",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    engine = TrustedPostmortemEngine()
    verdict = engine.evaluate_trust(p)
    assert verdict.verdict == TrustVerdict.DEGRADED # Missing root causes

    p.recurrence_records = [RecurrenceRecord(recurrence_id="R-1", recurrence_class=RecurrenceClass.SAME_FAMILY, previous_incident_family="FAM-1", interval_days=5, escalation_class=RecurrenceEscalationClass.UNCHANGED, comparison_notes="")]
    verdict2 = engine.evaluate_trust(p)
    assert verdict2.verdict == TrustVerdict.BLOCKED # Recurrence without preventive actions
