import pytest
import os
from app.optimizer.storage import OptimizerStorage
from app.optimizer.models import (
    OptimizerRun,
    OptimizerConfig,
    SearchSpace,
    ParameterSpec,
)
from app.optimizer.enums import SearchMode, OptimizerStatus, ParameterType


@pytest.fixture
def temp_db(tmpdir):
    db_path = os.path.join(tmpdir, "test_opt.db")
    storage = OptimizerStorage(db_path=db_path)
    yield storage
    if os.path.exists(db_path):
        os.remove(db_path)


def test_save_load_run(temp_db):
    config = OptimizerConfig(
        symbol="BTCUSDT",
        interval="1h",
        start_ts=0,
        end_ts=1000,
        feature_set="f1",
        strategy_family="s1",
        space_name="space1",
        max_trials=2,
    )
    space = SearchSpace(
        name="space1",
        strategy_family="s1",
        parameters=[
            ParameterSpec(name="p1", param_type=ParameterType.INT, default_value=1)
        ],
    )
    run = OptimizerRun(
        run_id="run_123",
        config=config,
        space=space,
        status=OptimizerStatus.COMPLETED,
        created_at="2023-01-01T00:00:00Z",
    )

    temp_db.save_run(run)
    loaded = temp_db.load_run("run_123")

    assert loaded is not None
    assert loaded.run_id == "run_123"
    assert loaded.status == OptimizerStatus.COMPLETED


def test_load_nonexistent(temp_db):
    assert temp_db.load_run("not_a_run") is None
