import sys
import pytest
from unittest.mock import patch
from app.core.bootstrap import bootstrap
from app.core.enums import EnvironmentProfile


def test_bootstrap_check_only_success(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main", "--check-only"])
    with pytest.raises(SystemExit) as e:
        bootstrap()
    assert e.value.code == 0


def test_bootstrap_override_profile(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main", "--profile", "paper", "--check-only"])
    with pytest.raises(SystemExit) as e:
        bootstrap()
    assert e.value.code == 0
    # The active context should have been set to paper before exit
    from app.core.run_context import get_active_context

    ctx = get_active_context()
    assert ctx is not None
    assert ctx.profile == EnvironmentProfile.PAPER
