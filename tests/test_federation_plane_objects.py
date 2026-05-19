from app.federation_plane.models import FederationObject
from app.federation_plane.objects import FederationObjectManager


def test_federation_object_manager():
    manager = FederationObjectManager()
    obj = FederationObject(
        federation_id="obj-001",
        domain_id="dom-001",
        tenant_id="ten-001",
        object_class="test_class",
        owner="test_owner",
        authority_scope="local",
        trust_boundary="internal",
        portability_posture="none",
    )
    manager.register(obj)
    assert manager.get_object("obj-001") == obj
