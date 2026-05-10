import pytest
from app.postmortem_plane.reopen import PostmortemReopener
from app.postmortem_plane.models import PostmortemDefinition, PostmortemClosureRecord, SourceIncidentBundle
from app.postmortem_plane.enums import ClosureClass, PostmortemClass
from datetime import datetime

def test_reopen():
    p = PostmortemDefinition(
        postmortem_id="PM-1",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        closure_record=PostmortemClosureRecord(closure_status=ClosureClass.CLOSED, closure_rationale="done"),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    PostmortemReopener.reopen(p, "Recurrence detected")
    assert p.closure_record.closure_status == ClosureClass.BLOCKED_EVIDENCE
    assert "Reopened: Recurrence detected" in p.closure_record.unresolved_blockers
