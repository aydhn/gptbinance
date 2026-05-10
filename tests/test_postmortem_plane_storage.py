import pytest
from app.postmortem_plane.storage import PostmortemStorage
from app.postmortem_plane.models import PostmortemDefinition, SourceIncidentBundle
from app.postmortem_plane.enums import PostmortemClass
from datetime import datetime

def test_storage():
    storage = PostmortemStorage()
    p = PostmortemDefinition(
        postmortem_id="PM-1",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    storage.save(p)
    loaded = storage.load("PM-1")
    assert loaded.postmortem_id == "PM-1"
    assert loaded.postmortem_class == PostmortemClass.INCIDENT_FULL_RCA
