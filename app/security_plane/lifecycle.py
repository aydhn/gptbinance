from app.security_plane.credentials import CredentialStateManager
from app.security_plane.models import CredentialStateRecord
from app.security_plane.enums import CredentialState
from datetime import datetime, timezone
from app.security_plane.exceptions import InvalidCredentialLifecycleStateError

class LifecycleManager:
    def __init__(self, state_manager: CredentialStateManager):
        self.state_manager = state_manager

    def transition_state(self, credential_id: str, new_state: CredentialState, notes: str = "") -> None:
        current = self.state_manager.get_state(credential_id)
        if current:
            # Enforce valid transitions here if needed
            if current.state == CredentialState.REVOKED and new_state == CredentialState.ACTIVE:
                 raise InvalidCredentialLifecycleStateError("Cannot activate a revoked credential")

        record = CredentialStateRecord(
            credential_id=credential_id,
            state=new_state,
            updated_at=datetime.now(timezone.utc),
            proof_notes=notes
        )
        self.state_manager.update_state(record)
