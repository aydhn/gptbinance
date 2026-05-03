from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


from app.events.enums import (
    EventSourceType,
    EventCategory,
    EventSeverity,
    EventConfidence,
    EventGateVerdict,
    CooldownMode,
    BlackoutType,
    ImpactClass,
    EventFreshness,
)


class EventRiskConfig(BaseModel):
    max_stale_hours: int = 12
    default_cooldown_minutes: int = 30
    strict_timezone_check: bool = True


class EventSourceConfig(BaseModel):
    source_id: str
    source_type: EventSourceType
    enabled: bool = True
    poll_interval_minutes: int = 60


class EventRecord(BaseModel):
    event_id: str
    source_id: str
    title: str
    category: EventCategory
    severity: EventSeverity
    confidence: EventConfidence
    timestamp: datetime
    end_timestamp: Optional[datetime] = None
    affected_symbols: Optional[List[str]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    freshness: EventFreshness = EventFreshness.FRESH


class EventWindow(BaseModel):
    window_id: str
    start_time: datetime
    end_time: datetime
    events: List[EventRecord]
    max_severity: EventSeverity
    cooldown_mode: CooldownMode


class EventSeverityProfile(BaseModel):
    profile_id: str
    severity_adjustments: Dict[EventCategory, EventSeverity]


class EventImpactModel(BaseModel):
    impact_class: ImpactClass
    description: str


class EventRiskOverlay(BaseModel):
    overlay_id: str
    timestamp: datetime
    active_windows: List[EventWindow]
    verdict: EventGateVerdict
    reasons: List[str]


class EventCalendarSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    events: List[EventRecord]


class EventGateDecision(BaseModel):
    verdict: EventGateVerdict
    reasons: List[str]


class EventCooldownPolicy(BaseModel):
    policy_id: str
    mode: CooldownMode
    pre_event_minutes: int
    post_event_minutes: int


class EventBlackoutWindow(BaseModel):
    blackout_id: str
    start_time: datetime
    end_time: datetime
    blackout_type: BlackoutType
    reason: str


class ExchangeMaintenanceEvent(BaseModel):
    event: EventRecord
    expected_downtime_minutes: int


class MacroCalendarEvent(BaseModel):
    event: EventRecord
    country: str
    indicator: str


class SystemScheduledEvent(BaseModel):
    event: EventRecord
    component: str


class ManualEventOverride(BaseModel):
    override_id: str
    event_id: str
    new_severity: EventSeverity
    reason: str


class EventRiskSummary(BaseModel):
    active_critical_events: int
    active_blackouts: int
    overall_verdict: EventGateVerdict


class EventRiskFinding(BaseModel):
    finding_id: str
    description: str
    severity: EventSeverity


class EventRiskAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    action: str
    details: Dict[str, Any]


class EventRiskArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    artifacts: List[str]
