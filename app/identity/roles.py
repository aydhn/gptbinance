from typing import List, Dict, Optional
from uuid import UUID
from app.identity.enums import RoleClass
from app.identity.models import RoleBinding
from app.identity.storage import identity_storage


class RoleRegistry:
    def grant_role(self, principal_id: UUID, role: RoleClass) -> None:
        binding = RoleBinding(principal_id=principal_id, role=role)
        identity_storage.save_role_binding(binding)

    def get_roles(self, principal_id: UUID) -> List[RoleClass]:
        bindings = identity_storage.role_bindings.get(principal_id, [])
        return [b.role for b in bindings]

    def list_all_roles(self) -> List[RoleClass]:
        return list(RoleClass)


role_registry = RoleRegistry()
