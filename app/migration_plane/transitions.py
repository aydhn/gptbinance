from app.migration_plane.models import TransitionContract
from app.migration_plane.enums import TransitionClass
from app.migration_plane.exceptions import InvalidTransitionContractError

class TransitionManager:
    @staticmethod
    def validate_contract(contract: TransitionContract) -> bool:
        if contract.transition_class == TransitionClass.DESTRUCTIVE_TRANSITION and not contract.is_destructive:
            raise InvalidTransitionContractError("Destructive transition must be marked as destructive")

        if contract.transition_class == TransitionClass.REVERSIBLE and contract.is_destructive:
            raise InvalidTransitionContractError("Reversible transition cannot be marked as destructive")

        return True
