from typing import Dict, List, Optional
from uuid import UUID
from app.identity.models import (
    PrincipalRecord,
    RoleBinding,
    CapabilityGrant,
    TrustZoneBinding,
    SessionRecord,
    DelegationRecord,
    ElevationGrant,
    BreakGlassRecord,
    AuthorizationProof,
    IdentityAuditRecord,
)


class InMemoryIdentityStorage:
    def __init__(self):
        self.principals: Dict[UUID, PrincipalRecord] = {}
        self.role_bindings: Dict[UUID, List[RoleBinding]] = {}
        self.capability_grants: Dict[UUID, List[CapabilityGrant]] = {}
        self.trust_zone_bindings: Dict[UUID, List[TrustZoneBinding]] = {}
        self.sessions: Dict[UUID, SessionRecord] = {}
        self.delegations: Dict[UUID, DelegationRecord] = {}
        self.elevations: Dict[UUID, ElevationGrant] = {}
        self.breakglass_records: Dict[UUID, BreakGlassRecord] = {}
        self.proofs: Dict[UUID, AuthorizationProof] = {}
        self.audit_records: List[IdentityAuditRecord] = []

    def save_principal(self, principal: PrincipalRecord) -> None:
        self.principals[principal.id] = principal

    def get_principal(self, principal_id: UUID) -> Optional[PrincipalRecord]:
        return self.principals.get(principal_id)

    def save_role_binding(self, binding: RoleBinding) -> None:
        if binding.principal_id not in self.role_bindings:
            self.role_bindings[binding.principal_id] = []
        self.role_bindings[binding.principal_id].append(binding)

    def save_capability_grant(self, grant: CapabilityGrant) -> None:
        if grant.principal_id not in self.capability_grants:
            self.capability_grants[grant.principal_id] = []
        self.capability_grants[grant.principal_id].append(grant)

    def get_capabilities(self, principal_id: UUID) -> List[CapabilityGrant]:
        return self.capability_grants.get(principal_id, [])

    def save_trust_zone_binding(self, binding: TrustZoneBinding) -> None:
        if binding.principal_id not in self.trust_zone_bindings:
            self.trust_zone_bindings[binding.principal_id] = []
        self.trust_zone_bindings[binding.principal_id].append(binding)

    def get_trust_zones(self, principal_id: UUID) -> List[TrustZoneBinding]:
        return self.trust_zone_bindings.get(principal_id, [])

    def save_session(self, session: SessionRecord) -> None:
        self.sessions[session.session_id] = session

    def get_session(self, session_id: UUID) -> Optional[SessionRecord]:
        return self.sessions.get(session_id)

    def save_delegation(self, delegation: DelegationRecord) -> None:
        self.delegations[delegation.delegation_id] = delegation

    def save_elevation(self, elevation: ElevationGrant) -> None:
        self.elevations[elevation.grant_id] = elevation

    def save_breakglass(self, record: BreakGlassRecord) -> None:
        self.breakglass_records[record.record_id] = record

    def save_proof(self, proof: AuthorizationProof) -> None:
        self.proofs[proof.proof_id] = proof

    def save_audit(self, record: IdentityAuditRecord) -> None:
        self.audit_records.append(record)

    def get_all_principals(self) -> List[PrincipalRecord]:
        return list(self.principals.values())

    def get_all_sessions(self) -> List[SessionRecord]:
        return list(self.sessions.values())

    def get_all_delegations(self) -> List[DelegationRecord]:
        return list(self.delegations.values())

    def get_all_elevations(self) -> List[ElevationGrant]:
        return list(self.elevations.values())

    def get_all_breakglass(self) -> List[BreakGlassRecord]:
        return list(self.breakglass_records.values())


identity_storage = InMemoryIdentityStorage()
