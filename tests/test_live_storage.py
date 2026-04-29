import pytest
import os
from pathlib import Path
from app.execution.live_runtime.storage import LiveStorage
from app.execution.live_runtime.repository import LiveRepository
from app.execution.live_runtime.models import (
    LiveRun,
    LiveSessionConfig,
    LiveCapitalCaps,
)
from app.execution.live_runtime.enums import LiveRolloutMode


def test_live_storage_and_repository(tmp_path):
    storage = LiveStorage(base_dir=str(tmp_path))
    repo = LiveRepository(storage)

    config = LiveSessionConfig(
        rollout_mode=LiveRolloutMode.CANARY_LIVE,
        capital_caps=LiveCapitalCaps(
            max_session_notional_usd=100.0,
            max_daily_loss_usd=10.0,
            max_live_exposure_usd=50.0,
            max_new_orders_per_session=5,
        ),
    )
    run = LiveRun(run_id="r1", config=config)

    repo.save_run(run)

    loaded_run = repo.get_run("r1")
    assert loaded_run is not None
    assert loaded_run.run_id == "r1"
    assert loaded_run.config.rollout_mode == LiveRolloutMode.CANARY_LIVE
