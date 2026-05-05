from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.remediation.enums import (
    RemediationClass,
    ApplyMode,
    BlastRadiusSeverity,
    VerificationVerdict,
    DebtSeverity,
)


class RemediationFindingRef(BaseModel):
    finding_id: str
    source_domain: str
    severity: str
    detected_at: datetime
    is_stale: bool = False
    context: Dict[str, Any] = Field(default_factory=dict)


class RemediationRecipe(BaseModel):
    recipe_id: str
    name: str
    safety_class: RemediationClass
    supported_finding_sources: List[str]
    allowed_apply_modes: List[ApplyMode]
    requires_approval: bool


class RemediationScope(BaseModel):
    workspace: str = "default"
    profile: Optional[str] = None
    symbol: Optional[str] = None
    run_id: Optional[str] = None


class RemediationAction(BaseModel):
    action_id: str
    type: str
    parameters: Dict[str, Any]
    is_reversible: bool


class BlastRadiusReport(BaseModel):
    severity: BlastRadiusSeverity
    impacted_domains: List[str]
    side_effects: List[str]
    conflict_warnings: List[str]


class RollbackPlan(BaseModel):
    is_eligible: bool
    steps: List[Dict[str, Any]]
    reason_if_not_eligible: Optional[str] = None


class RemediationPack(BaseModel):
    pack_id: str
    finding_ref: RemediationFindingRef
    recipe: RemediationRecipe
    scope: RemediationScope
    actions: List[RemediationAction]
    blast_radius: Optional[BlastRadiusReport] = None
    rollback_plan: Optional[RollbackPlan] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SimulationResult(BaseModel):
    is_safe: bool
    expected_deltas: List[str]
    verification_expectations: List[str]
    no_op_detected: bool


class ApplyResult(BaseModel):
    success: bool
    mode_used: ApplyMode
    generated_request_id: Optional[str] = None
    before_snapshot_ref: Optional[str] = None
    after_snapshot_ref: Optional[str] = None
    error_message: Optional[str] = None


class VerificationResult(BaseModel):
    verdict: VerificationVerdict
    details: str
    verified_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class RemediationDebtRecord(BaseModel):
    debt_id: str
    finding_ref: RemediationFindingRef
    severity: DebtSeverity
    failed_attempts: int
    aging_days: int
    is_qualification_blocker: bool
