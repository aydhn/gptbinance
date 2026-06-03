from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.sunset_plane.enums import (
    SunsetClass, TriggerClass, CriteriaClass, DecommissionClass,
    ArchiveClass, DeletionClass, TombstoneClass, ObligationClass,
    AfterlifeClass, SunsetEquivalenceVerdictEnum, SunsetTrustVerdictEnum
)

class SunsetPlaneConfig(BaseModel):
    enforce_strict_sunset_governance: bool = True
    allow_symbolic_retirement: bool = False
    require_archival_integrity: bool = True

class SunsetObjectRef(BaseModel):
    sunset_id: str
    version: Optional[str] = "1.0"

class SunsetObject(BaseModel):
    sunset_id: str
    sunset_class: SunsetClass
    owner: str
    scope: str
    exit_posture: str
    afterlife_posture: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SunsetRecord(BaseModel):
    record_id: str
    sunset_id: str
    status: str
    proof_notes: str
    lineage_refs: List[str]

class RetirementTriggerRecord(BaseModel):
    trigger_id: str
    sunset_id: str
    trigger_class: TriggerClass
    basis: str
    lineage_refs: List[str]

class ExitCriteriaRecord(BaseModel):
    criteria_id: str
    sunset_id: str
    criteria_class: CriteriaClass
    details: str
    lineage_refs: List[str]

class DecommissionPlanRecord(BaseModel):
    plan_id: str
    sunset_id: str
    plan_class: DecommissionClass
    details: str
    lineage_refs: List[str]

class DependencyDisentanglementRecord(BaseModel):
    disentanglement_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class BeneficiaryNoticeRecord(BaseModel):
    notice_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class StakeholderNoticeRecord(BaseModel):
    notice_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class ArchiveRecord(BaseModel):
    archive_id: str
    sunset_id: str
    archive_class: ArchiveClass
    lineage_refs: List[str]

class ArchiveIntegrityRecord(BaseModel):
    integrity_id: str
    archive_id: str
    status: str
    lineage_refs: List[str]

class DataRetentionRecord(BaseModel):
    retention_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class DataDeletionRecord(BaseModel):
    deletion_id: str
    sunset_id: str
    deletion_class: DeletionClass
    lineage_refs: List[str]

class TombstoneRecord(BaseModel):
    tombstone_id: str
    sunset_id: str
    tombstone_class: TombstoneClass
    lineage_refs: List[str]

class FailbackWindowRecord(BaseModel):
    failback_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class SafeShutdownRecord(BaseModel):
    shutdown_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class ResidualObligationRecord(BaseModel):
    obligation_id: str
    sunset_id: str
    obligation_class: ObligationClass
    details: str
    lineage_refs: List[str]

class AccessWithdrawalRecord(BaseModel):
    withdrawal_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class CredentialRevocationRecord(BaseModel):
    revocation_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class ZombieRiskRecord(BaseModel):
    zombie_id: str
    sunset_id: str
    risk_level: str
    details: str
    lineage_refs: List[str]

class GhostDependencyRecord(BaseModel):
    ghost_id: str
    sunset_id: str
    status: str
    lineage_refs: List[str]

class SunsetComparisonRecord(BaseModel):
    comparison_id: str
    sunset_id: str
    details: str
    lineage_refs: List[str]

class SunsetObservationReport(BaseModel):
    report_id: str
    sunset_id: str
    observations: List[str]

class SunsetForecastReport(BaseModel):
    forecast_id: str
    sunset_id: str
    forecasts: List[str]

class SunsetDebtRecord(BaseModel):
    debt_id: str
    sunset_id: str
    severity: str
    details: str

class SunsetEquivalenceReport(BaseModel):
    report_id: str
    verdict: SunsetEquivalenceVerdictEnum
    divergence_sources: List[str]

class SunsetDivergenceReport(BaseModel):
    report_id: str
    severity: str
    blast_radius: str

class SunsetTrustVerdict(BaseModel):
    sunset_id: str
    verdict: SunsetTrustVerdictEnum
    factors: Dict[str, str]

class SunsetAuditRecord(BaseModel):
    audit_id: str
    sunset_id: str
    event_type: str
    details: str

class SunsetArtifactManifest(BaseModel):
    manifest_id: str
    sunset_id: str
    refs: List[str]
    hash_values: Dict[str, str]
