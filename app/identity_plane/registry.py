from typing import Dict, List, Optional
from app.identity_plane.models import PrincipalDefinition, RoleDefinition, CapabilityDefinition, GrantRecord
from app.identity_plane.enums import PrincipalClass
from app.identity_plane.exceptions import InvalidPrincipalDefinition

class CanonicalPrincipalRegistry:
    def __init__(self):
        self.principals: Dict[str, PrincipalDefinition] = {}
        self.roles: Dict[str, RoleDefinition] = {}
        self.capabilities: Dict[str, CapabilityDefinition] = {}
        self.grants: List[GrantRecord] = []

    def register_principal(self, principal: PrincipalDefinition):
        if principal.principal_class == PrincipalClass.SERVICE_RUNTIME and not principal.owner_id:
            raise InvalidPrincipalDefinition("Service accounts must have an owner_id")
        self.principals[principal.principal_id] = principal

    def register_capability(self, cap: CapabilityDefinition):
        self.capabilities[cap.capability_id] = cap

    def register_role(self, role: RoleDefinition):
        self.roles[role.role_id] = role

    def add_grant(self, grant: GrantRecord):
        if grant.principal_id not in self.principals:
            raise ValueError("Unknown principal")
        self.grants.append(grant)

    def get_principal_capabilities(self, principal_id: str, environment: str) -> List[str]:
        caps = set()
        for grant in self.grants:
            if grant.principal_id == principal_id:
                env_match = any(scope.environment in ["*", environment] for scope in grant.scopes)
                if not env_match:
                    continue
                if grant.is_role:
                    role = self.roles.get(grant.role_or_capability_id)
                    if role:
                        caps.update(role.capabilities)
                else:
                    caps.add(grant.role_or_capability_id)
        return list(caps)
