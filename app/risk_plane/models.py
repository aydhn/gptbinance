from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
from .enums import (
    LimitClass,
    RiskDomain,
    DrawdownClass,
    MarginClass,
    LiquidationClass,
    BreachClass,
    ResponseClass,
    CooldownClass,
    EquivalenceVerdict,
    TrustVerdict,
)


class RiskLimitRef(BaseModel):
    limit_id: str
    limit_class: LimitClass
    owner_domain: str


class RiskStateRef(BaseModel):
    state_id: str
    domain: RiskDomain
    target_id: str


class RiskLimitDefinition(BaseModel):
    limit_id: str
    limit_class: LimitClass
    owner_domain: str
    domain: RiskDomain
    target_id: str
    value: float
    description: str


class DrawdownState(BaseModel):
    domain: RiskDomain
    target_id: str
    drawdown_class: DrawdownClass
    realized_drawdown: float
    unrealized_drawdown: float
    peak_value: float
    current_value: float
    reset_semantics: str
    proof_notes: List[str]


class LossState(BaseModel):
    domain: RiskDomain
    target_id: str
    realized_loss: float
    open_loss_burden: float
    session_loss: float
    evidence_refs: List[str]
    caveats: List[str]


class ConcentrationState(BaseModel):
    domain: RiskDomain
    target_id: str
    concentration_ratio: float
    clipping_reason: Optional[str] = None
    lineage_refs: List[str]


class MarginState(BaseModel):
    margin_class: MarginClass
    margin_usage_ratio: float
    usable_collateral: float
    collateral_fragility_ratio: float
    evidence_refs: List[str]
    proof_notes: List[str]


class LiquidationProximityState(BaseModel):
    liquidation_class: LiquidationClass
    proximity_ratio: float
    conservative_buffer: float
    stale_mark_caution: bool
    proof_notes: List[str]


class RiskState(BaseModel):
    state_id: str
    domain: RiskDomain
    target_id: str
    timestamp: datetime
    authoritative: bool
    source_position_refs: List[str]
    source_ledger_refs: List[str]
    source_market_truth_refs: List[str]
    drawdown: Optional[DrawdownState] = None
    loss: Optional[LossState] = None
    concentration: Optional[ConcentrationState] = None
    margin: Optional[MarginState] = None
    liquidation: Optional[LiquidationProximityState] = None
    completeness_summary: str


class RiskSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    states: Dict[str, RiskState]


class RiskBreachRecord(BaseModel):
    breach_id: str
    limit_ref: RiskLimitRef
    state_ref: RiskStateRef
    breach_class: BreachClass
    breached_value: float
    timestamp: datetime
    repeated_family: bool
    blast_radius: str
    proof_notes: List[str]


class RiskResponseIntent(BaseModel):
    intent_id: str
    response_class: ResponseClass
    source_breach_refs: List[str]
    target_domain: RiskDomain
    target_id: str
    rationale: str
    timestamp: datetime


class RiskCooldownRecord(BaseModel):
    cooldown_id: str
    cooldown_class: CooldownClass
    target_domain: RiskDomain
    target_id: str
    start_time: datetime
    end_time: datetime
    active: bool
    reason: str


class ReentryGate(BaseModel):
    gate_id: str
    target_domain: RiskDomain
    target_id: str
    requirements: List[str]
    cleared: bool
    proof_notes: List[str]


class RiskScenarioView(BaseModel):
    scenario_id: str
    description: str
    burden_summary: str
    evidence_refs: List[str]


class RiskEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    environments_compared: List[str]
    divergence_sources: List[str]
    proof_notes: List[str]


class RiskTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    breakdown: List[str]
    timestamp: datetime


class RiskArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    state_refs: List[str]
    limit_refs: List[str]
    breach_refs: List[str]
    response_refs: List[str]
    cooldown_refs: List[str]
    scenario_refs: List[str]
    hash_signature: str


class RiskPlaneConfig(BaseModel):
    enabled: bool = True
    default_cooldown_minutes: int = 60
    stale_state_threshold_seconds: int = 300
