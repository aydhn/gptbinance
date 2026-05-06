from typing import List, Optional
from uuid import UUID
from datetime import datetime, timezone

from app.identity.models import ElevationRequest, ElevationGrant
from app.identity.enums import ElevationClass
from app.identity.storage import identity_storage


class ElevationManager:
    def request_elevation(
        self,
        principal_id: UUID,
        reason: str,
        elevation_class: ElevationClass = ElevationClass.PURPOSE_BOUND,
    ) -> ElevationRequest:
        req = ElevationRequest(
            principal_id=principal_id,
            elevation_class=elevation_class,
            reason=reason,
            requested_at=datetime.now(timezone.utc),
        )
        # Store request (omitted here for brevity, assume passed to approver)
        return req

    def grant_elevation(
        self, request_id: UUID, approved_by: UUID, expires_at: datetime
    ) -> ElevationGrant:
        grant = ElevationGrant(
            request_id=request_id,
            approved_by=approved_by,
            granted_at=datetime.now(timezone.utc),
            expires_at=expires_at,
        )
        identity_storage.save_elevation(grant)
        return grant

    def list_all(self) -> List[ElevationGrant]:
        return identity_storage.get_all_elevations()


elevation_manager = ElevationManager()
