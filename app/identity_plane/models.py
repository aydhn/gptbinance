from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Set
from datetime import datetime, timezone
from app.identity_plane.enums import (
    PrincipalClass, LifecycleState, CapabilityRiskClass, SessionClass,
    DelegationClass, ImpersonationClass, ElevationClass, RevocationClass,
    EquivalenceVerdict, TrustVerdict
)

class IdentityPlaneConfig(BaseModel):
    strict_mode: bool = True

class PrincipalDefinition(BaseModel):
    principal_id: str
    principal_class: PrincipalClass
    owner_id: Optional[str] = None
    state: LifecycleState = LifecycleState.ACTIVE
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CapabilityDefinition(BaseModel):
    capability_id: str
    risk_class: CapabilityRiskClass
    description: str

class RoleDefinition(BaseModel):
    role_id: str
    capabilities: List[str]

class ScopeGrant(BaseModel):
    environment: str
    resource_pattern: str

class GrantRecord(BaseModel):
    grant_id: str
    principal_id: str
    role_or_capability_id: str
    is_role: bool
    scopes: List[ScopeGrant]
    expires_at: Optional[datetime] = None

class SessionProvenance(BaseModel):
    originating_principal_id: str
    auth_method: str
    trigger_chain: List[str]

class AuthSession(BaseModel):
    session_id: str
    principal_id: str
    session_class: SessionClass
    provenance: SessionProvenance
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime
    is_active: bool = True

class DelegationRecord(BaseModel):
    delegation_id: str
    delegator_id: str
    delegatee_id: str
    delegation_class: DelegationClass
    expires_at: datetime

class ImpersonationRecord(BaseModel):
    record_id: str
    session_id: str
    target_principal_id: str
    impersonation_class: ImpersonationClass
    approved_by: str
    justification: str
    expires_at: datetime

class ElevationRecord(BaseModel):
    record_id: str
    session_id: str
    elevation_class: ElevationClass
    granted_capabilities: List[str]
    approved_by: str
    justification: str
    expires_at: datetime

class RevocationRecord(BaseModel):
    revocation_id: str
    principal_id: str
    revocation_class: RevocationClass
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SuspensionRecord(BaseModel):
    suspension_id: str
    principal_id: str
    justification: str
    reactivation_prerequisites: List[str]

class AuthzEvaluationRecord(BaseModel):
    session_id: str
    capability: str
    environment: str
    is_allowed: bool
    deny_reasons: List[str]

class IdentityTrustVerdictDetails(BaseModel):
    principal_id: str
    verdict: TrustVerdict
    blockers: List[str]
    caveats: List[str]
