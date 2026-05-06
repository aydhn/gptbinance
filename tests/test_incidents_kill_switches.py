import pytest
from app.incidents.kill_switches import KillSwitchHierarchy


def test_kill_switches():
    switches = KillSwitchHierarchy.get_allowed_switches("SYMBOL")
    assert "SYMBOL_HALT" in switches
