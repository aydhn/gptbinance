"""
models.py
"""
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

from app.crossbook.enums import (
    BookType,
    MarginMode,
    ExposureClass,
    HedgeQuality,
    ConflictSeverity,
    LiquidationSensitivity,
    FundingBurdenClass,
    BorrowDependencyClass,
    CrossBookVerdict,
    OverlayReasonType,
)


class CrossBookConfig(BaseModel):
    max_combined_directional_exposure: float = 100000.0
    max_combined_leverage_impression: float = 5.0
    stale_snapshot_threshold_seconds: int = 60


class BookPositionRef(BaseModel):
    book_type: BookType
    symbol: str
    asset: str
    quantity: float
    notional: float
    is_borrowed: bool = False
    margin_mode: MarginMode = MarginMode.NONE
    metadata: Dict[str, Any] = Field(default_factory=dict)


class UnifiedExposureNode(BaseModel):
    node_id: str
    asset: str
    positions: List[BookPositionRef]
    total_quantity: float
    total_notional: float


class UnifiedExposureEdge(BaseModel):
    source_id: str
    target_id: str
    edge_type: str
    weight: float = 1.0


class ExposureGraphModel(BaseModel):
    nodes: Dict[str, UnifiedExposureNode]
    edges: List[UnifiedExposureEdge]
    timestamp: datetime


class FakeHedgeFinding(BaseModel):
    asset: str
    reason: str
    severity: ConflictSeverity


class CollateralDependency(BaseModel):
    asset: str
    locked_amount: float
    usable_amount: float
    is_cross: bool


class CollateralPressureReport(BaseModel):
    total_locked: float
    total_usable: float
    pressure_ratio: float
    dependencies: List[CollateralDependency]


class BorrowDependencyReport(BaseModel):
    borrowed_assets: Dict[str, float]
    dependency_class: BorrowDependencyClass
    total_borrow_value: float


class FundingBurdenOverlay(BaseModel):
    burden_class: FundingBurdenClass
    symbols: List[str]
    total_expected_drag: float


class BasisExposureReport(BaseModel):
    asset: str
    basis_spread: float
    is_widening: bool


class CrossBookConflict(BaseModel):
    conflict_type: OverlayReasonType
    severity: ConflictSeverity
    asset: str
    evidence: str


class LiquidationSensitivityReport(BaseModel):
    sensitivity: LiquidationSensitivity
    contagion_risk_assets: List[str]
    unwind_pressure: float


class DirectionalExposure(BaseModel):
    long_notional: float
    short_notional: float
    net_notional: float


class NetAssetExposure(BaseModel):
    asset: str
    directional: DirectionalExposure
    exposure_class: ExposureClass
    hedge_quality: HedgeQuality


class NetExposureSnapshot(BaseModel):
    snapshot_id: str
    timestamp: datetime
    assets: Dict[str, NetAssetExposure]
    total_gross_notional: float
    total_net_notional: float


class CrossBookOverlayDecision(BaseModel):
    verdict: CrossBookVerdict
    reasons: List[str]
    conflicts: List[CrossBookConflict]
    timestamp: datetime


class CrossBookAuditRecord(BaseModel):
    record_id: str
    timestamp: datetime
    action: str
    details: Dict[str, Any]


class CrossBookArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime
    refs: List[str]
