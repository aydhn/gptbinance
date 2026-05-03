from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.perf.enums import (
    WorkloadType,
    ProfileScope,
    ResourceType,
    BudgetSeverity,
    HostClass,
    RegressionSeverity,
    ReadinessVerdict,
    LatencyPercentile,
    BottleneckType,
    PerfVerdict,
)


class PerfConfig(BaseModel):
    enabled: bool = True
    storage_path: str = "data/perf"


class PerfProfile(BaseModel):
    profile_id: str
    workload_type: WorkloadType
    scope: ProfileScope
    duration_sec: float
    recorded_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkloadDefinition(BaseModel):
    workload_type: WorkloadType
    target_components: List[str]
    expected_inputs: Dict[str, Any]
    measurement_scope: ProfileScope
    representative_concurrency: int
    safe_modes: List[str]


class ResourceUsageSnapshot(BaseModel):
    cpu_percent: float
    memory_mb: float
    disk_read_mb: float
    disk_write_mb: float
    network_rx_kb: float
    network_tx_kb: float


class CpuProfileSummary(BaseModel):
    peak_cpu_percent: float
    avg_cpu_percent: float
    top_components: Dict[str, float]


class MemoryProfileSummary(BaseModel):
    peak_memory_mb: float
    memory_growth_mb: float
    leak_suspicion: bool


class DiskProfileSummary(BaseModel):
    total_read_mb: float
    total_write_mb: float
    peak_iops: float


class NetworkProfileSummary(BaseModel):
    total_rx_kb: float
    total_tx_kb: float


class ComponentLatencySummary(BaseModel):
    component_name: str
    p50_ms: float
    p95_ms: float
    p99_ms: float
    max_ms: float
    call_count: int


class PerfRun(BaseModel):
    run_id: str
    workload_type: WorkloadType
    host_class: HostClass
    start_time: datetime
    end_time: datetime
    duration_sec: float
    cpu_summary: CpuProfileSummary
    memory_summary: MemoryProfileSummary
    disk_summary: DiskProfileSummary
    network_summary: NetworkProfileSummary
    latencies: List[ComponentLatencySummary]
    verdict: PerfVerdict


class ResourceBudget(BaseModel):
    resource_type: ResourceType
    severity: BudgetSeverity
    limit_value: float
    applicable_modes: List[str]


class LatencyBudget(BaseModel):
    component_name: str
    percentile: LatencyPercentile
    severity: BudgetSeverity
    limit_ms: float
    applicable_modes: List[str]


class BottleneckReport(BaseModel):
    run_id: str
    bottleneck_type: BottleneckType
    likely_component: str
    evidence: str
    impacted_workloads: List[WorkloadType]
    recommendation: str


class HostClassDefinition(BaseModel):
    host_class: HostClass
    expected_cores: int
    expected_ram_gb: int
    recommended_modes: List[str]
    caution_modes: List[str]


class CapacityReport(BaseModel):
    host_class: HostClass
    available_headroom_percent: float
    concurrency_cautions: List[str]
    reserve_capacity_recommendation: str
    unsupported_combinations: List[str]


class HostQualificationReport(BaseModel):
    host_class: HostClass
    tested_workloads: List[WorkloadType]
    readiness: ReadinessVerdict
    evidence_refs: List[str]
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PerfFinding(BaseModel):
    metric_name: str
    baseline_value: float
    target_value: float
    delta_percent: float
    is_regression: bool


class PerfRegressionReport(BaseModel):
    baseline_run_id: str
    target_run_id: str
    severity: RegressionSeverity
    findings: List[PerfFinding]
    recommendation: str
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PerfArtifactManifest(BaseModel):
    run_id: str
    artifacts_stored: List[str]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class PerfRecommendation(BaseModel):
    workload: WorkloadType
    caution_message: str


class PerfAuditRecord(BaseModel):
    record_id: str
    action: str
    details: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkloadResult(BaseModel):
    run_id: str
    success: bool
    data: Dict[str, Any]
