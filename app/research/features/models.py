from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.research.features.enums import (
    FeatureCategory,
    InputDataType,
    WindowMode,
    AlignmentMode,
    NormalizationMode,
    FeatureQualityStatus,
)


class WindowConfig(BaseModel):
    window_size: int
    min_periods: int = 1
    mode: WindowMode = WindowMode.ROLLING


class FeatureSpec(BaseModel):
    name: str
    category: FeatureCategory
    input_type: InputDataType = InputDataType.KLINE
    params: Dict[str, Any] = Field(default_factory=dict)
    window: Optional[WindowConfig] = None
    normalization: NormalizationMode = NormalizationMode.NONE


class MultiTimeframeFeatureSpec(BaseModel):
    base_spec: FeatureSpec
    target_timeframe: str
    alignment_mode: AlignmentMode = AlignmentMode.STRICT_CLOSED


class FeatureRequest(BaseModel):
    feature_set_name: str
    symbol: str
    interval: str
    specs: List[FeatureSpec | MultiTimeframeFeatureSpec]


class FeatureColumnMeta(BaseModel):
    column_name: str
    spec: FeatureSpec | MultiTimeframeFeatureSpec
    null_count: int = 0
    warmup_period: int = 0


class FeatureLineage(BaseModel):
    run_id: str
    timestamp: datetime
    feature_set_name: str
    symbol: str
    interval: str
    columns_meta: List[FeatureColumnMeta]
    source_data_hash: Optional[str] = None


class FeatureQualityReport(BaseModel):
    status: FeatureQualityStatus
    null_percentage: float
    warnings: List[str] = Field(default_factory=list)
    leakage_checks_passed: bool = True


class FeatureGenerationReport(BaseModel):
    lineage: FeatureLineage
    quality: FeatureQualityReport
    generation_time_ms: float


class FeatureSet(BaseModel):
    name: str
    report: FeatureGenerationReport
    # We don't store the actual dataframe here directly to keep the model lightweight,
    # The actual dataframe will be handled by the engine/storage
    storage_path: Optional[str] = None


class PivotPoint(BaseModel):
    index: int
    timestamp: int
    price: float
    type: str  # 'high' or 'low'


class DivergenceSignalCandidate(BaseModel):
    timestamp: int
    divergence_type: str
    price_pivot_1: PivotPoint
    price_pivot_2: PivotPoint
    osc_pivot_1: PivotPoint
    osc_pivot_2: PivotPoint
    strength: float = 0.0
