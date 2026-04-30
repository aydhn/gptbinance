from app.governance.models import RollbackReference, CandidateBundle
from app.governance.enums import RollbackStatus

import logging

logger = logging.getLogger(__name__)


class RollbackManager:
    def prepare_rollback_ref(
        self, previous_bundle: CandidateBundle
    ) -> RollbackReference:
        if not previous_bundle:
            logger.warning("No previous bundle to create rollback reference")
            return None
        return RollbackReference(
            bundle_id=previous_bundle.bundle_id,
            status=RollbackStatus.READY,
            known_good_since=previous_bundle.created_at,
        )
