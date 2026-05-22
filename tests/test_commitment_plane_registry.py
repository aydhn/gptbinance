import pytest
from app.commitment_plane.registry import CanonicalCommitmentRegistry
from app.commitment_plane.models import CommitmentObject, BindingStrengthRecord, OwnerRecord, AccountabilityRecord
from app.commitment_plane.enums import CommitmentClass, BindingClass, OwnerClass

def test_registry_registration():
    registry = CanonicalCommitmentRegistry()
    commitment = CommitmentObject(
        commitment_id="COM-001",
        commitment_class=CommitmentClass.PROMISE,
        scope="Global",
        description="Test promise",
        binding=BindingStrengthRecord(binding_class=BindingClass.COMMITTED),
        owners=[OwnerRecord(owner_id="user1", owner_class=OwnerClass.ACCOUNTABLE)],
        accountability=AccountabilityRecord(accountable_actor="user1")
    )
    registry.register_commitment(commitment)
    retrieved = registry.get_commitment("COM-001")
    assert retrieved is not None
    assert retrieved.commitment_id == "COM-001"
