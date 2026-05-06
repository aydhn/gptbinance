from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from uuid import UUID, uuid4

from app.identity.enums import (
    PrincipalType,
    PrincipalStatus,
    RoleClass,
    CapabilityClass,
    TrustZone,
    SessionClass,
    DelegationClass,
    ElevationClass,
    BreakglassClass,
    AuthorizationVerdict,
    ScopeClaimClass,
)


class IdentityPlaneConfig(BaseModel):
    strict_mode: bool = True


class PrincipalRef(BaseModel):
    principal_id: UUID


class PrincipalRecord(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    principal_type: PrincipalType
    status: PrincipalStatus = PrincipalStatus.ACTIVE
    metadata: Dict[str, Any] = Field(default_factory=dict)


class PrincipalProfile(BaseModel):
    principal_id: UUID
    department: Optional[str] = None


class PrincipalScope(BaseModel):
    allowed_workspaces: List[str] = Field(default_factory=list)


class RoleBinding(BaseModel):
    principal_id: UUID
    role: RoleClass


class CapabilityGrant(BaseModel):
    principal_id: UUID
    capability: CapabilityClass
    granted_at: datetime
    granted_by: Optional[UUID] = None


class TrustZoneBinding(BaseModel):
    principal_id: UUID
    zone: TrustZone


class SessionClaim(BaseModel):
    claim_type: ScopeClaimClass
    claim_value: str


class SessionRecord(BaseModel):
    session_id: UUID = Field(default_factory=uuid4)
    principal_id: UUID
    session_class: SessionClass
    issued_at: datetime
    expires_at: datetime
    claims: List[SessionClaim] = Field(default_factory=list)


class DelegationRecord(BaseModel):
    delegation_id: UUID = Field(default_factory=uuid4)
    delegator_id: UUID
    delegatee_id: UUID
    delegation_class: DelegationClass
    capabilities: List[CapabilityClass]
    granted_at: datetime
    expires_at: datetime


class ElevationRequest(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    principal_id: UUID
    elevation_class: ElevationClass
    reason: str
    requested_at: datetime


class ElevationGrant(BaseModel):
    grant_id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    approved_by: UUID
    granted_at: datetime
    expires_at: datetime


class BreakGlassRecord(BaseModel):
    record_id: UUID = Field(default_factory=uuid4)
    principal_id: UUID
    breakglass_class: BreakglassClass
    reason: str
    activated_at: datetime
    reviewed_at: Optional[datetime] = None


class AuthorizationRequest(BaseModel):
    principal_id: UUID
    action: str
    required_capabilities: List[CapabilityClass]
    target_zone: TrustZone
    target_scope: Optional[Dict[str, str]] = None


class AuthorizationProof(BaseModel):
    proof_id: UUID = Field(default_factory=uuid4)
    request: AuthorizationRequest
    verdict: AuthorizationVerdict
    denial_reasons: List[str] = Field(default_factory=list)
    generated_at: datetime


class AuthorizationDecision(BaseModel):
    verdict: AuthorizationVerdict
    reasons: List[str]


class IdentityAuditRecord(BaseModel):
    record_id: UUID = Field(default_factory=uuid4)
    timestamp: datetime
    event_type: str
    principal_id: Optional[UUID] = None
    details: Dict[str, Any]


class IdentityArtifactManifest(BaseModel):
    manifest_id: UUID = Field(default_factory=uuid4)
    proof_id: UUID
    generated_at: datetime
