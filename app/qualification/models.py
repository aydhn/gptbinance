from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
import uuid

from app.qualification.enums import (
    QualificationScope,
    QualificationProfile,
    RequirementCriticality,
    ScenarioType,
    ContractSeverity,
    CertificationVerdict,
    EvidenceStatus,
    WaiverStatus,
    EnvironmentReadiness,
    GoNoGoVerdict,
)


class QualificationConfig(BaseModel):
    strict_mode: bool = Field(
        default=True, description="Enforce all requirements strictly"
    )
    allow_waivers: bool = Field(
        default=True, description="Allow waivers for non-critical findings"
    )
    evidence_retention_days: int = Field(default=30)
    dry_run: bool = Field(default=False)


class RequirementRef(BaseModel):
    req_id: str
    description: str
    criticality: RequirementCriticality
    scope: QualificationScope


class TraceabilityEntry(BaseModel):
    req_id: str
    scenario_ids: List[str] = Field(default_factory=list)
    evidence_refs: List[str] = Field(default_factory=list)
    is_covered: bool = Field(default=False)


class ScenarioResult(BaseModel):
    scenario_id: str
    scenario_type: ScenarioType
    passed: bool
    evidence_refs: List[str] = Field(default_factory=list)
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ContractCheckResult(BaseModel):
    contract_id: str
    source_component: str
    target_component: str
    passed: bool
    severity: ContractSeverity
    drift_detected: bool = Field(default=False)
    details: Dict[str, Any] = Field(default_factory=dict)


class ForbiddenActionCheck(BaseModel):
    action_id: str
    description: str
    was_blocked: bool  # True means pass (the action was correctly blocked)
    details: Dict[str, Any] = Field(default_factory=dict)


class QualificationEvidenceRef(BaseModel):
    evidence_id: str
    source: str
    status: EvidenceStatus
    artifact_uri: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class QualificationFinding(BaseModel):
    finding_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    criticality: RequirementCriticality
    scenario_id: Optional[str] = None
    contract_id: Optional[str] = None
    is_waived: bool = Field(default=False)
    waiver_id: Optional[str] = None


class WaiverRecord(BaseModel):
    waiver_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    finding_id: str
    rationale: str
    status: WaiverStatus = Field(default=WaiverStatus.ACTIVE)
    approved_by: str
    expires_at: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class QualificationScore(BaseModel):
    overall_score: float = Field(default=0.0)
    golden_path_pass_rate: float = Field(default=0.0)
    negative_test_pass_rate: float = Field(default=0.0)
    contract_verification_score: float = Field(default=0.0)
    evidence_completeness: float = Field(default=0.0)
    critical_findings_count: int = Field(default=0)
    waived_findings_count: int = Field(default=0)


class QualificationVerdict(BaseModel):
    profile: QualificationProfile
    verdict: CertificationVerdict
    go_no_go: GoNoGoVerdict
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    recommended_actions: List[str] = Field(default_factory=list)


class EnvironmentQualificationMatrix(BaseModel):
    paper: EnvironmentReadiness = Field(default=EnvironmentReadiness.NOT_READY)
    shadow: EnvironmentReadiness = Field(default=EnvironmentReadiness.NOT_READY)
    testnet: EnvironmentReadiness = Field(default=EnvironmentReadiness.NOT_READY)
    live: EnvironmentReadiness = Field(default=EnvironmentReadiness.NOT_READY)


class EvidencePack(BaseModel):
    pack_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    run_id: str
    release_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    security_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    backup_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    ops_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    control_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    observability_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    resilience_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    governance_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    analytics_refs: List[QualificationEvidenceRef] = Field(default_factory=list)
    is_complete: bool = Field(default=False)
    assembled_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class QualificationRun(BaseModel):
    run_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    profile: QualificationProfile
    config: QualificationConfig
    scenarios: List[ScenarioResult] = Field(default_factory=list)
    contracts: List[ContractCheckResult] = Field(default_factory=list)
    forbidden_actions: List[ForbiddenActionCheck] = Field(default_factory=list)
    findings: List[QualificationFinding] = Field(default_factory=list)
    evidence_pack_id: Optional[str] = None
    score: Optional[QualificationScore] = None
    verdict: Optional[QualificationVerdict] = None
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None


class QualificationSuite(BaseModel):
    suite_id: str
    description: str
    scenarios: List[str] = Field(default_factory=list)


class QualificationScenario(BaseModel):
    scenario_id: str
    description: str
    type: ScenarioType
    prerequisites: List[str] = Field(default_factory=list)
    required_evidence: List[str] = Field(default_factory=list)


class CertificationSummary(BaseModel):
    summary_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    run_id: str
    profile: QualificationProfile
    verdict: GoNoGoVerdict
    score: QualificationScore
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class CertificationStatus(BaseModel):
    profile: QualificationProfile
    is_certified: bool
    verdict: GoNoGoVerdict
    last_run_id: Optional[str] = None
    last_run_time: Optional[datetime] = None
    is_stale: bool = Field(default=True)


class QualificationArtifactManifest(BaseModel):
    manifest_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    run_id: str
    artifacts: Dict[str, str] = Field(default_factory=dict)  # key: type, value: uri
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class QualificationAuditRecord(BaseModel):
    audit_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    run_id: str
    event: str
    details: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
