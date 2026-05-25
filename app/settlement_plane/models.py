from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.settlement_plane.enums import (
    SettlementClass, ReleaseClass, ReservationClass, CarveOutClass,
    ConsiderationClass, PerformanceClass, ClosureClass, DefaultClass,
    ReopenClass, SurvivalClass, EquivalenceVerdict, TrustVerdict
)

class SettlementObjectRef(BaseModel):
    id: str
    type: str
    version: int

class SettlementRecord(BaseModel):
    id: str
    settlement_class: SettlementClass
    owner: str
    scope_refs: List[str]
    release_refs: List[str]
    performance_refs: List[str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ReleaseRecord(BaseModel):
    id: str
    settlement_id: str
    release_class: ReleaseClass
    scope: str
    inflation_caution: bool = False

class CovenantRecord(BaseModel):
    id: str
    settlement_id: str
    covenant_type: str
    is_defective: bool = False

class ReservationRecord(BaseModel):
    id: str
    settlement_id: str
    reservation_class: ReservationClass
    description: str

class CarveOutRecord(BaseModel):
    id: str
    settlement_id: str
    carveout_class: CarveOutClass
    details: str

class ConsiderationRecord(BaseModel):
    id: str
    settlement_id: str
    consideration_class: ConsiderationClass
    value: Dict[str, Any]

class ConsiderationMilestoneRecord(BaseModel):
    id: str
    settlement_id: str
    milestone_type: str
    due_date: datetime

class StructuredPerformanceRecord(BaseModel):
    id: str
    settlement_id: str
    performance_class: PerformanceClass
    milestone_refs: List[str]

class InstallmentRecord(BaseModel):
    id: str
    settlement_id: str
    amount: float
    status: str

class AcceptanceRecord(BaseModel):
    id: str
    settlement_id: str
    status: str
    defects: List[str]

class AuthorityToSettleRecord(BaseModel):
    id: str
    settlement_id: str
    authority_type: str
    defects: List[str]

class ScopeRecord(BaseModel):
    id: str
    settlement_id: str
    issues: List[str]
    overreach_caution: bool

class BeneficiaryClosureRecord(BaseModel):
    id: str
    settlement_id: str
    beneficiary_id: str
    closure_type: str

class PartialClosureRecord(BaseModel):
    id: str
    settlement_id: str
    scope_refs: List[str]

class FullFinalClosureRecord(BaseModel):
    id: str
    settlement_id: str
    carveout_refs: List[str]

class ConditionalSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    conditions: List[str]

class ProvisionalSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    review_status: str

class BreachOfSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    breach_type: str

class RescissionRecord(BaseModel):
    id: str
    settlement_id: str
    status: str

class ReopenAfterSettlementRecord(BaseModel):
    id: str
    settlement_id: str
    reopen_class: ReopenClass

class SurvivalRecord(BaseModel):
    id: str
    settlement_id: str
    survival_class: SurvivalClass
    details: str

class SettlementComparisonRecord(BaseModel):
    id: str
    settlement_a: str
    settlement_b: str
    differences: Dict[str, Any]

class SettlementObservationReport(BaseModel):
    id: str
    observations: List[str]

class SettlementForecastReport(BaseModel):
    id: str
    predictions: Dict[str, float]

class SettlementDebtRecord(BaseModel):
    id: str
    settlement_id: str
    debt_type: str

class SettlementEquivalenceReport(BaseModel):
    id: str
    verdict: EquivalenceVerdict

class SettlementDivergenceReport(BaseModel):
    id: str
    divergences: List[str]

class SettlementTrustVerdict(BaseModel):
    id: str
    settlement_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class SettlementAuditRecord(BaseModel):
    id: str
    settlement_id: str
    action: str

class SettlementArtifactManifest(BaseModel):
    id: str
    settlement_id: str
    hashes: Dict[str, str]

class DefaultRecord(BaseModel):
    id: str
    settlement_id: str
    default_class: DefaultClass
    cured: bool = False
