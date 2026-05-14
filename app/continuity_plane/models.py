from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.continuity_plane.enums import (
    ContinuityServiceClass, ContinuityObjectiveClass, BackupClass,
    SnapshotClass, ReplicationClass, RestoreClass, FailoverClass,
    FailbackClass, StandbyClass, ContinuityEquivalenceVerdict,
    ContinuityTrustVerdict
)

class ContinuityServiceRef(BaseModel):
    service_id: str
    description: Optional[str] = None

class ContinuityObjectiveRef(BaseModel):
    objective_id: str
    description: Optional[str] = None

class RtoTarget(BaseModel):
    target_seconds: int
    is_strict: bool = True
    caveats: Optional[str] = None

class RpoTarget(BaseModel):
    target_seconds: int
    is_strict: bool = True
    caveats: Optional[str] = None

class ContinuityObjective(BaseModel):
    objective_id: str
    service_id: str
    objective_class: ContinuityObjectiveClass
    rto: Optional[RtoTarget] = None
    rpo: Optional[RpoTarget] = None
    description: str

class ContinuityService(BaseModel):
    service_id: str
    service_class: ContinuityServiceClass
    owner: str
    dependencies: List[str] = Field(default_factory=list)
    description: str

class BackupPolicy(BaseModel):
    policy_id: str
    service_id: str
    backup_class: BackupClass
    frequency_seconds: int
    retention_days: int
    is_encrypted: bool
    requires_verification: bool

class SnapshotRecord(BaseModel):
    snapshot_id: str
    service_id: str
    snapshot_class: SnapshotClass
    timestamp: datetime
    is_complete: bool
    is_stale: bool
    lineage_ref: str

class ReplicationRecord(BaseModel):
    replication_id: str
    service_id: str
    replication_class: ReplicationClass
    lag_seconds: int
    is_healthy: bool
    lineage_ref: str

class RestoreRecord(BaseModel):
    restore_id: str
    service_id: str
    snapshot_id: str
    restore_class: RestoreClass
    timestamp: datetime
    is_successful: bool
    actor: str

class RestoreVerificationRecord(BaseModel):
    verification_id: str
    restore_id: str
    is_verified: bool
    details: str
    timestamp: datetime

class FailoverRecord(BaseModel):
    failover_id: str
    service_id: str
    failover_class: FailoverClass
    timestamp: datetime
    is_successful: bool
    actor: str

class FailbackRecord(BaseModel):
    failback_id: str
    service_id: str
    failback_class: FailbackClass
    timestamp: datetime
    is_successful: bool
    actor: str

class StandbyModeRecord(BaseModel):
    service_id: str
    standby_class: StandbyClass
    is_fresh: bool
    compatibility_drift: bool
    last_checked: datetime

class ContinuityExposureRecord(BaseModel):
    exposure_id: str
    service_id: str
    exposure_type: str
    severity: str
    description: str
    timestamp: datetime

class SplitBrainRiskRecord(BaseModel):
    risk_id: str
    service_id: str
    risk_type: str
    severity: str
    description: str
    timestamp: datetime

class ContinuityStateSnapshot(BaseModel):
    service_id: str
    state: str
    timestamp: datetime

class ContinuityForecastReport(BaseModel):
    service_id: str
    forecast_type: str
    uncertainty_class: str
    description: str

class ContinuityIncidentLink(BaseModel):
    incident_id: str
    service_id: str
    link_type: str

class ContinuityDebtRecord(BaseModel):
    debt_id: str
    service_id: str
    description: str
    severity: str

class ContinuityEquivalenceReport(BaseModel):
    service_id: str
    verdict: ContinuityEquivalenceVerdict
    divergence_details: Optional[str] = None
    timestamp: datetime

class ContinuityDivergenceReport(BaseModel):
    service_id: str
    divergence_source: str
    severity: str
    description: str
    timestamp: datetime

class ContinuityTrustVerdict(BaseModel):
    service_id: str
    verdict: ContinuityTrustVerdict
    factors: Dict[str, Any]
    timestamp: datetime

class ContinuityAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    details: str
    timestamp: datetime

class ContinuityArtifactManifest(BaseModel):
    manifest_id: str
    service_id: str
    refs: Dict[str, str]
    timestamp: datetime

class ContinuityPlaneConfig(BaseModel):
    enabled: bool = True
    strict_verification: bool = True
