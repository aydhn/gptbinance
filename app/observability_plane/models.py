from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum
from .enums import (
    TelemetryClass, MetricClass, LogClass, TraceClass, EventClass,
    ClockClass, SamplingClass, RetentionClass, DiagnosticClass,
    EquivalenceVerdict, TrustVerdict
)

class ObservabilityPlaneConfig(BaseModel):
    enforce_canonical_telemetry: bool = True
    block_unstructured_logs: bool = True
    require_explicit_sampling: bool = True
    reject_clock_ambiguity: bool = True

class TelemetryDefinition(BaseModel):
    telemetry_id: str
    telemetry_class: TelemetryClass
    producer: str
    description: str
    is_mandatory: bool = False

class TelemetryRef(BaseModel):
    telemetry_id: str
    version: str = "1.0"

class MetricDefinition(TelemetryDefinition):
    metric_class: MetricClass
    unit: str
    aggregation_compatibility: List[str]

class LogSchema(TelemetryDefinition):
    log_class: LogClass
    required_fields: List[str]
    severity_taxonomy: List[str]
    schema_version: str

class TraceDefinition(TelemetryDefinition):
    trace_class: TraceClass
    parent_child_linkage: bool
    expected_spans: List[str]

class EventDefinition(TelemetryDefinition):
    event_class: EventClass
    provenance: str

class DimensionDefinition(BaseModel):
    dimension_id: str
    scope: str
    is_mandatory: bool

class TagDefinition(BaseModel):
    tag_id: str
    cardinality_expectation: str

class ClockSemanticRecord(BaseModel):
    telemetry_id: str
    clock_class: ClockClass
    window_semantics: Optional[str] = None

class SamplingRecord(BaseModel):
    telemetry_id: str
    sampling_class: SamplingClass
    sampling_rate: float

class RetentionRecord(BaseModel):
    telemetry_id: str
    retention_class: RetentionClass
    retention_days: int

class TelemetryIngestionRecord(BaseModel):
    ingestion_id: str
    source_ref: str
    lag_ms: int

class TelemetryNormalizationRecord(BaseModel):
    normalization_id: str
    telemetry_id: str
    semantic_rewrite: bool = False

class TelemetryCorrelationReport(BaseModel):
    correlation_id: str
    telemetry_refs: List[str]
    confidence_score: float

class TelemetryGapFinding(BaseModel):
    gap_id: str
    missing_telemetry_id: str
    blast_radius: str

class TelemetryAnomalyFinding(BaseModel):
    anomaly_id: str
    telemetry_id: str
    anomaly_type: str

class CardinalityCostRecord(BaseModel):
    telemetry_id: str
    estimated_series: int
    cost_burden: str

class DiagnosticSignal(BaseModel):
    signal_id: str
    diagnostic_class: DiagnosticClass
    contributing_telemetry: List[str]

class SliSupportRecord(BaseModel):
    sli_id: str
    supported_telemetry_refs: List[str]

class ObservabilityEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict

class ObservabilityDivergenceReport(BaseModel):
    report_id: str
    divergence_sources: List[str]

class ObservabilityTrustVerdict(BaseModel):
    verdict: TrustVerdict
    factors: Dict[str, str]

class ObservabilityAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime
    verdict: TrustVerdict

class ObservabilityArtifactManifest(BaseModel):
    manifest_id: str
    telemetry_refs: List[TelemetryRef]
    trust_verdict: ObservabilityTrustVerdict
