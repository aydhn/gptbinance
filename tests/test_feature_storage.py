import pytest
import pandas as pd
import os
import shutil
from app.research.features.storage import FeatureStorage
from app.research.features.models import (
    FeatureSet,
    FeatureGenerationReport,
    FeatureLineage,
    FeatureQualityReport,
)
from app.research.features.enums import FeatureQualityStatus
from datetime import datetime


@pytest.fixture
def temp_storage_dir(tmpdir):
    d = str(tmpdir.mkdir("features"))
    yield d
    shutil.rmtree(d)


def test_feature_storage_save_load(temp_storage_dir):
    storage = FeatureStorage(base_dir=temp_storage_dir)

    df = pd.DataFrame({"col1": [1, 2, 3]})

    lineage = FeatureLineage(
        run_id="test_run",
        timestamp=datetime.utcnow(),
        feature_set_name="test_set",
        symbol="BTC",
        interval="1h",
        columns_meta=[],
    )
    quality = FeatureQualityReport(
        status=FeatureQualityStatus.GOOD, null_percentage=0.0
    )
    report = FeatureGenerationReport(
        lineage=lineage, quality=quality, generation_time_ms=10.0
    )

    feature_set = FeatureSet(name="test_set", report=report)

    # Save
    storage.save(df, feature_set)

    # Load Meta
    loaded_set = storage.load_metadata("test_set", "BTC", "1h")
    assert loaded_set.name == "test_set"
    assert loaded_set.report.lineage.run_id == "test_run"

    # Load Data
    loaded_df = storage.load_data(loaded_set)
    assert list(loaded_df.columns) == ["col1"]
    assert len(loaded_df) == 3
