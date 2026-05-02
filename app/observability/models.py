from datetime import timezone
from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from app.observability.enums import (
    MetricType,
    MetricUnit,
    ComponentType,
    HealthSeverity,
    AlertSeverity,
    AlertState,
    CorrelationVerdict,
    SloStatus,
    DigestScope,
)


class ObservabilityConfig(BaseModel):
    enabled: bool = True
    storage_path: str = "data/observability"
    max_history_days: int = 30
    alert_quiet_period_minutes: int = 60


class MetricDefinition(BaseModel):
    name: str
    type: MetricType
    unit: MetricUnit
    component: ComponentType
    description: str
    tags: List[str] = Field(default_factory=list)


class MetricSample(BaseModel):
    metric_name: str
    value: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tags: Dict[str, str] = Field(default_factory=dict)
    run_id: Optional[str] = None


class TelemetryEvent(BaseModel):
    event_type: str
    component: ComponentType
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    details: Dict[str, Any] = Field(default_factory=dict)
    severity: AlertSeverity = AlertSeverity.INFO
    run_id: Optional[str] = None


class HealthSignal(BaseModel):
    component: ComponentType
    severity: HealthSeverity
    reason: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metrics_refs: List[str] = Field(default_factory=list)


class ComponentHealthSnapshot(BaseModel):
    component: ComponentType
    severity: HealthSeverity
    last_updated: datetime
    signals: List[HealthSignal] = Field(default_factory=list)
    explanation: str


class SystemHealthSnapshot(BaseModel):
    severity: HealthSeverity
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    components: Dict[ComponentType, ComponentHealthSnapshot] = Field(
        default_factory=dict
    )
    summary: str


class AlertRule(BaseModel):
    rule_id: str
    name: str
    component: ComponentType
    severity: AlertSeverity
    condition_type: str  # e.g., 'threshold', 'stale', 'rate'
    threshold_value: Optional[float] = None
    time_window_seconds: Optional[int] = None
    description: str


class AlertEvent(BaseModel):
    alert_id: str
    rule_id: str
    component: ComponentType
    severity: AlertSeverity
    state: AlertState
    first_seen: datetime
    last_seen: datetime
    occurrence_count: int = 1
    evidence: Dict[str, Any] = Field(default_factory=dict)
    runbook_ref: Optional[str] = None


class AlertCorrelationGroup(BaseModel):
    group_id: str
    verdict: CorrelationVerdict
    primary_alert_id: str
    related_alert_ids: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    likely_parent_issue: str


class AlertSuppressionState(BaseModel):
    alert_rule_id: str
    suppressed_until: datetime
    reason: str
    created_by: str


class SliDefinition(BaseModel):
    sli_id: str
    name: str
    component: ComponentType
    query: str
    target_percentage: float


class SliSnapshot(BaseModel):
    sli_id: str
    current_value: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    period_seconds: int


class SloDefinition(BaseModel):
    slo_id: str
    name: str
    sli_id: str
    warning_threshold: float
    breach_threshold: float


class SloEvaluation(BaseModel):
    slo_id: str
    status: SloStatus
    current_sli_value: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    explanation: str


class TelemetryDigest(BaseModel):
    scope: DigestScope
    start_time: datetime
    end_time: datetime
    top_alerts: List[str]
    health_highlights: str
    slo_summary: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class RunbookRef(BaseModel):
    ref_id: str
    title: str
    description: str
    investigation_steps: List[str]
    mitigation_steps: List[str]


class EnrichedIncidentHint(BaseModel):
    alert_id: str
    impacted_components: List[ComponentType]
    suggested_runbook: Optional[RunbookRef]
    context: str


class ObservabilitySummary(BaseModel):
    system_health: HealthSeverity
    active_critical_alerts: int
    slo_breaches: int
    last_digest_time: Optional[datetime]


class ObservabilityArtifactManifest(BaseModel):
    manifest_id: str
    created_at: datetime
    type: str  # e.g., "digest", "snapshot"
    path: str
    hash: str


class ObservabilityAuditRecord(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    action: str
    actor: str
    details: str
