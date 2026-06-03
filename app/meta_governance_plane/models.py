from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.meta_governance_plane.enums import (
    MetaGovernanceClass, ProposalClass, CanonClass, VersionClass, SupersessionClass,
    DeprecationClass, CompatibilityClass, MigrationClass, ConflictClass,
    MetaGovernanceTrustVerdict, MetaGovernanceEquivalenceVerdict
)

class MetaGovernancePlaneConfig(BaseModel):
    strict_lineage_enforcement: bool = True

class MetaGovernanceObjectRef(BaseModel):
    meta_governance_id: str
    class_name: str

class MetaGovernanceObject(BaseModel):
    meta_governance_id: str
    object_class: MetaGovernanceClass
    owner: str
    scope: str
    canon_posture: str
    migration_posture: str

class MetaGovernanceRecord(BaseModel):
    meta_governance_id: str
    status: str

class GovernanceProposalRecord(BaseModel):
    proposal_id: str
    proposal_class: ProposalClass
    target_canon_id: str
    proposed_by: str

class CanonRecord(BaseModel):
    canon_id: str
    canon_class: CanonClass

class CanonVersionRecord(BaseModel):
    version_id: str
    canon_id: str
    version_class: VersionClass

class RuleLineageRecord(BaseModel):
    lineage_id: str
    canon_id: str
    history: List[str]

class SupersessionRecord(BaseModel):
    supersession_id: str
    old_version_id: str
    new_version_id: str
    supersession_class: SupersessionClass

class DeprecationRecord(BaseModel):
    deprecation_id: str
    canon_id: str
    deprecation_class: DeprecationClass
    sunset_date: Optional[datetime]

class CompatibilityWindowRecord(BaseModel):
    window_id: str
    canon_id: str
    compatibility_class: CompatibilityClass

class GovernanceMigrationRecord(BaseModel):
    migration_id: str
    canon_id: str
    migration_class: MigrationClass

class DependencyMapRecord(BaseModel):
    map_id: str
    canon_id: str
    dependencies: List[str]

class ExceptionRecord(BaseModel):
    exception_id: str
    canon_id: str
    justification: str

class EmergencyPatchRecord(BaseModel):
    patch_id: str
    canon_id: str
    is_active: bool

class ShadowCanonRecord(BaseModel):
    shadow_id: str
    suspected_canon: str

class RuntimeDivergenceRecord(BaseModel):
    divergence_id: str
    canon_id: str

class ConstitutionalConflictRecord(BaseModel):
    conflict_id: str
    conflict_class: ConflictClass

class HistoricalPreservationRecord(BaseModel):
    preservation_id: str
    canon_id: str
    is_preserved: bool

class MetaGovernanceComparisonRecord(BaseModel):
    comparison_id: str

class MetaGovernanceObservationReport(BaseModel):
    report_id: str

class MetaGovernanceForecastReport(BaseModel):
    forecast_id: str

class MetaGovernanceDebtRecord(BaseModel):
    debt_id: str
    amount: float

class MetaGovernanceEquivalenceReport(BaseModel):
    report_id: str
    verdict: MetaGovernanceEquivalenceVerdict

class MetaGovernanceDivergenceReport(BaseModel):
    report_id: str

class MetaGovernanceTrustVerdictRecord(BaseModel):
    verdict_id: str
    verdict: MetaGovernanceTrustVerdict

class MetaGovernanceAuditRecord(BaseModel):
    audit_id: str

class MetaGovernanceArtifactManifest(BaseModel):
    manifest_id: str
