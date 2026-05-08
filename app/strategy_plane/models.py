from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from app.strategy_plane.enums import (
    StrategyClass,
    StrategyFamily,
    LifecycleState,
    PromotionClass,
    FreezeClass,
    RetirementClass,
    FitClass,
    DecaySeverity,
    EquivalenceVerdict,
    TrustVerdict,
)


class StrategyRef(BaseModel):
    strategy_id: str
    version: str


class SignalContract(BaseModel):
    signal_id: str
    description: str
    expected_inputs: List[str]
    expected_semantics: str
    directionality: str


class DependencyContract(BaseModel):
    data_manifests: List[str]
    feature_manifests: List[str]
    model_manis: List[str]
    config_manifests: List[str]


class StrategyHypothesis(BaseModel):
    hypothesis_id: str
    behavioral_claim: str
    expected_edge_reason: str
    expected_regimes: List[str]
    invalidation_conditions: List[str]
    lineage_refs: List[str]


class StrategyThesis(BaseModel):
    thesis_id: str
    version: str
    concrete_claim: str
    benchmark_expectations: Dict[str, Any]
    expected_drag_profile: str
    expected_failure_modes: List[str]
    expected_hold_time: str
    expected_regime_fit: List[str]
    proof_notes: str


class StrategyDefinition(BaseModel):
    strategy_id: str
    strategy_class: StrategyClass
    family: StrategyFamily
    hypothesis_ref: str
    thesis_ref: str
    signal_contracts: List[SignalContract]
    dependencies: DependencyContract
    is_production_grade: bool = False


class StrategyLifecycleRecord(BaseModel):
    strategy_id: str
    state: LifecycleState
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    reason: str
    evidence_refs: List[str]


class StrategyPromotionRecord(BaseModel):
    strategy_id: str
    from_state: LifecycleState
    to_state: LifecycleState
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    reason: str
    evidence_refs: List[str]
    promotion_class: PromotionClass


class StrategyFreezeRecord(BaseModel):
    strategy_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    reason: str
    freeze_class: FreezeClass
    evidence_refs: List[str]


class StrategyRetirementRecord(BaseModel):
    strategy_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    reason: str
    retirement_class: RetirementClass
    evidence_refs: List[str]


class StrategyFitReport(BaseModel):
    strategy_id: str
    regime_fit: FitClass
    sleeve_fit: FitClass
    liquidity_fit: FitClass
    risk_fit: FitClass
    notes: str


class StrategyDecayReport(BaseModel):
    strategy_id: str
    severity: DecaySeverity
    performance_decay: str
    capture_decay: str
    execution_drag_increase: str
    notes: str


class StrategyOverlapReport(BaseModel):
    strategy_id: str
    overlapping_strategies: List[str]
    severity: str
    notes: str


class StrategyEquivalenceReport(BaseModel):
    strategy_id: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str]
    notes: str


class StrategyTrustVerdict(BaseModel):
    strategy_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StrategyArtifactManifest(BaseModel):
    strategy_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    artifacts: List[str]


class StrategyAuditRecord(BaseModel):
    strategy_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    action: str
    details: str


class StrategyManifest(BaseModel):
    strategy_id: str
    definition: StrategyDefinition
    thesis: StrategyThesis
    lifecycle_state: LifecycleState
    trust_verdict: TrustVerdict
    manifest_hash: str


class StrategyPlaneConfig(BaseModel):
    enabled: bool = True
