import pytest
from app.postmortem_plane.equivalence import PostmortemEquivalenceEvaluator
from app.postmortem_plane.enums import EquivalenceVerdict
from app.postmortem_plane.models import PostmortemDefinition, SourceIncidentBundle
from app.postmortem_plane.enums import PostmortemClass
from datetime import datetime

def test_equivalence():
    p1 = PostmortemDefinition(
        postmortem_id="PM-1",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    p2 = p1.model_copy(deep=True)

    report = PostmortemEquivalenceEvaluator.evaluate("R-1", ["live", "paper"], p1, p2)
    assert report.verdict == EquivalenceVerdict.EQUIVALENT
