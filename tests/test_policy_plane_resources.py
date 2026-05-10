import pytest
from app.policy_plane.resources import (
    create_symbol_resource,
    create_environment_resource,
)
from app.policy_plane.enums import ResourceClass


def test_symbol_resource():
    res = create_symbol_resource("BTCUSD")
    assert res.resource_class == ResourceClass.SYMBOL


def test_environment_resource():
    res = create_environment_resource("live")
    assert res.resource_class == ResourceClass.ENVIRONMENT
