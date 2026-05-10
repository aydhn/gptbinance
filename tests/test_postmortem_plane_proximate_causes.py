import pytest
from app.postmortem_plane.proximate_causes import ProximateCauseHandler

def test_proximate_cause_creation():
    pc = ProximateCauseHandler.create_proximate_cause("PC-1", "DB connection pool exhausted", ["N-1"], [])
    assert pc.proximate_cause_id == "PC-1"
