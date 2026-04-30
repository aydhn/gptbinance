from datetime import datetime, timedelta
from app.ml.models import DatasetSpec
from app.ml.enums import SplitType
from app.ml.datasets import DatasetBuilder


def test_dataset_builder():
    spec = DatasetSpec(
        feature_set="core_trend",
        label_spec_name="success_v1",
        split_type=SplitType.CONTIGUOUS,
        train_start=datetime(2023, 1, 1),
        train_end=datetime(2023, 2, 1),
        test_start=datetime(2023, 2, 1),
        test_end=datetime(2023, 3, 1),
    )
    builder = DatasetBuilder()
    manifest = builder.build(spec)

    assert manifest.spec.feature_set == "core_trend"
    assert manifest.train_rows == 1000
    assert "core_trend" in manifest.dataset_id
