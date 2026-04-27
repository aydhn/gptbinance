import time
import pandas as pd
from datetime import datetime
from typing import Dict, List, Tuple
import uuid

from app.research.features.models import (
    FeatureRequest,
    FeatureSpec,
    MultiTimeframeFeatureSpec,
    FeatureColumnMeta,
    FeatureLineage,
    FeatureQualityReport,
    FeatureGenerationReport,
    FeatureSet,
)
from app.research.features.registry import FeatureRegistry
from app.research.features.leakage_guards import LeakageGuard
from app.research.features.enums import FeatureQualityStatus
from app.research.features.mtf_alignment import MTFAligner
from app.research.features.exceptions import FeatureGenerationError


class FeatureEngine:
    """
    Orchestrates feature generation based on a request.
    """

    def generate(
        self, df: pd.DataFrame, request: FeatureRequest, run_id: str = None
    ) -> Tuple[pd.DataFrame, FeatureSet]:
        start_time = time.time()

        if run_id is None:
            run_id = str(uuid.uuid4())

        result_df = pd.DataFrame(index=df.index)
        columns_meta: List[FeatureColumnMeta] = []
        warnings: List[str] = []

        total_cells = 0
        null_cells = 0

        for spec_item in request.specs:
            try:
                if isinstance(spec_item, MultiTimeframeFeatureSpec):
                    # MTF Logic
                    # 1. We assume the required HTF data is somehow provided or calculated.
                    # For a true engine, we'd need to fetch HTF data, calculate feature, then align.
                    # Since this engine only receives one `df`, if we want MTF, we must assume
                    # `df` already contains the HTF data merged, OR this engine is expanded to take multiple dfs.
                    # For Phase 06, we will flag this as a warning if we can't process it directly,
                    # but we provide the aligner for manual use.
                    warnings.append(
                        f"MTF Spec for {spec_item.base_spec.name} skipped in single-df engine logic. Use MTFAligner manually or pass multi-df dict."
                    )
                    continue

                else:
                    # Normal Feature Logic
                    spec = spec_item
                    calc = FeatureRegistry.get(spec.name)

                    # Calculate
                    feature_output = calc(df, spec)

                    # Handle output
                    if isinstance(feature_output, pd.Series):
                        outputs = {feature_output.name: feature_output}
                    else:
                        outputs = {
                            col: feature_output[col] for col in feature_output.columns
                        }

                    for col_name, series in outputs.items():
                        # Leakage Guard: Check index alignment
                        LeakageGuard.check_future_leak(df, series)

                        # Calculate warmup and nulls
                        min_hist = calc.get_min_history_required(spec)
                        warmup = LeakageGuard.validate_warmup(series, min_hist)
                        nulls = int(series.isna().sum())

                        total_cells += len(series)
                        null_cells += nulls

                        columns_meta.append(
                            FeatureColumnMeta(
                                column_name=col_name,
                                spec=spec,
                                null_count=nulls,
                                warmup_period=warmup,
                            )
                        )

                        result_df[col_name] = series

            except Exception as e:
                raise FeatureGenerationError(
                    f"Failed to generate feature {spec_item}: {str(e)}"
                ) from e

        # Quality Report
        null_pct = (null_cells / total_cells * 100) if total_cells > 0 else 0
        status = FeatureQualityStatus.GOOD
        if null_pct > 20:
            status = FeatureQualityStatus.WARNING
            warnings.append(f"High null percentage: {null_pct:.1f}%")
        if null_pct > 50:
            status = FeatureQualityStatus.BAD

        quality = FeatureQualityReport(
            status=status,
            null_percentage=null_pct,
            warnings=warnings,
            leakage_checks_passed=True,  # If an exception wasn't raised by LeakageGuard
        )

        # Lineage
        lineage = FeatureLineage(
            run_id=run_id,
            timestamp=datetime.utcnow(),
            feature_set_name=request.feature_set_name,
            symbol=request.symbol,
            interval=request.interval,
            columns_meta=columns_meta,
            source_data_hash=None,  # Could hash the input df
        )

        # Report
        report = FeatureGenerationReport(
            lineage=lineage,
            quality=quality,
            generation_time_ms=(time.time() - start_time) * 1000,
        )

        feature_set = FeatureSet(
            name=request.feature_set_name, report=report, storage_path=None
        )

        return result_df, feature_set
