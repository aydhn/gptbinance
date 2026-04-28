from pydantic import BaseModel, Field
from typing import Dict, List
from app.research.regime.enums import RegimeFamily


class RegimeEvaluatorSpec(BaseModel):
    name: str
    family: RegimeFamily
    description: str
    required_features: List[str]
    parameters: Dict[str, float] = Field(default_factory=dict)


class TrendPersistenceSpec(RegimeEvaluatorSpec):
    name: str = "trend_persistence_evaluator"
    family: RegimeFamily = RegimeFamily.TREND
    description: str = (
        "Evaluates trend strength and persistence based on momentum and MA alignment."
    )
    required_features: List[str] = ["trend_sma_fast", "trend_sma_slow", "momentum_rsi"]
    parameters: Dict[str, float] = {
        "strong_trend_threshold": 0.8,
        "weak_trend_threshold": 0.4,
    }


class VolatilityExpansionSpec(RegimeEvaluatorSpec):
    name: str = "volatility_expansion_evaluator"
    family: RegimeFamily = RegimeFamily.VOLATILITY
    description: str = "Evaluates if volatility is expanding, contracting or normal."
    required_features: List[str] = ["volatility_atr", "volatility_bb_width"]
    parameters: Dict[str, float] = {
        "expansion_threshold": 1.5,
        "low_energy_threshold": 0.5,
    }


class MeanReversionProneSpec(RegimeEvaluatorSpec):
    name: str = "mean_reversion_prone_evaluator"
    family: RegimeFamily = RegimeFamily.MEAN_REVERSION
    description: str = (
        "Evaluates if market is prone to mean reversion (overstretched or range-bound)."
    )
    required_features: List[str] = ["momentum_rsi", "price_to_sma_dist"]
    parameters: Dict[str, float] = {
        "overbought_threshold": 75.0,
        "oversold_threshold": 25.0,
    }


class StructureBreakoutSpec(RegimeEvaluatorSpec):
    name: str = "structure_breakout_evaluator"
    family: RegimeFamily = RegimeFamily.STRUCTURE
    description: str = "Evaluates price structure and breakout pressure."
    required_features: List[str] = ["close", "high", "low"]  # Will be expanded
    parameters: Dict[str, float] = {"pressure_threshold": 0.7}
