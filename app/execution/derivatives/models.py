from pydantic import BaseModel, Field
from typing import Optional, List
from .enums import (
    DerivativeSide,
    LeverageAction,
    ReduceOnlyVerdict,
    MarginCallSeverity,
    LiquidationProximity,
    FundingDirection,
    BorrowState
)
from app.products.enums import ProductType, MarginMode, PositionMode

class DerivativeExecutionIntent(BaseModel):
    product_type: ProductType
    symbol: str
    side: DerivativeSide
    quantity: float
    price: Optional[float] = None
    is_reduce_only: bool = False

class LeverageRequest(BaseModel):
    product_type: ProductType
    symbol: str
    requested_leverage: int

class MarginModeRequest(BaseModel):
    product_type: ProductType
    symbol: str
    requested_mode: MarginMode

class PositionModeRequest(BaseModel):
    product_type: ProductType
    requested_mode: PositionMode

class ReduceOnlyExecutionRequest(BaseModel):
    intent: DerivativeExecutionIntent
    current_position_qty: float

class DerivativeOrderFlags(BaseModel):
    reduce_only: bool = False
    close_position: bool = False

class LiquidationSnapshot(BaseModel):
    symbol: str
    current_price: float
    liquidation_price: Optional[float]
    distance_pct: float
    proximity: LiquidationProximity

class MaintenanceMarginSnapshot(BaseModel):
    symbol: str
    maintenance_margin: float
    margin_balance: float
    margin_ratio: float
    severity: MarginCallSeverity

class FundingSnapshot(BaseModel):
    symbol: str
    funding_rate: float
    next_funding_time: int
    direction: FundingDirection
    estimated_cost: float

class BorrowSnapshot(BaseModel):
    asset: str
    borrowed_amount: float
    interest_rate: float
    state: BorrowState

class CarryCostSnapshot(BaseModel):
    product_type: ProductType
    symbol: str
    total_accrued_cost: float
    funding_snapshot: Optional[FundingSnapshot] = None
    borrow_snapshot: Optional[BorrowSnapshot] = None

class DerivativeExecutionAudit(BaseModel):
    run_id: str
    intent: DerivativeExecutionIntent
    verdict: ReduceOnlyVerdict
    leverage_snapshot: int
    liquidation_snapshot: Optional[LiquidationSnapshot] = None
    timestamp: float

class DerivativeSessionSummary(BaseModel):
    run_id: str
    product_type: ProductType
    realized_pnl: float
    total_carry_costs: float
    max_leverage_used: int
    liquidation_warnings_count: int
