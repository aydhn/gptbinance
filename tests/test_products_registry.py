import pytest
from app.products.registry import ProductRegistry
from app.products.enums import ProductType


def test_spot_capabilities():
    reg = ProductRegistry()
    desc = reg.get_descriptor(ProductType.SPOT)
    assert desc.capabilities.supports_short is False
    assert desc.capabilities.supports_leverage is False


def test_futures_capabilities():
    reg = ProductRegistry()
    desc = reg.get_descriptor(ProductType.FUTURES_USDM)
    assert desc.capabilities.supports_short is True
    assert desc.capabilities.max_leverage > 1
