from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from .enums import (
    SourceClass,
    FieldClass,
    DatasetClass,
    TimeSemantic,
    RevisionClass,
    GapClass,
    AnomalyClass,
    ConsensusClass,
    EquivalenceVerdict,
    TrustVerdict,
)


class DataPlaneConfig(BaseModel):
    storage_path: str = "data_plane_storage"


class DataSourceDefinition(BaseModel):
    source_id: str
    source_class: SourceClass
    is_mainnet: bool
    expected_cadence_ms: Optional[int]


class DataSourceRef(BaseModel):
    source_id: str
    ref_id: str


class DataFieldDefinition(BaseModel):
    field_name: str
    field_class: FieldClass
    nullable: bool
    unit: Optional[str]


class DataSchema(BaseModel):
    schema_id: str
    version: int
    fields: List[DataFieldDefinition]


class DataSchemaVersion(BaseModel):
    version: int
    backward_compatible: bool


class DataPoint(BaseModel):
    value: Any
    event_time: datetime
    available_at_time: datetime


class DataSnapshot(BaseModel):
    snapshot_id: str
    as_of: datetime
    data: Dict[str, Any]


class DataSnapshotRef(BaseModel):
    snapshot_id: str
    hash: str


class DataRevisionRecord(BaseModel):
    revision_id: str
    revision_class: RevisionClass
    original_snapshot_id: str
    new_snapshot_id: str
    reason: str


class BackfillRecord(BaseModel):
    backfill_id: str
    start_time: datetime
    end_time: datetime
    source_id: str


class DataGapFinding(BaseModel):
    gap_id: str
    gap_class: GapClass
    start_time: datetime
    end_time: datetime


class DataAnomalyFinding(BaseModel):
    anomaly_id: str
    anomaly_class: AnomalyClass
    details: str


class DataConsensusRecord(BaseModel):
    consensus_id: str
    consensus_class: ConsensusClass
    rationale: str


class DataAvailabilityWindow(BaseModel):
    window_id: str
    start_time: datetime
    end_time: datetime
    completeness: float


class DataEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str]


class DataTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, Any]
    proof_notes: List[str]


class DataAuditRecord(BaseModel):
    audit_id: str
    action: str
    timestamp: datetime


class DataArtifactManifest(BaseModel):
    manifest_id: str
    source_refs: List[str]
    snapshot_refs: List[str]
