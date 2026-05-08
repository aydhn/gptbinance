from enum import Enum


class PositionClass(Enum):
    SPOT = "spot"
    MARGIN = "margin"
    FUTURES = "futures"


class ProductClass(Enum):
    PERPETUAL = "perpetual"
    QUARTERLY = "quarterly"
    SPOT_PAIR = "spot_pair"
    MARGIN_PAIR = "margin_pair"


class Side(Enum):
    LONG = "long"
    SHORT = "short"
    FLAT = "flat"


class LifecycleState(Enum):
    FLAT = "flat"
    OPENING = "opening"
    OPEN = "open"
    SCALING_IN = "scaling_in"
    SCALING_OUT = "scaling_out"
    REVERSING = "reversing"
    CLOSED = "closed"
    DUST_RESIDUAL = "dust_residual"
    HEDGED_OPEN = "hedged_open"


class PnlComponent(Enum):
    REALIZED_PRICE_MOVE = "realized_price_move"
    UNREALIZED_PRICE_MOVE = "unrealized_price_move"
    MAKER_FEE = "maker_fee"
    TAKER_FEE = "taker_fee"
    FUNDING_INCOME = "funding_income"
    FUNDING_EXPENSE = "funding_expense"
    CARRY_COST = "carry_cost"
    SLIPPAGE_BURDEN = "slippage_burden"


class ExposureClass(Enum):
    GROSS = "gross"
    NET_DIRECTIONAL = "net_directional"
    HEDGE_ADJUSTED = "hedge_adjusted"
    RESIDUAL_DIRECTIONAL = "residual_directional"


class DivergenceSeverity(Enum):
    NONE = "none"
    MINOR_DUST = "minor_dust"
    COST_BASIS_MISMATCH = "cost_basis_mismatch"
    QUANTITY_MISMATCH = "quantity_mismatch"
    MISSING_LOT = "missing_lot"
    STALE_STATE = "stale_state"
    CRITICAL = "critical"


class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"


class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class CostBasisClass(Enum):
    WEIGHTED_AVERAGE = "weighted_average"
    FIFO_LOT = "fifo_lot"
    LIFO_LOT = "lifo_lot"
    SPECIFIC_LOT = "specific_lot"
