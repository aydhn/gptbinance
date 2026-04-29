import pytest
from app.execution.live_runtime.rollback import LiveRollbackController
from app.execution.live_runtime.enums import RollbackSeverity
from unittest.mock import MagicMock


def test_live_rollback():
    mock_flatten = MagicMock()
    ctrl = LiveRollbackController(mock_flatten)

    context = {"mainnet_armed": True}
    plan = ctrl.initiate_rollback(
        "r1", RollbackSeverity.HARD, "Critical Failure", context
    )

    assert plan.run_id == "r1"
    assert plan.disarm_mainnet
    assert plan.trigger_flatten
    assert not context["mainnet_armed"]
