from uuid import UUID
from datetime import datetime, timezone
from typing import List, Optional

from app.identity.enums import SessionClass, ScopeClaimClass
from app.identity.models import SessionRecord, SessionClaim
from app.identity.storage import identity_storage
from app.identity.base import SessionValidatorBase


class SessionManager(SessionValidatorBase):
    def issue_session(
        self,
        principal_id: UUID,
        session_class: SessionClass,
        expires_at: datetime,
        claims: List[SessionClaim] = None,
    ) -> SessionRecord:
        # In a real system, you'd check if they are allowed this session type
        session = SessionRecord(
            principal_id=principal_id,
            session_class=session_class,
            issued_at=datetime.now(timezone.utc),
            expires_at=expires_at,
            claims=claims or [],
        )
        identity_storage.save_session(session)
        return session

    def validate_session(self, session_id: UUID) -> bool:
        session = identity_storage.get_session(session_id)
        if not session:
            return False

        now = datetime.now(timezone.utc)
        if now > session.expires_at:
            return False

        return True

    def list_all(self) -> List[SessionRecord]:
        return identity_storage.get_all_sessions()


session_manager = SessionManager()
