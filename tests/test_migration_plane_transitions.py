import pytest
from app.migration_plane.models import TransitionContract
from app.migration_plane.enums import TransitionClass
from app.migration_plane.transitions import TransitionManager
from app.migration_plane.exceptions import InvalidTransitionContractError

def test_valid_transition():
    contract = TransitionContract(transition_class=TransitionClass.FORWARD_ONLY, is_destructive=False)
    assert TransitionManager.validate_contract(contract) is True

def test_destructive_transition_must_be_marked():
    contract = TransitionContract(transition_class=TransitionClass.DESTRUCTIVE_TRANSITION, is_destructive=False)
    with pytest.raises(InvalidTransitionContractError):
        TransitionManager.validate_contract(contract)

def test_reversible_cannot_be_destructive():
    contract = TransitionContract(transition_class=TransitionClass.REVERSIBLE, is_destructive=True)
    with pytest.raises(InvalidTransitionContractError):
        TransitionManager.validate_contract(contract)
