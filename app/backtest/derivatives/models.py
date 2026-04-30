from pydantic import BaseModel
from typing import Optional
from app.products.enums import ProductType

class DerivativeBacktestConfig(BaseModel):
    product_type: ProductType
    initial_margin: float
    maintenance_margin_rate: float = 0.005
    hourly_funding_rate: float = 0.0001
    hourly_borrow_rate: float = 0.00005

class FundingEvent(BaseModel):
    timestamp: float
    symbol: str
    amount: float

class BorrowCostEvent(BaseModel):
    timestamp: float
    asset: str
    amount: float

class DerivativeTradeRecord(BaseModel):
    timestamp: float
    symbol: str
    side: str
    quantity: float
    price: float
    realized_pnl: float
    leverage: int

class DerivativePnlAdjustment(BaseModel):
    timestamp: float
    total_funding_paid: float
    total_borrow_paid: float
    net_pnl_after_costs: float
