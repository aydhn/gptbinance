from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
import uuid

from app.migration_plane.enums import (
    MigrationClass, TransitionClass, CompatibilityClass,
    PrecheckClass, CutoverClass, RollbackClass, DebtClass,
    ShimClass, EquivalenceVerdict, TrustVerdict
)

class MigrationRef(BaseModel):
    migration_id: str
    version_id: str

class MigrationVersionPair(BaseModel):
    source_version: str
    target_version: str
    is_downgrade: bool = False

class TransitionContract(BaseModel):
    transition_class: TransitionClass
    prerequisites: List[str] = Field(default_factory=list)
    is_destructive: bool = False

class CompatibilityShim(BaseModel):
    shim_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    shim_class: ShimClass
    description: str
    ttl_seconds: int
    cleanup_plan: str

class MigrationDefinition(BaseModel):
    migration_id: str
    migration_class: MigrationClass
    version_pair: MigrationVersionPair
    transition_contract: TransitionContract
    affected_artefacts: List[str]
    is_mandatory: bool = True
    description: str

class MigrationPrecheckRecord(BaseModel):
    migration_id: str
    precheck_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: PrecheckClass
    details: Dict[str, Any]
    blockers: List[str]

class MigrationDryRunRecord(BaseModel):
    migration_id: str
    dry_run_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_successful: bool
    blast_radius: Dict[str, Any]
    divergence_notes: List[str]
    fidelity_class: str

class MigrationCutoverRecord(BaseModel):
    migration_id: str
    cutover_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    cutover_class: CutoverClass
    start_time: datetime
    end_time: Optional[datetime] = None
    is_successful: bool
    details: Dict[str, Any]
    environment: str

class MigrationVerificationRecord(BaseModel):
    cutover_id: str
    verification_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_successful: bool
    details: Dict[str, Any]

class BackfillExecutionRecord(BaseModel):
    migration_id: str
    backfill_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_required: bool
    is_successful: bool
    details: Dict[str, Any]

class ReindexExecutionRecord(BaseModel):
    migration_id: str
    reindex_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_successful: bool
    details: Dict[str, Any]

class RehydrationRecord(BaseModel):
    migration_id: str
    rehydration_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_successful: bool
    details: Dict[str, Any]

class DualWriteRecord(BaseModel):
    migration_id: str
    dual_write_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    start_time: datetime
    end_time: Optional[datetime] = None
    expiry: datetime
    divergence_detected: bool

class RollbackMigrationRecord(BaseModel):
    migration_id: str
    rollback_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    rollback_class: RollbackClass
    is_successful: bool
    details: Dict[str, Any]

class FallbackRecord(BaseModel):
    migration_id: str
    fallback_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_successful: bool
    details: Dict[str, Any]

class MigrationDebtRecord(BaseModel):
    debt_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    migration_id: str
    debt_class: DebtClass
    severity: str
    details: Dict[str, Any]
    is_resolved: bool = False

class MigrationEquivalenceReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    migration_id: str
    verdict: EquivalenceVerdict
    details: Dict[str, Any]

class MigrationDivergenceReport(BaseModel):
    report_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    migration_id: str
    severity: str
    details: Dict[str, Any]

class MigrationTrustVerdict(BaseModel):
    verdict_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    migration_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MigrationAuditRecord(BaseModel):
    audit_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    migration_id: str
    action: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    details: Dict[str, Any]

class MigrationArtifactManifest(BaseModel):
    manifest_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    migration_id: str
    hash_value: str
    lineage_refs: List[str]
    details: Dict[str, Any]

class MigrationPlaneConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
