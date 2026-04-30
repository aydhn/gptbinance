import pytest
from app.governance.refresh_plans import get_fast_refresh_plan, get_deep_refresh_plan


def test_fast_refresh_plan():
    plan = get_fast_refresh_plan()
    assert plan.name == "fast_refresh"
    assert "data" in plan.components
    assert not plan.is_deep


def test_deep_refresh_plan():
    plan = get_deep_refresh_plan()
    assert plan.name == "deep_refresh"
    assert "ml" in plan.components
    assert plan.is_deep
