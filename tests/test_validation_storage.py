import pytest
import uuid
from app.backtest.validation.storage import ValidationStorage
from app.backtest.validation.models import (
    ValidationSummary,
    ValidationStatus,
    ValidationArtifactManifest,
)


def test_validation_storage():
    storage = ValidationStorage(db_path=":memory:")
    strategy_run_id = uuid.uuid4()

    manifest = ValidationArtifactManifest(
        benchmark_run_ids=[], comparison_ids=[], ablation_run_ids=[], robustness_ids=[]
    )

    summary = ValidationSummary(
        strategy_run_id=strategy_run_id,
        status=ValidationStatus.COMPLETED,
        benchmarks=[],
        comparisons=[],
        ablations=[],
        robustness_checks=[],
        artifact_manifest=manifest,
    )

    storage.save_validation_summary(summary)
    retrieved = storage.get_validation_summary(strategy_run_id)
    assert retrieved is not None
    assert retrieved.status == ValidationStatus.COMPLETED
