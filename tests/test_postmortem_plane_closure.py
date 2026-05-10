import pytest
from datetime import datetime
from app.postmortem_plane.closure import PostmortemClosureGovernance
from app.postmortem_plane.models import PostmortemDefinition, SourceIncidentBundle, CorrectiveAction, ActionVerificationRecord
from app.postmortem_plane.enums import PostmortemClass, ActionClass, ClosureClass, VerificationClass

def test_closure_governance():
    unverified_action = CorrectiveAction(
        action_id="A-1",
        action_class=ActionClass.CORRECTIVE,
        description="Fix something",
        owner="user",
        due_date=datetime.now(),
        target_scope="system",
        verification_records=[]
    )

    p = PostmortemDefinition(
        postmortem_id="PM-1",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        corrective_actions=[unverified_action],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    readiness = PostmortemClosureGovernance.evaluate_readiness(p)
    assert readiness.closure_status == ClosureClass.BLOCKED_VERIFICATION
    assert "Action A-1 lacks verification" in readiness.unresolved_blockers

    verified_action = unverified_action.model_copy(deep=True)
    verified_action.verification_records = [
        ActionVerificationRecord(verification_id="V-1", verification_class=VerificationClass.IMPLEMENTED, proof_notes="merged")
    ]
    p.corrective_actions = [verified_action]

    readiness2 = PostmortemClosureGovernance.evaluate_readiness(p)
    assert readiness2.closure_status == ClosureClass.READY
