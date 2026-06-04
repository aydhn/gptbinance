from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime
from app.renewal_plane.enums import *

class RenewalPlaneConfig(BaseModel):
    strict_evidence_freshness: bool = True
    forbid_indefinite_extensions: bool = True

class RenewalObject(BaseModel):
    renewal_id: str
    renewal_class: RenewalClass
    owner: str
    scope: str
    continuation_posture: ContinuationClass
    reauthorization_posture: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class RenewalObjectRef(BaseModel):
    renewal_id: str

class RenewalRecord(BaseModel):
    record_id: str
    renewal_id: str
    status: str

class RenewalTriggerRecord(BaseModel):
    trigger_id: str
    renewal_id: str
    trigger_class: TriggerClass

class RenewalIntervalRecord(BaseModel):
    interval_id: str
    interval_class: IntervalClass

class RenewalCriteriaRecord(BaseModel):
    criteria_id: str
    criteria_class: CriteriaClass

class EvidenceFreshnessRecord(BaseModel):
    freshness_id: str
    state: EvidenceFreshness

class ReauthorizationRecord(BaseModel):
    reauth_id: str
    type: str

class RecharterRecord(BaseModel):
    recharter_id: str
    type: str

class ExtensionRecord(BaseModel):
    extension_id: str
    type: str

class ProvisionalContinuationRecord(BaseModel):
    prov_id: str
    type: str

class ConditionalContinuationRecord(BaseModel):
    cond_id: str
    type: str

class RenewalRefusalRecord(BaseModel):
    refusal_id: str

class NonRenewalRecord(BaseModel):
    non_renewal_id: str
    type: NonRenewalClass

class ExpiryRecord(BaseModel):
    expiry_id: str

class RenewalDebtRecord(BaseModel):
    debt_id: str
    debt_class: RenewalDebtClass

class RenewalDriftRecord(BaseModel):
    drift_id: str
    drift_class: RenewalDriftClass

class RenewalDowngradeRecord(BaseModel):
    downgrade_id: str

class RenewalRevocationRecord(BaseModel):
    revocation_id: str

class RenewalComparisonRecord(BaseModel):
    comparison_id: str

class RenewalObservationReport(BaseModel):
    report_id: str

class RenewalForecastReport(BaseModel):
    forecast_id: str

class RenewalEquivalenceReport(BaseModel):
    equivalence_id: str
    verdict: EquivalenceVerdict

class RenewalDivergenceReport(BaseModel):
    divergence_id: str

class RenewalTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict

class RenewalAuditRecord(BaseModel):
    audit_id: str

class RenewalArtifactManifest(BaseModel):
    manifest_id: str
