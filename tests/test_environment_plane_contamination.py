import pytest
from app.environment_plane.contamination import record_contamination
from app.environment_plane.enums import ContaminationClass

def test_record_contamination():
    contam = record_contamination(ContaminationClass.SHARED_STATE, "HIGH", "All tenants")
    assert contam.contamination_class == ContaminationClass.SHARED_STATE
    assert contam.severity == "HIGH"
    assert contam.blast_radius == "All tenants"
