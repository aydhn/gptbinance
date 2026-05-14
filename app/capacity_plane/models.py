from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime

from app.capacity_plane.enums import (
    ResourceClass,
    QuotaClass,
    WorkloadClass,
    PriorityClass,
    ReservationClass,
    SaturationSeverity,
    ThrottlingClass,
    SheddingClass,
    FairnessClass,
    EquivalenceVerdict,
    CapacityTrustVerdict,
)


class CapacityResourceRef(BaseModel):
    resource_id: str
    class_name: ResourceClass


class CapacityResource(BaseModel):
    resource_id: str
    class_name: ResourceClass
    owner: str
    scope: str
    total_capacity: float
    unit: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityQuotaRef(BaseModel):
    quota_id: str
    class_name: QuotaClass


class CapacityQuota(BaseModel):
    quota_id: str
    resource_id: str
    class_name: QuotaClass
    limit_value: float
    reset_semantics: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ReservationRecord(BaseModel):
    reservation_id: str
    resource_id: str
    workload_class: WorkloadClass
    priority_class: PriorityClass
    reservation_class: ReservationClass
    amount: float
    created_at: datetime
    expires_at: Optional[datetime] = None
    lineage_refs: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AllocationRecord(BaseModel):
    allocation_id: str
    resource_id: str
    reservation_id: Optional[str] = None
    actor: str
    amount: float
    exclusive: bool
    created_at: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class UsageSnapshot(BaseModel):
    resource_id: str
    timestamp: datetime
    current_usage: float
    peak_usage_1m: float
    sustained_usage_5m: float
    attribution: Dict[str, float] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ConcurrencyLimit(BaseModel):
    limit_id: str
    scope: str
    max_concurrent: int
    current_concurrent: int
    saturation_notes: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ExternalQuotaRecord(BaseModel):
    quota_id: str
    vendor: str
    limit: float
    used: float
    window_seconds: int
    exhaustion_posture: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class RateLimitRecord(BaseModel):
    limit_id: str
    target: str
    rate: float
    window_type: str
    budget_usage_ratio: float
    retry_budget_linked: bool
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SaturationRecord(BaseModel):
    resource_id: str
    severity: SaturationSeverity
    duration_seconds: float
    blast_radius: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BackpressureRecord(BaseModel):
    target_id: str
    queue_growth_rate: float
    consumer_lag: float
    backlog_age_seconds: float
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class QueueDepthRecord(BaseModel):
    queue_id: str
    size: int
    oldest_message_age_seconds: float
    drop_policy: str
    starvation_surfaces: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ThrottlingRecord(BaseModel):
    throttle_id: str
    target_id: str
    throttle_class: ThrottlingClass
    affected_workloads: List[WorkloadClass]
    trigger_history: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SheddingRecord(BaseModel):
    shed_id: str
    target_id: str
    shed_class: SheddingClass
    verification_notes: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class FairnessReport(BaseModel):
    target_id: str
    fairness_class: FairnessClass
    dominance_indicators: Dict[str, float]
    starvation_warnings: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class NoisyNeighborReport(BaseModel):
    resource_id: str
    interfering_workloads: List[str]
    impacted_workloads: List[str]
    burst_collisions: int
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityForecastReport(BaseModel):
    target_id: str
    forecast_type: str
    exhaustion_eta_seconds: Optional[float]
    uncertainty_class: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityDebtRecord(BaseModel):
    debt_id: str
    debt_type: str
    severity: str
    description: str
    created_at: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityEquivalenceReport(BaseModel):
    report_id: str
    workload_class: WorkloadClass
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    divergence_sources: List[str]
    proof_notes: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityDivergenceReport(BaseModel):
    report_id: str
    divergence_type: str
    severity: str
    blast_radius: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityTrustVerdictModel(BaseModel):
    verdict_id: str
    verdict: CapacityTrustVerdict
    factors: Dict[str, str]
    blockers: List[str]
    caveats: List[str]
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityAuditRecord(BaseModel):
    audit_id: str
    action: str
    target_id: str
    actor: str
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapacityArtifactManifest(BaseModel):
    manifest_id: str
    resources: List[CapacityResourceRef]
    quotas: List[CapacityQuotaRef]
    verdict_ref: str
    timestamp: datetime
    hashes: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
