from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.migrations.enums import (
    MigrationDomain,
    MigrationType,
    ApplyClass,
    CompatibilityVerdict,
    ReversibilityClass,
    MigrationSeverity,
    PreflightVerdict,
    MigrationStatus,
    RollbackStrategy,
    MigrationVerdict,
)


class MigrationVersion(BaseModel):
    major: int
    minor: int
    patch: int


class MigrationScope(BaseModel):
    workspaces: List[str] = Field(default_factory=list)
    profiles: List[str] = Field(default_factory=list)
    domains: List[MigrationDomain] = Field(default_factory=list)
    symbols: List[str] = Field(default_factory=list)


class MigrationDependency(BaseModel):
    migration_id: str
    required: bool = True


class CompatibilityDeclaration(BaseModel):
    backward_compatible: bool
    forward_compatible: bool
    read_compatible: bool
    write_compatible: bool
    replay_compatible: bool
    ledger_compatible: bool
    mixed_version_safe: bool
    notes: str = ""


class MigrationDefinition(BaseModel):
    id: str
    name: str
    domain: MigrationDomain
    type: MigrationType
    version_from: str
    version_to: str
    scope: MigrationScope
    dependencies: List[MigrationDependency] = Field(default_factory=list)
    compatibility: CompatibilityDeclaration
    reversibility: ReversibilityClass
    severity: MigrationSeverity
    required_evidence: List[str] = Field(default_factory=list)
    required_approvals: int = 0
    apply_class: ApplyClass
    rollback_hints: str = ""
    description: str = ""


class MigrationPlanStep(BaseModel):
    migration_id: str
    order: int
    estimated_duration_seconds: int = 0


class MigrationPlan(BaseModel):
    id: str
    created_at: datetime
    steps: List[MigrationPlanStep] = Field(default_factory=list)
    target_scope: MigrationScope
    total_estimated_duration_seconds: int = 0


class MigrationPack(BaseModel):
    plan_id: str
    migrations: List[MigrationDefinition] = Field(default_factory=list)


class CompatibilityCheckResult(BaseModel):
    verdict: CompatibilityVerdict
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    safe_window_notes: str = ""


class CompatibilityMatrix(BaseModel):
    domain_versions: Dict[MigrationDomain, str] = Field(default_factory=dict)
    mixed_version_safety: bool
    known_conflicts: List[str] = Field(default_factory=list)


class MigrationPreflightReport(BaseModel):
    plan_id: str
    verdict: PreflightVerdict
    active_runtime_collision: bool
    unresolved_remediation_debt: bool
    stale_qualification: bool
    policy_hard_blocks: List[str] = Field(default_factory=list)
    backup_readiness: bool
    workspace_cleanliness: bool
    evidence_completeness: bool
    blockers: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)


class MigrationDryRunResult(BaseModel):
    plan_id: str
    expected_state_deltas: Dict[str, Any] = Field(default_factory=dict)
    touched_files: List[str] = Field(default_factory=list)
    compatibility_expectations: str = ""
    potential_side_effects: List[str] = Field(default_factory=list)
    expected_verification_outcomes: List[str] = Field(default_factory=list)
    is_noop: bool = False
    simulation_logs: List[str] = Field(default_factory=list)


class MigrationApplyResult(BaseModel):
    plan_id: str
    status: MigrationStatus
    applied_migrations: List[str] = Field(default_factory=list)
    failed_migrations: List[str] = Field(default_factory=list)
    before_snapshot_ref: str = ""
    after_snapshot_ref: str = ""
    logs: List[str] = Field(default_factory=list)


class MigrationRollbackPlan(BaseModel):
    plan_id: str
    eligible: bool
    strategy: RollbackStrategy
    steps: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)


class MigrationRollforwardPlan(BaseModel):
    plan_id: str
    follow_up_migrations: List[str] = Field(default_factory=list)
    quarantine_mode: bool = False
    degraded_compatibility_mode: bool = False
    recovery_path_suggestions: List[str] = Field(default_factory=list)
    staged_stabilization_steps: List[str] = Field(default_factory=list)


class MigrationVerificationResult(BaseModel):
    plan_id: str
    verdict: MigrationVerdict
    target_versions_reached: bool
    compatibility_preserved: bool
    policy_kernel_clean: bool
    evidence_integrity_preserved: bool
    shadow_state_integrity_preserved: bool
    notes: str = ""


class MigrationDebtRecord(BaseModel):
    migration_id: str
    domain: MigrationDomain
    severity: MigrationSeverity
    status: MigrationStatus
    recorded_at: datetime
    impact_summary: str = ""
    stale_definition: bool = False
    incompatible_old_scope: bool = False


class MigrationStatusSnapshot(BaseModel):
    timestamp: datetime
    current_versions: Dict[MigrationDomain, str] = Field(default_factory=dict)
    pending_migrations: List[str] = Field(default_factory=list)


class MigrationAuditRecord(BaseModel):
    action: str
    migration_id: Optional[str]
    plan_id: Optional[str]
    timestamp: datetime
    user: str
    details: Dict[str, Any] = Field(default_factory=dict)


class MigrationArtifactManifest(BaseModel):
    artifacts: List[str] = Field(default_factory=list)
    checksums: Dict[str, str] = Field(default_factory=dict)


class MigrationFabricConfig(BaseModel):
    dry_run_mandatory: bool = True
    enforce_preflight: bool = True
    allow_destructive_apply: bool = False
