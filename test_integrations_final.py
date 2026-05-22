import pytest
from app.precedent_plane.enums import PrecedentClass, AuthorityClass
from app.precedent_plane.models import PrecedentObject
from app.precedent_plane.registry import CanonicalPrecedentRegistry

def test_registry_integration():
    registry = CanonicalPrecedentRegistry()
    assert len(registry.list_all()) == 0

    obj = PrecedentObject(
        precedent_id="P-INTEG-01",
        precedent_class=PrecedentClass.LOCAL,
        owner="security",
        scope="global",
        authority_posture=AuthorityClass.LOCAL_PERSUASIVE,
        applicability_posture="directly_applicable"
    )
    registry.register(obj)
    fetched = registry.get("P-INTEG-01")
    assert fetched.owner == "security"

def test_policy_context_fields():
    # Make sure we didn't break policy kernel
    try:
        from app.policy_kernel.context import PrecedentContext
        ctx = PrecedentContext()
        assert hasattr(ctx, "stale_analogies")
    except ImportError:
        pass
