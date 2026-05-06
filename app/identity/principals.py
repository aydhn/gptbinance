from typing import List, Optional
from uuid import UUID
from app.identity.models import PrincipalRecord
from app.identity.base import PrincipalResolverBase
from app.identity.storage import identity_storage


class PrincipalRegistry(PrincipalResolverBase):
    def register_principal(self, principal: PrincipalRecord) -> None:
        identity_storage.save_principal(principal)

    def resolve_principal(self, principal_id: UUID) -> Optional[PrincipalRecord]:
        return identity_storage.get_principal(principal_id)

    def list_all(self) -> List[PrincipalRecord]:
        return identity_storage.get_all_principals()


principal_registry = PrincipalRegistry()
