import pytest
from app.postmortem_plane.manifests import PostmortemManifestBuilder
from app.postmortem_plane.models import PostmortemDefinition, SourceIncidentBundle
from app.postmortem_plane.enums import PostmortemClass
from datetime import datetime

def test_manifest_builder():
    p = PostmortemDefinition(
        postmortem_id="PM-1",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    m = PostmortemManifestBuilder.build("M-1", p)
    assert m.postmortem_id == "PM-1"
    assert "definition" in m.hashes
