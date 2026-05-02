from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.release.enums import (
    ReleaseStage,
    BundleType,
    CompatibilityVerdict,
    MigrationDirection,
    MigrationSeverity,
    InstallVerdict,
    UpgradeVerdict,
    RollbackVerdict,
    HostReadiness,
    DependencyStatus,
)


class ReleaseVersion(BaseModel):
    version: str
    stage: ReleaseStage
    build_fingerprint: str
    config_schema_version: str
    state_schema_version: str
    artifact_schema_version: str


class DependencyLockSummary(BaseModel):
    fingerprint: str
    status: DependencyStatus
    drift_details: List[str] = []


class ReleaseComponentRef(BaseModel):
    name: str
    version: str
    checksum: str


class ReleaseManifest(BaseModel):
    version: ReleaseVersion
    dependency_lock: DependencyLockSummary
    components: List[ReleaseComponentRef]
    supported_modes: List[str]
    required_python_version: str
    rollback_refs: List[str]


class ReleaseBundle(BaseModel):
    manifest: ReleaseManifest
    archive_path: str
    checksum: str
    created_at: datetime


class ReleaseConfig(BaseModel):
    version: str
    stage: ReleaseStage


class HostProbeReport(BaseModel):
    readiness: HostReadiness
    python_version_ok: bool
    disk_space_ok: bool
    writable_paths_ok: bool
    warnings: List[str] = []
    blockers: List[str] = []


class CompatibilityReport(BaseModel):
    target_version: str
    current_version: str
    verdict: CompatibilityVerdict
    migrations_required: List[str] = []
    warnings: List[str] = []


class SchemaVersionSnapshot(BaseModel):
    config_schema_version: str
    state_schema_version: str
    artifact_schema_version: str


class MigrationRecord(BaseModel):
    migration_id: str
    direction: MigrationDirection
    severity: MigrationSeverity
    applied_at: datetime
    success: bool
    error_message: Optional[str] = None


class MigrationPlan(BaseModel):
    source_version: str
    target_version: str
    migrations_to_apply: List[str]
    estimated_severity: MigrationSeverity
    dry_run: bool


class UpgradePlan(BaseModel):
    target_release: ReleaseManifest
    compatibility_report: CompatibilityReport
    migration_plan: Optional[MigrationPlan] = None
    verdict: UpgradeVerdict
    warnings: List[str] = []


class UpgradeResult(BaseModel):
    plan: UpgradePlan
    success: bool
    applied_at: datetime
    error_message: Optional[str] = None


class RollbackPlan(BaseModel):
    target_release: ReleaseManifest
    compatibility_report: CompatibilityReport
    migration_plan: Optional[MigrationPlan] = None
    verdict: RollbackVerdict
    warnings: List[str] = []


class RollbackResult(BaseModel):
    plan: RollbackPlan
    success: bool
    applied_at: datetime
    error_message: Optional[str] = None


class InstallPlan(BaseModel):
    target_release: ReleaseManifest
    host_probe: HostProbeReport
    verdict: InstallVerdict
    warnings: List[str] = []


class BootstrapResult(BaseModel):
    plan: InstallPlan
    success: bool
    applied_at: datetime
    error_message: Optional[str] = None


class ReleaseAuditRecord(BaseModel):
    run_id: str
    action: str
    details: Dict[str, Any]
    timestamp: datetime


class ReleaseArtifactManifest(BaseModel):
    files: Dict[str, str]


class ReleaseSummary(BaseModel):
    bundle: ReleaseBundle
    host_probe: HostProbeReport
    compatibility: CompatibilityReport
