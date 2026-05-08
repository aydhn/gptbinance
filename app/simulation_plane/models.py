from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime
from app.simulation_plane.enums import (
    SimulationClass,
    SimulationMode,
    PartitionClass,
    SensitivityClass,
    OOSClass,
    WalkForwardClass,
    EquivalenceVerdict,
    TrustVerdict,
)


class SimulationPlaneConfig(BaseModel):
    enabled: bool = True
    require_assumption_manifests: bool = True


class SimulationWindow(BaseModel):
    start_time: datetime
    end_time: datetime
    window_type: str = "fixed"  # fixed, rolling, anchored
    caveats: List[str] = Field(default_factory=list)


class SimulationPartition(BaseModel):
    partition_id: str
    partition_class: PartitionClass
    window: SimulationWindow
    caveats: List[str] = Field(default_factory=list)


class FillAssumption(BaseModel):
    model_type: str  # touch, partial, no-fill
    caveats: List[str] = Field(default_factory=list)


class SlippageAssumption(BaseModel):
    model_type: str  # fixed_bps, volatility_aware
    value: float
    caveats: List[str] = Field(default_factory=list)


class LatencyAssumption(BaseModel):
    model_type: str
    decision_to_order_ms: int
    caveats: List[str] = Field(default_factory=list)


class FeeFundingAssumption(BaseModel):
    includes_fees: bool
    includes_funding: bool
    caveats: List[str] = Field(default_factory=list)


class OrderLegalityAssumption(BaseModel):
    enforces_filters: bool
    caveats: List[str] = Field(default_factory=list)


class AssumptionManifest(BaseModel):
    manifest_id: str
    fill: FillAssumption
    slippage: SlippageAssumption
    latency: LatencyAssumption
    fee_funding: FeeFundingAssumption
    legality: OrderLegalityAssumption
    caveats: List[str] = Field(default_factory=list)


class SimulationDefinition(BaseModel):
    sim_id: str
    sim_class: SimulationClass
    mode: SimulationMode
    strategy_ref: str
    data_refs: List[str]
    description: str


class SimulationRef(BaseModel):
    sim_id: str
    version: str


class SimulationRun(BaseModel):
    run_id: str
    sim_ref: SimulationRef
    window: SimulationWindow
    partitions: List[SimulationPartition]
    assumption_manifest_id: str
    created_at: datetime


class SimulationRunRef(BaseModel):
    run_id: str


class SimulationResult(BaseModel):
    run_id: str
    total_return: float
    max_drawdown: float
    metrics: Dict[str, float]
    caveats: List[str] = Field(default_factory=list)


class SimulationSensitivityReport(BaseModel):
    run_id: str
    sensitivities: Dict[SensitivityClass, str]
    caveats: List[str] = Field(default_factory=list)


class WalkForwardReport(BaseModel):
    run_id: str
    wf_class: WalkForwardClass
    fold_results: List[Dict[str, Any]]
    caveats: List[str] = Field(default_factory=list)


class OOSReport(BaseModel):
    run_id: str
    oos_class: OOSClass
    leakage_checks_passed: bool
    caveats: List[str] = Field(default_factory=list)


class SimulationEquivalenceReport(BaseModel):
    run_id: str
    compare_to_mode: SimulationMode
    verdict: EquivalenceVerdict
    divergence_sources: List[str]
    caveats: List[str] = Field(default_factory=list)


class SimulationTrustVerdict(BaseModel):
    run_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    caveats: List[str] = Field(default_factory=list)


class SimulationAuditRecord(BaseModel):
    record_id: str
    run_id: str
    timestamp: datetime
    action: str
    details: Dict[str, Any]


class SimulationArtifactManifest(BaseModel):
    manifest_id: str
    run_id: str
    artifacts: Dict[str, str]
