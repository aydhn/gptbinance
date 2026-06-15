from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class ReliancePlaneConfig(BaseModel):
    enforce_strict_freshness: bool = True
    require_contradiction_cleanliness: bool = True
    fallback_paths_mandatory: bool = True

class RelianceObject(BaseModel):
    reliance_id: str
    class_name: str
    owner: str
    scope: str
    reliance_posture: str
    fallback_posture: str

class BaseRelianceRecord(BaseModel):
    record_id: str
    reliance_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class RelianceSubjectRecord(BaseRelianceRecord): pass
class RelianceConsumerRecord(BaseRelianceRecord): pass
class RelianceBasisRecord(BaseRelianceRecord): pass
class RelianceEligibilityRecord(BaseRelianceRecord): pass
class RelianceScopeRecord(BaseRelianceRecord): pass
class RelianceBoundaryRecord(BaseRelianceRecord): pass
class RelianceFreshnessRecord(BaseRelianceRecord): pass
class ValidityAwarenessRecord(BaseRelianceRecord): pass
class RevocationAwarenessRecord(BaseRelianceRecord): pass
class ContradictionAwarenessRecord(BaseRelianceRecord): pass
class DecisionUseRecord(BaseRelianceRecord): pass
class DependencyUseRecord(BaseRelianceRecord): pass
class CounterpartyRelianceRecord(BaseRelianceRecord): pass
class CompensatingReviewRecord(BaseRelianceRecord): pass
class FallbackPathRecord(BaseRelianceRecord): pass
class ProvisionalRelianceRecord(BaseRelianceRecord): pass
class EmergencyRelianceRecord(BaseRelianceRecord): pass
class DeniedRelianceRecord(BaseRelianceRecord): pass
class OverrelianceRecord(BaseRelianceRecord): pass
class MisrelianceRecord(BaseRelianceRecord): pass
class StaleRelianceRecord(BaseRelianceRecord): pass
class RevokedRelianceRecord(BaseRelianceRecord): pass
class OrphanRelianceRecord(BaseRelianceRecord): pass
class RelianceDebtRecord(BaseRelianceRecord): pass
class RelianceDriftRecord(BaseRelianceRecord): pass
class RelianceComparisonRecord(BaseRelianceRecord): pass
class RelianceObservationReport(BaseRelianceRecord): pass
class RelianceForecastReport(BaseRelianceRecord): pass
class RelianceEquivalenceReport(BaseRelianceRecord): pass
class RelianceDivergenceReport(BaseRelianceRecord): pass
class RelianceTrustVerdict(BaseRelianceRecord): pass
class RelianceAuditRecord(BaseRelianceRecord): pass
class RelianceArtifactManifest(BaseRelianceRecord): pass
