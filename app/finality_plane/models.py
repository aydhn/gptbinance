from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.finality_plane.enums import (
    FinalityClass, ClosureClass, SettlementClass, TerminalityClass,
    ReopenClass, AppealClass, DisputeClass, SupersessionClass,
    RetirementClass, IrreversibilityClass, FinalityTrustVerdictClass
)

class FinalityObjectRef(BaseModel):
    finality_id: str

class FinalityObject(BaseModel):
    finality_id: str
    finality_class: FinalityClass
    owner: str
    scope: str
    closure_posture: str
    reopen_posture: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ClosureBasisRecord(BaseModel):
    basis_id: str
    finality_id: str
    basis_type: str
    caveats: str
    proof_notes: str

class ClosureRecord(BaseModel):
    closure_id: str
    finality_id: str
    closure_class: ClosureClass
    notes: str

class ProvisionalClosureRecord(ClosureRecord):
    observation_pending: bool = False
    compensation_pending: bool = False
    appeal_window_open: bool = False
    caveats: str

class ConditionalClosureRecord(ClosureRecord):
    condition: str
    trigger_refs: List[str]

class FinalClosureRecord(ClosureRecord):
    authoritative: bool
    operational: bool
    legal: bool
    proof_notes: str

class SettlementRecord(BaseModel):
    settlement_id: str
    finality_id: str
    settlement_class: SettlementClass
    caveats: str

class TerminalStateRecord(BaseModel):
    terminal_id: str
    finality_id: str
    terminality_class: TerminalityClass
    proof_notes: str

class IrreversibilityRecord(BaseModel):
    irreversibility_id: str
    finality_id: str
    irreversibility_class: IrreversibilityClass
    caveats: str

class ReopenRecord(BaseModel):
    reopen_id: str
    finality_id: str
    reopen_class: ReopenClass
    notes: str

class ReopenRightRecord(BaseModel):
    right_id: str
    finality_id: str
    actor_scoped: str
    window_bounded: str
    exhausted: bool
    caveats: str

class ReopenTriggerRecord(BaseModel):
    trigger_id: str
    finality_id: str
    trigger_type: str
    proof_notes: str

class AppealRecord(BaseModel):
    appeal_id: str
    finality_id: str
    appeal_class: AppealClass
    caveats: str

class DisputeRecord(BaseModel):
    dispute_id: str
    finality_id: str
    dispute_class: DisputeClass
    suppression_warning: bool

class SupersessionRecord(BaseModel):
    supersession_id: str
    finality_id: str
    supersession_class: SupersessionClass
    scope_notes: str

class RetirementRecord(BaseModel):
    retirement_id: str
    finality_id: str
    retirement_class: RetirementClass
    caveats: str

class CompensationSettlementRecord(BaseModel):
    compensation_id: str
    finality_id: str
    remedy: str
    sufficiency_notes: str

class ResidualObligationRecord(BaseModel):
    obligation_id: str
    finality_id: str
    duty: str
    pending: bool

class ResidualRiskRecord(BaseModel):
    risk_id: str
    finality_id: str
    risk_type: str
    bounded: bool

class FinalityComparisonRecord(BaseModel):
    comparison_id: str
    finality_id_a: str
    finality_id_b: str
    notes: str

class FinalityTrustVerdict(BaseModel):
    verdict: FinalityTrustVerdictClass
    finality_id: str
    closure_basis_strength: str
    reopen_clarity: str
    settlement_rigor: str
    residual_duty_visibility: str
    caveats: List[str]
    blockers: List[str]

class FinalityForecastReport(BaseModel):
    finality_id: str
    reopen_likelihood: str
    appeal_likelihood: str
    premature_closure: bool
    supersession_pressure: str

class FinalityDebtRecord(BaseModel):
    debt_id: str
    finality_id: str
    debt_type: str
    severity: str

class FinalityEquivalenceReport(BaseModel):
    finality_id: str
    environments_compared: List[str]
    equivalence_verdict: str
    blockers: List[str]

class FinalityDivergenceReport(BaseModel):
    finality_id: str
    divergence_type: str
    severity: str
    blast_radius: str

class FinalityManifest(BaseModel):
    finality_id: str
    closures: List[ClosureRecord]
    settlements: List[SettlementRecord]
    reopens: List[ReopenRecord]
    appeals: List[AppealRecord]
    supersessions: List[SupersessionRecord]
    residuals: List[ResidualObligationRecord]
    trust_verdict: Optional[FinalityTrustVerdict]
    generated_at: datetime = Field(default_factory=datetime.utcnow)
