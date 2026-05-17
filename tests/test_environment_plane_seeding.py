import pytest
from app.environment_plane.seeding import define_seed

def test_define_seed():
    seed = define_seed("Replay DB", "Stale by 2 days")
    assert seed.seed_provenance == "Replay DB"
    assert seed.stale_warnings == "Stale by 2 days"
