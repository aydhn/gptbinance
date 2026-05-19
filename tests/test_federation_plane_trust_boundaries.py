import pytest
from app.federation_plane.models import TrustBoundaryRecord
from app.federation_plane.enums import TrustBoundaryClass
from app.federation_plane.trust_boundaries import TrustBoundaryManager
from app.federation_plane.exceptions import InvalidBoundaryDefinition


def test_trust_boundary_manager_register():
    manager = TrustBoundaryManager()
    record = TrustBoundaryRecord(
        boundary_id="bnd-001",
        boundary_class=TrustBoundaryClass.PARTNER,
        crossing_notes="Strict partner crossing",
    )
    manager.register(record)
    assert manager.get_boundary("bnd-001") == record


def test_trust_boundary_manager_invalid_id():
    manager = TrustBoundaryManager()
    record = TrustBoundaryRecord(
        boundary_id="", boundary_class=TrustBoundaryClass.PARTNER, crossing_notes=""
    )
    with pytest.raises(InvalidBoundaryDefinition):
        manager.register(record)
