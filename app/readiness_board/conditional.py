from datetime import datetime, timezone
from app.readiness_board.models import ConditionalGoTerms
from app.readiness_board.enums import ConditionalScope


class ConditionalGoManager:
    def is_terms_expired(self, terms: ConditionalGoTerms) -> bool:
        return datetime.now(timezone.utc) > terms.expires_at

    def validate_scope(
        self, terms: ConditionalGoTerms, requested_scope: ConditionalScope
    ) -> bool:
        return requested_scope in terms.scopes
