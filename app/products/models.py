from pydantic import BaseModel, Field
from typing import Optional, List
from .enums import (
    ProductType,
    MarginMode,
    PositionMode,
    ProductReadiness,
    SettlementType,
)


class ProductTradingCapabilities(BaseModel):
    supports_short: bool = False
    supports_leverage: bool = False
    max_leverage: int = 1
    supported_margin_modes: List[MarginMode] = Field(default_factory=list)
    supported_position_modes: List[PositionMode] = Field(default_factory=list)


class ProductRiskDescriptor(BaseModel):
    liquidation_risk_enabled: bool = False
    funding_risk_enabled: bool = False
    borrow_risk_enabled: bool = False
    reduce_only_required_on_flatten: bool = False


class ProductExecutionConstraints(BaseModel):
    min_notional: float = 0.0
    step_size: float = 0.0
    tick_size: float = 0.0


class ProductCostModel(BaseModel):
    has_funding_fee: bool = False
    has_borrow_interest: bool = False
    estimated_daily_carry_bps: float = 0.0


class ProductDescriptor(BaseModel):
    product_type: ProductType
    readiness: ProductReadiness
    capabilities: ProductTradingCapabilities
    risk: ProductRiskDescriptor
    constraints: ProductExecutionConstraints
    cost_model: ProductCostModel


class SpotProductConfig(BaseModel):
    allowed_quote_assets: List[str] = ["USDT", "USDC"]


class MarginProductConfig(BaseModel):
    default_margin_mode: MarginMode = MarginMode.ISOLATED
    max_allowed_leverage: int = 3
    auto_borrow: bool = False
    auto_repay: bool = False


class FuturesProductConfig(BaseModel):
    default_margin_mode: MarginMode = MarginMode.ISOLATED
    default_position_mode: PositionMode = PositionMode.ONE_WAY
    max_allowed_leverage: int = 5
    settlement: SettlementType = SettlementType.CASH


class ProductModeSnapshot(BaseModel):
    product_type: ProductType
    current_leverage: int
    current_margin_mode: Optional[MarginMode]
    current_position_mode: Optional[PositionMode]
