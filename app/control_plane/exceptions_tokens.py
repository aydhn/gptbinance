import uuid
from typing import Dict, Optional
from app.control_plane.models import ExceptionToken
from app.control_plane.enums import ExceptionClass
from datetime import datetime, timezone


class ExceptionTokenManager:
    def __init__(self):
        self._tokens: Dict[str, ExceptionToken] = {}

    def issue_token(
        self, action_id: str, scope_ref: str, rationale: str, ttl_seconds: int = 3600
    ) -> ExceptionToken:
        token = ExceptionToken(
            token_id=f"TOK-{uuid.uuid4().hex[:8]}",
            action_id=action_id,
            exception_class=ExceptionClass.SINGLE_USE,
            scope_ref=scope_ref,
            ttl_seconds=ttl_seconds,
            rationale=rationale,
        )
        self._tokens[token.token_id] = token
        return token

    def get_token(self, token_id: str) -> Optional[ExceptionToken]:
        return self._tokens.get(token_id)

    def revoke_token(self, token_id: str):
        if token_id in self._tokens:
            self._tokens[token_id].is_revoked = True

    def validate_token(self, token_id: str) -> bool:
        token = self.get_token(token_id)
        if not token or token.is_revoked:
            return False
        age = (datetime.now(timezone.utc) - token.issued_at).total_seconds()
        return age <= token.ttl_seconds
