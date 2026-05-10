from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.release_plane.enums import (
    ReleaseClass,
    CandidateClass,
    BundleClass,
    EnvironmentClass,
    RolloutClass,
    CanaryClass,
    RollbackClass,
    HotfixClass,
    EquivalenceVerdict,
    TrustVerdict,
)

class ReleasePlaneBaseModel(BaseModel):
    class Config:
        frozen = True

class ReleasePlaneConfig(ReleasePlaneBaseModel):
    strict_pinning: bool = True
    allow_hotfix: bool = False
    enforce_canary_before_full: bool = True

class BundlePin(ReleasePlaneBaseModel):
    artifact_id: str
    version_hash: str
    pin_type: str  # e.g., 'model', 'strategy', 'config', 'dependency'
    proof_notes: Optional[str] = None

class ReleaseBundleEntry(ReleasePlaneBaseModel):
    entry_id: str
    entry_type: str
    manifest_ref: str
    pins: List[BundlePin] = Field(default_factory=list)

class ReleaseBundle(ReleasePlaneBaseModel):
    bundle_id: str
    bundle_class: BundleClass
    entries: List[ReleaseBundleEntry] = Field(default_factory=list)
    bundle_hash: str

class EnvironmentTarget(ReleasePlaneBaseModel):
    environment_class: EnvironmentClass
    isolation_rules: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ReleaseDefinition(ReleasePlaneBaseModel):
    release_id: str
    objective: str
    release_class: ReleaseClass
    target_environments: List[EnvironmentTarget] = Field(default_factory=list)

class ReleaseRef(ReleasePlaneBaseModel):
    release_id: str

class ReleaseCandidateRef(ReleasePlaneBaseModel):
    candidate_id: str

class ReleaseCandidate(ReleasePlaneBaseModel):
    candidate_id: str
    definition: ReleaseDefinition
    bundle: ReleaseBundle
    candidate_class: CandidateClass
    created_at: datetime
    expiry: Optional[datetime] = None
    readiness_class: str
    source_refs: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class CompatibilityReport(ReleasePlaneBaseModel):
    report_id: str
    candidate_ref: ReleaseCandidateRef
    environment: EnvironmentClass
    is_compatible: bool
    missing_dependencies: List[str] = Field(default_factory=list)
    blockers: List[str] = Field(default_factory=list)
    proof_notes: Optional[str] = None

class RolloutStage(ReleasePlaneBaseModel):
    stage_id: str
    stage_name: str
    description: str

class RolloutPlan(ReleasePlaneBaseModel):
    plan_id: str
    candidate_ref: ReleaseCandidateRef
    rollout_class: RolloutClass
    stages: List[RolloutStage] = Field(default_factory=list)
    current_stage: str

class CanaryRecord(ReleasePlaneBaseModel):
    canary_id: str
    candidate_ref: ReleaseCandidateRef
    canary_class: CanaryClass
    scope: str
    caps: Dict[str, Any] = Field(default_factory=dict)
    observation_window_seconds: int
    promotion_readiness: bool
    stop_criteria: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class ReleaseDiffRecord(ReleasePlaneBaseModel):
    diff_id: str
    candidate_ref: ReleaseCandidateRef
    active_release_ref: ReleaseRef
    semantic_summaries: List[str] = Field(default_factory=list)
    blast_radius_hints: List[str] = Field(default_factory=list)

class SupersessionRecord(ReleasePlaneBaseModel):
    supersession_id: str
    superseded_by: ReleaseRef
    superseded_release: ReleaseRef
    retained_rollback_window_seconds: int
    lineage_refs: List[str] = Field(default_factory=list)

class HotfixRecord(ReleasePlaneBaseModel):
    hotfix_id: str
    hotfix_class: HotfixClass
    candidate_ref: ReleaseCandidateRef
    scope_limits: Dict[str, Any] = Field(default_factory=dict)
    review_debt: str
    proof_notes: Optional[str] = None

class RollbackPackage(ReleasePlaneBaseModel):
    package_id: str
    target_release_ref: ReleaseRef
    reversible_entries: List[str] = Field(default_factory=list)
    prerequisites: List[str] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)

class RollbackExecutionRecord(ReleasePlaneBaseModel):
    execution_id: str
    package_id: str
    executed_at: datetime

class ReleaseEquivalenceReport(ReleasePlaneBaseModel):
    report_id: str
    candidate_ref: ReleaseCandidateRef
    environments_compared: List[EnvironmentClass] = Field(default_factory=list)
    verdict: EquivalenceVerdict
    proof_notes: Optional[str] = None

class ReleaseDivergenceReport(ReleasePlaneBaseModel):
    report_id: str
    candidate_ref: ReleaseCandidateRef
    environment_drift: List[str] = Field(default_factory=list)
    pin_drift: List[str] = Field(default_factory=list)
    severity: str

class ReleaseTrustVerdict(ReleasePlaneBaseModel):
    verdict_id: str
    candidate_ref: ReleaseCandidateRef
    verdict: TrustVerdict
    factors: Dict[str, Any] = Field(default_factory=dict)

class ReleaseAuditRecord(ReleasePlaneBaseModel):
    audit_id: str
    candidate_ref: ReleaseCandidateRef
    timestamp: datetime
    action: str

class ReleaseArtifactManifest(ReleasePlaneBaseModel):
    manifest_id: str
    candidate_ref: ReleaseCandidateRef
    bundle_hash: str
    pins: List[BundlePin] = Field(default_factory=list)
    lineage_refs: List[str] = Field(default_factory=list)
