from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from .enums import (
    BookType, MarginMode, CollateralType, ExposureClass,
    HedgeQuality, ConflictSeverity, LiquidationSensitivity,
    FundingBurdenClass, BorrowDependencyClass, CrossBookVerdict
)

class CrossBookConfig(BaseModel):
    enabled: bool = True
    max_combined_directional_exposure_usd: float = 50000.0
    max_borrow_dependency_ratio: float = 0.5

class BookPositionRef(BaseModel):
    book_type: BookType
    symbol: str
    amount: float
    margin_mode: MarginMode = MarginMode.NONE
    borrowed: float = 0.0
    collateral_locked: float = 0.0

class UnifiedExposureNode(BaseModel):
    id: str
    asset: str
    exposure_usd: float
    direction: int # 1 for long, -1 for short
    refs: List[BookPositionRef]

class UnifiedExposureEdge(BaseModel):
    source_id: str
    target_id: str
    relation_type: str # e.g. "hedges", "collateralizes"
    weight: float

class ExposureGraph(BaseModel):
    nodes: List[UnifiedExposureNode] = []
    edges: List[UnifiedExposureEdge] = []

class NetAssetExposure(BaseModel):
    asset: str
    gross_long: float
    gross_short: float
    net: float

class DirectionalExposure(BaseModel):
    total_long_usd: float
    total_short_usd: float
    net_directional_usd: float

class NetExposureSnapshot(BaseModel):
    timestamp: datetime
    assets: Dict[str, NetAssetExposure]
    directional: DirectionalExposure

class CrossBookConflict(BaseModel):
    conflict_type: str
    severity: ConflictSeverity
    description: str
    related_nodes: List[str]

class FakeHedgeFinding(BaseModel):
    asset: str
    apparent_hedge_ratio: float
    trusted_hedge_ratio: float
    quality: HedgeQuality
    reason: str

class CollateralDependency(BaseModel):
    asset: str
    locked_amount: float
    usable_amount: float
    pressure_ratio: float

class CollateralPressureReport(BaseModel):
    dependencies: List[CollateralDependency]
    overall_pressure: float
    warning: Optional[str]

class BorrowDependencyReport(BaseModel):
    total_borrowed_usd: float
    dependency_class: BorrowDependencyClass

class FundingBurdenOverlay(BaseModel):
    symbol: str
    expected_drag_usd_per_day: float
    burden_class: FundingBurdenClass

class BasisExposureReport(BaseModel):
    symbol: str
    spot_price: float
    futures_price: float
    basis_pct: float
    caution: Optional[str]

class LiquidationSensitivityReport(BaseModel):
    sensitivity: LiquidationSensitivity
    contagion_risk: bool
    notes: str

class CrossBookOverlayDecision(BaseModel):
    verdict: CrossBookVerdict
    reasons: List[str]

class CrossBookAuditRecord(BaseModel):
    timestamp: datetime
    decision: CrossBookOverlayDecision
    run_id: str

class CrossBookArtifactManifest(BaseModel):
    snapshot_id: str
    artifacts: List[str]
