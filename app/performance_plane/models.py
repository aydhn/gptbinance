from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from decimal import Decimal

from app.performance_plane.enums import (
    PerformanceDomain,
    BenchmarkClass,
    ReturnClass,
    AttributionClass,
    DragClass,
    OpportunityClass,
    CohortClass,
    EquivalenceVerdict,
    TrustVerdict,
    WindowClass,
)


class PerformancePlaneConfig(BaseModel):
    strict_benchmark_checks: bool = True
    enforce_equivalence_thresholds: bool = True


class PerformanceWindow(BaseModel):
    window_class: WindowClass
    start_time: datetime
    end_time: Optional[datetime] = None
    is_complete: bool = False
    caveats: List[str] = Field(default_factory=list)


class BenchmarkRef(BaseModel):
    benchmark_id: str
    version: str


class BenchmarkDefinition(BaseModel):
    benchmark_id: str
    benchmark_class: BenchmarkClass
    description: str
    comparability_requirements: List[str]
    freshness_ttl_seconds: int


class ReturnSurfaceRef(BaseModel):
    surface_id: str


class ReturnSurface(BaseModel):
    surface_id: str
    return_class: ReturnClass
    domain: PerformanceDomain
    target_id: str
    window: PerformanceWindow
    value: Decimal
    currency: str
    caveats: List[str] = Field(default_factory=list)


class AttributionNode(BaseModel):
    attribution_class: AttributionClass
    contribution_value: Decimal
    currency: str
    proof_notes: List[str] = Field(default_factory=list)


class AttributionTree(BaseModel):
    tree_id: str
    surface_id: str
    nodes: List[AttributionNode]
    residual_value: Decimal
    currency: str


class DragComponent(BaseModel):
    component_id: str
    drag_class: DragClass
    impact_value: Decimal
    currency: str
    lineage_refs: List[str] = Field(default_factory=list)


class OpportunitySurface(BaseModel):
    surface_id: str
    opportunity_class: OpportunityClass
    estimated_value: Decimal
    currency: str
    confidence_score: float
    caveats: List[str] = Field(default_factory=list)


class CaptureRatioRecord(BaseModel):
    record_id: str
    step_name: str
    ratio: float
    degradation_notes: List[str] = Field(default_factory=list)


class CohortContribution(BaseModel):
    cohort_class: CohortClass
    cohort_id: str
    contribution_value: Decimal
    currency: str
    caveats: List[str] = Field(default_factory=list)


class PerformanceManifestEntry(BaseModel):
    entry_id: str
    entry_type: str
    reference_id: str


class PerformanceManifest(BaseModel):
    manifest_id: str
    window: PerformanceWindow
    entries: List[PerformanceManifestEntry]
    hash_signature: str


class BenchmarkRelativeReport(BaseModel):
    report_id: str
    surface_id: str
    benchmark_ref: BenchmarkRef
    relative_value: Decimal
    mismatch_cautions: List[str] = Field(default_factory=list)


class PerformanceEquivalenceReport(BaseModel):
    report_id: str
    source_manifest_id: str
    target_manifest_id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)


class PerformanceTrustVerdict(BaseModel):
    verdict_id: str
    manifest_id: str
    verdict: TrustVerdict
    blockers: List[str] = Field(default_factory=list)
    factors: Dict[str, Any] = Field(default_factory=dict)


class PerformanceAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    action: str
    details: Dict[str, Any]


class PerformanceArtifactManifest(BaseModel):
    artifact_id: str
    manifest_id: str
    artifact_type: str
