import pytest
from app.postmortem_plane.registry import CanonicalPostmortemRegistry
from app.postmortem_plane.models import PostmortemDefinition, SourceIncidentBundle
from app.postmortem_plane.enums import PostmortemClass
from datetime import datetime
from app.postmortem_plane.exceptions import InvalidPostmortemDefinitionError

def test_registry_registration():
    registry = CanonicalPostmortemRegistry()

    # Valid postmortem
    p = PostmortemDefinition(
        postmortem_id="PM-123",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=["INC-1"], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    pid = registry.register_postmortem(p)
    assert pid == "PM-123"
    assert registry.get_postmortem("PM-123") is not None

    # Missing incident should fail validation during creation conceptually, but we test registry logic
    invalid_p = PostmortemDefinition(
        postmortem_id="PM-456",
        postmortem_class=PostmortemClass.INCIDENT_FULL_RCA,
        source_incidents=SourceIncidentBundle(incident_ids=[], severity_carryover="HIGH", blast_radius="GLOBAL"),
        severity_class="HIGH",
        affected_scopes=["ALL"],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    with pytest.raises(InvalidPostmortemDefinitionError):
        registry.register_postmortem(invalid_p)
