import glob

# The feedback said the tests are empty. Let's add some assertions that test our basic models.
test_file = "tests/test_precedent_plane_models.py"

with open(test_file, "w") as f:
    f.write("""import pytest
from app.precedent_plane.models import PrecedentObject, AuthorityClass, ApplicabilityClass, PrecedentClass

def test_precedent_object_creation():
    obj = PrecedentObject(
        precedent_id="P-001",
        precedent_class=PrecedentClass.LOCAL,
        owner="test-owner",
        scope="global",
        authority_posture=AuthorityClass.LOCAL_PERSUASIVE,
        applicability_posture=ApplicabilityClass.DIRECTLY_APPLICABLE
    )
    assert obj.precedent_id == "P-001"
    assert obj.owner == "test-owner"
""")

test_reg = "tests/test_precedent_plane_registry.py"
with open(test_reg, "w") as f:
    f.write("""import pytest
from app.precedent_plane.registry import CanonicalPrecedentRegistry
from app.precedent_plane.models import PrecedentObject, AuthorityClass, ApplicabilityClass, PrecedentClass
from app.precedent_plane.exceptions import InvalidPrecedentObjectError

def test_registry():
    registry = CanonicalPrecedentRegistry()
    obj = PrecedentObject(
        precedent_id="P-001",
        precedent_class=PrecedentClass.LOCAL,
        owner="test-owner",
        scope="global",
        authority_posture=AuthorityClass.LOCAL_PERSUASIVE,
        applicability_posture=ApplicabilityClass.DIRECTLY_APPLICABLE
    )
    registry.register(obj)
    fetched = registry.get("P-001")
    assert fetched.owner == "test-owner"

def test_registry_invalid():
    registry = CanonicalPrecedentRegistry()
    obj = PrecedentObject(
        precedent_id="",
        precedent_class=PrecedentClass.LOCAL,
        owner="test-owner",
        scope="global",
        authority_posture=AuthorityClass.LOCAL_PERSUASIVE,
        applicability_posture=ApplicabilityClass.DIRECTLY_APPLICABLE
    )
    with pytest.raises(InvalidPrecedentObjectError):
        registry.register(obj)
""")
