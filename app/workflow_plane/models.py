from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.workflow_plane.enums import (
    RunState, TriggerClass, GateClass, TrustVerdict, WorkflowClass,
    JobClass, ScheduleClass, WindowClass, DependencyClass, RetryClass,
    RerunClass, EquivalenceVerdict
)

class RunWindow(BaseModel):
    window_id: str
    start_time: datetime
    end_time: datetime
    as_of_cut: datetime
    available_data_cut: Optional[datetime] = None
    window_class: WindowClass = WindowClass.ROLLING
    is_partial: bool = False

class JobContract(BaseModel):
    job_id: str
    job_class: JobClass
    description: str
    is_idempotent: bool
    mutability_class: str
    recoverability_class: str
    required_trust_inputs: List[str]

class TriggerDefinition(BaseModel):
    trigger_class: TriggerClass
    description: str
    lineage_ref: Optional[str] = None

class ScheduleDefinition(BaseModel):
    schedule_id: str
    schedule_class: ScheduleClass
    cadence: str
    description: str

class WorkflowDefinition(BaseModel):
    workflow_id: str
    objective: str
    workflow_class: WorkflowClass
    jobs: List[JobContract]
    triggers: List[TriggerDefinition] = []
    critical: bool = False
    scope_metadata: Dict[str, Any] = Field(default_factory=dict)
    lineage_refs: List[str] = Field(default_factory=list)

class GateCheckResult(BaseModel):
    gate_class: GateClass
    passed: bool
    rationale: str
    severity: str = "low"
    bypassed: bool = False
    audit_ref: Optional[str] = None

class JobRun(BaseModel):
    job_run_id: str
    job_id: str
    state: RunState
    started_at: datetime
    completed_at: Optional[datetime] = None

class WorkflowRun(BaseModel):
    run_id: str
    workflow_id: str
    window: RunWindow
    trigger_class: TriggerClass
    state: RunState
    started_at: datetime
    completed_at: Optional[datetime] = None
    gate_results: List[GateCheckResult] = []
    job_runs: List[JobRun] = []
    receipts: List[Dict[str, Any]] = []
    superseded_by: Optional[str] = None
    start_reason: Optional[str] = None
    stop_reason: Optional[str] = None
    parent_run_id: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class RetryRecord(BaseModel):
    retry_id: str
    run_id: str
    reason: str
    retry_class: RetryClass
    retry_count: int

class ResumeRecord(BaseModel):
    resume_id: str
    run_id: str
    checkpoint_ref: str
    reason: str
    resumed_lineage: Optional[str] = None

class RerunRecord(BaseModel):
    rerun_id: str
    original_run_id: str
    new_run_id: str
    reason: str
    rerun_class: RerunClass
    same_window: bool
    approved_by: str

class BackfillRunRecord(BaseModel):
    backfill_id: str
    workflow_id: str
    start_window: RunWindow
    end_window: RunWindow
    reason: str
    lineage_refs: List[str] = Field(default_factory=list)

class RunReceipt(BaseModel):
    receipt_id: str
    run_id: str
    trigger_provenance: str
    completion_summary: str
    failure_summary: Optional[str] = None
    gate_outcomes: List[GateCheckResult] = []
    output_refs: List[str] = Field(default_factory=list)

class WorkflowDependencyEdge(BaseModel):
    upstream_job_id: str
    downstream_job_id: str
    dependency_class: DependencyClass
    must_share_same_window: bool = True
    must_share_same_snapshot: bool = True

class RunCheckpoint(BaseModel):
    checkpoint_id: str
    run_id: str
    job_id: str
    payload_metadata: Dict[str, Any]
    freshness: datetime
    downstream_compatible: bool = True

class WorkflowEquivalenceReport(BaseModel):
    report_id: str
    workflow_id: str
    run_window: RunWindow
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    differences: List[str] = Field(default_factory=list)
    proof_notes: str

class WorkflowDivergenceReport(BaseModel):
    report_id: str
    workflow_id: str
    divergence_type: str
    severity: str
    blast_radius: str
    description: str

class WorkflowTrustVerdict(BaseModel):
    verdict: TrustVerdict
    factors: Dict[str, str] = Field(default_factory=dict)
    breakdown_mandatory: bool = True

class WorkflowAuditRecord(BaseModel):
    audit_id: str
    action: str
    workflow_id: str
    actor: str
    timestamp: datetime
    details: Dict[str, Any] = Field(default_factory=dict)

class WorkflowArtifactManifest(BaseModel):
    manifest_id: str
    workflow_id: str
    run_id: str
    artifacts: List[str] = Field(default_factory=list)
