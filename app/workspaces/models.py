from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.workspaces.enums import (
    WorkspaceType,
    ProfileType,
    ContextStatus,
    BoundarySeverity,
    IsolationVerdict,
    SwitchVerdict,
    ScopeType,
    ProfileSensitivity,
    WorkspaceReadiness,
    ContaminationSeverity,
)


class WorkspaceRef(BaseModel):
    workspace_id: str
    name: str


class WorkspaceProfileRef(BaseModel):
    workspace_id: str
    profile_id: str
    profile_type: ProfileType


class WorkspaceConfig(BaseModel):
    workspace_id: str
    name: str
    description: str = ""
    workspace_type: WorkspaceType = WorkspaceType.TRADING
    default_release_line: str = "main"
    default_storage_roots: List[str] = Field(default_factory=list)
    archived: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ScopedPathSet(BaseModel):
    config_root: str
    state_root: str
    artifact_root: str
    log_root: str
    evidence_root: str
    backup_root: str
    metrics_root: str
    replays_root: str
    analytics_root: str


class WorkspaceProfile(BaseModel):
    profile_id: str
    workspace_id: str
    name: str
    profile_type: ProfileType
    allowed_modes: List[str] = Field(default_factory=list)
    product_types: List[str] = Field(default_factory=list)
    risk_profile_refs: List[str] = Field(default_factory=list)
    bundle_model_refs: List[str] = Field(default_factory=list)
    sensitivity: ProfileSensitivity = ProfileSensitivity.LOW
    live_affecting: bool = False
    scoped_paths: Optional[ScopedPathSet] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkspaceManifest(BaseModel):
    workspace_id: str
    schema_version: str = "1.0"
    profile_ids: List[str] = Field(default_factory=list)
    release_refs: List[str] = Field(default_factory=list)
    security_posture_refs: List[str] = Field(default_factory=list)
    data_governance_refs: List[str] = Field(default_factory=list)
    qualification_refs: List[str] = Field(default_factory=list)
    last_active_bundle_refs: List[str] = Field(default_factory=list)
    scoped_paths: Optional[ScopedPathSet] = None
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProfileContextSnapshot(BaseModel):
    snapshot_id: str
    profile_ref: WorkspaceProfileRef
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    active_bundle_ref: Optional[str] = None
    active_release_ref: Optional[str] = None


class WorkspaceContext(BaseModel):
    active_workspace: Optional[WorkspaceConfig] = None
    active_profile: Optional[WorkspaceProfile] = None
    status: ContextStatus = ContextStatus.STALE
    last_switch_at: Optional[datetime] = None


class BoundaryCheckResult(BaseModel):
    check_id: str
    passed: bool
    severity: BoundarySeverity
    details: str
    evidence: Optional[Dict[str, Any]] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProfileBoundary(BaseModel):
    profile_ref: WorkspaceProfileRef
    checks: List[BoundaryCheckResult] = Field(default_factory=list)
    last_verified: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkspaceSwitchRecord(BaseModel):
    switch_id: str
    from_profile: Optional[WorkspaceProfileRef] = None
    to_profile: WorkspaceProfileRef
    verdict: SwitchVerdict
    reason: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ScopedStorageRef(BaseModel):
    ref_id: str
    scope_type: ScopeType
    target_id: str
    path: str
    read_only: bool = False


class WorkspaceHealthSummary(BaseModel):
    workspace_id: str
    readiness: WorkspaceReadiness
    boundary_violations: int = 0
    contamination_suspicions: int = 0
    last_checked: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkspaceCatalogEntry(BaseModel):
    workspace: WorkspaceConfig
    profiles: List[WorkspaceProfile]
    health: Optional[WorkspaceHealthSummary] = None


class WorkspaceAuditRecord(BaseModel):
    audit_id: str
    workspace_id: str
    action: str
    profile_id: Optional[str] = None
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkspaceArtifactManifest(BaseModel):
    artifact_id: str
    profile_ref: WorkspaceProfileRef
    paths: List[str]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ContaminationFinding(BaseModel):
    finding_id: str
    severity: ContaminationSeverity
    impacted_profiles: List[WorkspaceProfileRef]
    evidence: Dict[str, Any]
    recommended_actions: List[str]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
