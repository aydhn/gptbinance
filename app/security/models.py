from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.security.enums import (
    SecretSourceType, SecretStatus, BackupScope, BackupType, RestoreVerdict,
    IntegritySeverity, EvidenceStatus, RetentionClass, SecurityVerdict, DRRehearsalVerdict
)

class SecretSource(BaseModel):
    type: SecretSourceType
    path: Optional[str] = None

class SecretRef(BaseModel):
    key: str
    description: str = ""

class SecretResolutionResult(BaseModel):
    ref: SecretRef
    source: SecretSource
    status: SecretStatus
    value: Optional[str] = Field(None, repr=False)

class SecretInventoryEntry(BaseModel):
    ref: SecretRef
    status: SecretStatus
    used_by: List[str] = []
    blast_radius: str = "unknown"

class SecurityCheck(BaseModel):
    name: str
    verdict: SecurityVerdict
    message: str

class SecurityCheckReport(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    checks: List[SecurityCheck]
    overall_verdict: SecurityVerdict

class BackupPlan(BaseModel):
    scope: BackupScope
    type: BackupType
    target_dir: str

class BackupArtifact(BaseModel):
    path: str
    size_bytes: int
    hash_sha256: str

class BackupManifest(BaseModel):
    run_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    scope: BackupScope
    artifacts: List[BackupArtifact]

class BackupRun(BaseModel):
    manifest: BackupManifest
    success: bool
    error_message: Optional[str] = None

class RestorePlan(BaseModel):
    source_manifest_path: str
    target_dir: str
    dry_run: bool = True

class RestoreResult(BaseModel):
    verdict: RestoreVerdict
    conflicts: List[str] = []
    restored_artifacts: List[str] = []
    message: str

class IntegrityCheckResult(BaseModel):
    file_path: str
    expected_hash: str
    actual_hash: str
    severity: IntegritySeverity

class EvidenceChainEntry(BaseModel):
    seq_num: int
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    event_type: str
    payload_hash: str
    previous_hash: str
    signature: str = "unsigned"

class RetentionPolicy(BaseModel):
    retention_class: RetentionClass
    max_age_days: int
    action: str

class RotationReadinessReport(BaseModel):
    readiness_score: int
    impacted_modules: List[str]
    recommendations: List[str]

class DisasterRecoveryPlan(BaseModel):
    scenario: str
    steps: List[str]
    estimated_rto_minutes: int

class DisasterRecoveryRehearsal(BaseModel):
    run_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    verdict: DRRehearsalVerdict
    blockers: List[str]

class SecurityAuditRecord(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    event: str
    details: Dict[str, Any]
