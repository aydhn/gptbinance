from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.security_plane.enums import (
    AssetClass, BoundaryClass, SecretClass, CredentialState,
    VulnerabilityClass, ExploitabilityClass, ExposureClass,
    HardeningClass, DetectionClass, ExceptionClass,
    EquivalenceVerdict, SecurityTrustVerdictEnum
)

class SecurityPlaneConfig(BaseModel):
    is_enabled: bool = True
    strict_boundary_enforcement: bool = True
    require_owners_for_assets: bool = True

class SecurityOwner(BaseModel):
    owner_id: str
    contact_email: Optional[str] = None
    team_name: Optional[str] = None

class SecurityAssetRef(BaseModel):
    asset_id: str

class SecurityAsset(BaseModel):
    asset_id: str
    asset_class: AssetClass
    owner: SecurityOwner
    environment: str
    description: str = ""
    trust_posture: str = "unknown"

class TrustBoundary(BaseModel):
    boundary_id: str
    boundary_class: BoundaryClass
    description: str
    crossing_metadata: Dict[str, Any] = Field(default_factory=dict)
    collapsed: bool = False

class SecretDefinition(BaseModel):
    secret_id: str
    secret_class: SecretClass
    owner_id: str
    scope: str
    environment: str
    ttl_seconds: Optional[int] = None
    usage_lineage_refs: List[str] = Field(default_factory=list)

class TokenDefinition(BaseModel):
    token_id: str
    token_type: str
    owner_id: str
    scope: str
    expires_at: Optional[datetime] = None
    misuse_indicators: List[str] = Field(default_factory=list)

class KeyDefinition(BaseModel):
    key_id: str
    key_type: str
    environment_binding: str
    created_at: datetime
    expected_rotation_days: int
    lineage_refs: List[str] = Field(default_factory=list)

class CertificateDefinition(BaseModel):
    cert_id: str
    subject: str
    issuer: str
    expires_at: datetime
    is_revoked: bool = False
    chain_trust_metadata: Dict[str, Any] = Field(default_factory=dict)

class CredentialStateRecord(BaseModel):
    credential_id: str
    state: CredentialState
    updated_at: datetime
    proof_notes: str = ""

class VulnerabilityRecord(BaseModel):
    vuln_id: str
    vuln_class: VulnerabilityClass
    source_refs: List[str] = Field(default_factory=list)
    severity: str
    affected_asset_ids: List[str] = Field(default_factory=list)
    patch_status: str
    exploit_prerequisites: str = ""

class ExploitabilityAssessment(BaseModel):
    assessment_id: str
    vuln_id: str
    exploitability_class: ExploitabilityClass
    is_authenticated: bool
    environment_conditions: str = ""
    compensating_control_effect: str = ""
    confidence: str = "medium"

class ExposureRecord(BaseModel):
    exposure_id: str
    exposure_class: ExposureClass
    asset_id: str
    blast_radius_hints: str = ""
    proof_notes: str = ""

class PatchRecord(BaseModel):
    patch_id: str
    vuln_id: str
    status: str
    incompatibility_caveats: str = ""
    latency_debt_days: int = 0

class RotationRecord(BaseModel):
    rotation_id: str
    target_id: str
    target_type: str
    rotated_at: datetime
    verification_notes: str = ""

class RevocationRecord(BaseModel):
    revocation_id: str
    target_id: str
    target_type: str
    revoked_at: datetime
    propagation_verified: bool = False
    linked_principal_ids: List[str] = Field(default_factory=list)

class HardeningControlRecord(BaseModel):
    control_id: str
    hardening_class: HardeningClass
    asset_id: str
    effectiveness_notes: str = ""

class SecurityDetectionRecord(BaseModel):
    detection_id: str
    detection_class: DetectionClass
    description: str
    coverage_notes: str = ""

class SecuritySignalRecord(BaseModel):
    signal_id: str
    signal_type: str
    confidence: str
    freshness: str
    details: Dict[str, Any] = Field(default_factory=dict)

class CompensatingSecurityControl(BaseModel):
    control_id: str
    description: str
    residual_risk_estimation: str

class SecurityExceptionRecord(BaseModel):
    exception_id: str
    exception_class: ExceptionClass
    scope: str
    ttl_expires_at: datetime
    residual_risk_note: str = ""
    compensating_control_ids: List[str] = Field(default_factory=list)

class SecurityBlastRadiusReport(BaseModel):
    report_id: str
    asset_scope: List[str] = Field(default_factory=list)
    credential_spread: List[str] = Field(default_factory=list)
    environment_scope: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class SecurityEquivalenceReport(BaseModel):
    report_id: str
    asset_id: str
    verdict: EquivalenceVerdict
    proof_notes: str = ""
    divergence_sources: List[str] = Field(default_factory=list)

class SecurityDivergenceReport(BaseModel):
    report_id: str
    severity: str
    blast_radius_refs: List[str] = Field(default_factory=list)
    divergence_details: str = ""

class SecurityTrustVerdict(BaseModel):
    asset_id: str
    verdict: SecurityTrustVerdictEnum
    factors: Dict[str, Any] = Field(default_factory=dict)

class SecurityAuditRecord(BaseModel):
    audit_id: str
    action: str
    timestamp: datetime
    actor_id: str
    details: Dict[str, Any] = Field(default_factory=dict)

class SecurityArtifactManifest(BaseModel):
    manifest_id: str
    asset_refs: List[str] = Field(default_factory=list)
    boundary_refs: List[str] = Field(default_factory=list)
    secret_refs: List[str] = Field(default_factory=list)
    vulnerability_refs: List[str] = Field(default_factory=list)
    trust_verdict_refs: List[str] = Field(default_factory=list)
