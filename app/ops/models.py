from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.ops.enums import (
    OpsMode,
    RolloutMode,
    ReadinessVerdict,
    IncidentType,
    IncidentSeverity,
    MaintenanceStatus,
    SupervisorStatus,
    ControlAction,
    RecoveryVerdict,
    GoLiveVerdict,
)


class OpsConfig(BaseModel):
    mode: OpsMode = OpsMode.PAPER
    rollout: RolloutMode = RolloutMode.STANDARD
    run_id: str
    require_readiness: bool = True
    enforce_kill_switch: bool = True


class OpsRun(BaseModel):
    run_id: str
    started_at: datetime = Field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = None
    config: OpsConfig
    status: SupervisorStatus = SupervisorStatus.INITIALIZING


class ReadinessCheckResult(BaseModel):
    name: str
    verdict: ReadinessVerdict
    rationale: str
    remediation: Optional[str] = None
    severity: IncidentSeverity = IncidentSeverity.LOW


class ReadinessReport(BaseModel):
    run_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    checks: List[ReadinessCheckResult]
    overall_verdict: ReadinessVerdict


class SessionSupervisorState(BaseModel):
    run_id: str
    status: SupervisorStatus
    last_health_check: datetime = Field(default_factory=datetime.utcnow)
    active_incidents: List[str] = Field(default_factory=list)


class IncidentRecord(BaseModel):
    incident_id: str
    run_id: str
    type: IncidentType
    severity: IncidentSeverity
    details: str
    detected_at: datetime = Field(default_factory=datetime.utcnow)
    resolved_at: Optional[datetime] = None
    resolved: bool = False


class MaintenanceWindow(BaseModel):
    window_id: str
    start_time: datetime
    end_time: datetime
    status: MaintenanceStatus = MaintenanceStatus.SCHEDULED
    description: str
    allowed_actions: List[str] = Field(default_factory=list)


class PauseRequest(BaseModel):
    run_id: str
    reason: str
    requested_at: datetime = Field(default_factory=datetime.utcnow)


class ResumeRequest(BaseModel):
    run_id: str
    clearance_code: str
    requested_at: datetime = Field(default_factory=datetime.utcnow)


class DrainState(BaseModel):
    run_id: str
    drain_initiated_at: datetime = Field(default_factory=datetime.utcnow)
    new_intents_frozen: bool = False
    open_orders_remaining: int = 0
    drain_complete: bool = False


class RecoveryPlan(BaseModel):
    run_id: str
    hydrate_positions: bool
    reconcile_orders: bool
    unresolved_anomalies: List[str] = Field(default_factory=list)


class RecoveryResult(BaseModel):
    run_id: str
    verdict: RecoveryVerdict
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class GoLiveGateReport(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    verdict: GoLiveVerdict
    reasons: List[str]
    blockers: List[str]
    recommended_actions: List[str]


class ShadowModeConfig(BaseModel):
    enabled: bool = False
    paper_symbols: List[str] = Field(default_factory=list)
    sink_type: str = "log"


class CanaryModeConfig(BaseModel):
    enabled: bool = False
    symbols: List[str] = Field(default_factory=list)
    max_orders: int = 5
    max_risk_usd: float = 100.0
    duration_minutes: int = 60


class RuntimeControlDecision(BaseModel):
    action: ControlAction
    reason: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class OpsAuditRecord(BaseModel):
    run_id: str
    action: str
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class RolloverSummary(BaseModel):
    run_id: str
    date: datetime
    total_orders: int
    incidents_count: int
    status: str
