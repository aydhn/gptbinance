from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime

from app.research.regime.enums import (
    RegimeFamily,
    TransitionType,
    SuitabilityVerdict,
    ContextQuality,
)


class RegimeLabel(BaseModel):
    family: RegimeFamily
    name: str  # The specific regime enum name, e.g. STRONG_UPTREND


class RegimeScore(BaseModel):
    score: float = Field(..., ge=0.0, le=1.0)
    confidence: float = Field(..., ge=0.0, le=1.0)


class RegimeQualityReport(BaseModel):
    quality: ContextQuality
    warnings: List[str] = Field(default_factory=list)
    stability_score: float = Field(
        ..., ge=0.0, le=1.0
    )  # 1.0 means highly stable over recent history


class RegimeEvaluationResult(BaseModel):
    timestamp: datetime
    label: RegimeLabel
    score: RegimeScore
    quality: RegimeQualityReport
    rationale: str
    feature_contributions: Dict[str, float] = Field(default_factory=dict)


class RegimeTransition(BaseModel):
    timestamp: datetime
    from_label: RegimeLabel
    to_label: RegimeLabel
    transition_type: TransitionType
    transition_strength: float = Field(..., ge=0.0, le=1.0)
    rationale: str


class StrategyRegimeCompatibility(BaseModel):
    strategy_family: str
    verdict: SuitabilityVerdict
    suitability_score: float = Field(..., ge=0.0, le=1.0)
    rationale: str


class RegimeSuitabilityMap(BaseModel):
    timestamp: datetime
    symbol: str
    interval: str
    compatibilities: Dict[str, StrategyRegimeCompatibility]


class RegimeContext(BaseModel):
    timestamp: datetime
    symbol: str
    interval: str
    evaluations: Dict[RegimeFamily, RegimeEvaluationResult]
    transitions: Dict[RegimeFamily, Optional[RegimeTransition]]
    suitability: Optional[RegimeSuitabilityMap] = None
    overall_quality: ContextQuality


class MultiTimeframeRegimeContext(BaseModel):
    timestamp: datetime
    symbol: str
    base_interval: str
    contexts: Dict[str, RegimeContext]  # key is interval
    consistency_score: float = Field(..., ge=0.0, le=1.0)
    contradiction_warnings: List[str] = Field(default_factory=list)


class RegimeSnapshot(BaseModel):
    timestamp: datetime
    symbol: str
    interval: str
    context: RegimeContext
    mtf_context: Optional[MultiTimeframeRegimeContext] = None


class RegimeFeatureBundle(BaseModel):
    timestamp: datetime
    symbol: str
    interval: str
    features: Dict[str, Any]


class RegimeHistoryWindow(BaseModel):
    symbol: str
    interval: str
    snapshots: List[RegimeSnapshot]
