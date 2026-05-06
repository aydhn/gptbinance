from app.postmortems.seeds import IncidentSeedIntake
from app.postmortems.models import PostmortemSeedRef
from datetime import datetime, timezone


def test_incident_seed_generation():
    intake = IncidentSeedIntake()
    seed = PostmortemSeedRef(
        incident_id="INC-001",
        seed_timestamp=datetime.now(timezone.utc),
        affected_scopes=["live"],
    )
    assert intake.intake_seed(seed) is True
    assert len(intake.get_unresolved_seeds()) == 1
