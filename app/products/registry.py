from typing import Dict, List
from .enums import ProductType, ProductReadiness, MarginMode, PositionMode
from .models import (
    ProductDescriptor,
    ProductTradingCapabilities,
    ProductRiskDescriptor,
    ProductExecutionConstraints,
    ProductCostModel,
)
from .exceptions import UnsupportedProductType


class ProductRegistry:
    def __init__(self):
        self._products: Dict[ProductType, ProductDescriptor] = {}
        self._initialize_defaults()

    def _initialize_defaults(self):
        self.register_product(
            ProductDescriptor(
                product_type=ProductType.SPOT,
                readiness=ProductReadiness.LIVE,
                capabilities=ProductTradingCapabilities(
                    supports_short=False, supports_leverage=False, max_leverage=1
                ),
                risk=ProductRiskDescriptor(
                    liquidation_risk_enabled=False,
                    funding_risk_enabled=False,
                    borrow_risk_enabled=False,
                    reduce_only_required_on_flatten=False,
                ),
                constraints=ProductExecutionConstraints(min_notional=10.0),
                cost_model=ProductCostModel(
                    has_funding_fee=False, has_borrow_interest=False
                ),
            )
        )

        self.register_product(
            ProductDescriptor(
                product_type=ProductType.MARGIN,
                readiness=ProductReadiness.PAPER_ONLY,  # Conservative default
                capabilities=ProductTradingCapabilities(
                    supports_short=True,
                    supports_leverage=True,
                    max_leverage=3,
                    supported_margin_modes=[MarginMode.ISOLATED, MarginMode.CROSS],
                ),
                risk=ProductRiskDescriptor(
                    liquidation_risk_enabled=True,
                    funding_risk_enabled=False,
                    borrow_risk_enabled=True,
                    reduce_only_required_on_flatten=False,
                ),
                constraints=ProductExecutionConstraints(min_notional=10.0),
                cost_model=ProductCostModel(
                    has_funding_fee=False, has_borrow_interest=True
                ),
            )
        )

        self.register_product(
            ProductDescriptor(
                product_type=ProductType.FUTURES_USDM,
                readiness=ProductReadiness.TESTNET_ONLY,  # Conservative default
                capabilities=ProductTradingCapabilities(
                    supports_short=True,
                    supports_leverage=True,
                    max_leverage=5,
                    supported_margin_modes=[MarginMode.ISOLATED, MarginMode.CROSS],
                    supported_position_modes=[PositionMode.ONE_WAY, PositionMode.HEDGE],
                ),
                risk=ProductRiskDescriptor(
                    liquidation_risk_enabled=True,
                    funding_risk_enabled=True,
                    borrow_risk_enabled=False,
                    reduce_only_required_on_flatten=True,
                ),
                constraints=ProductExecutionConstraints(min_notional=5.0),
                cost_model=ProductCostModel(
                    has_funding_fee=True, has_borrow_interest=False
                ),
            )
        )

    def register_product(self, descriptor: ProductDescriptor):
        self._products[descriptor.product_type] = descriptor

    def get_descriptor(self, product_type: ProductType) -> ProductDescriptor:
        if product_type not in self._products:
            raise UnsupportedProductType(
                f"Product type {product_type} is not supported or not registered."
            )
        return self._products[product_type]

    def list_supported_products(self) -> List[ProductType]:
        return list(self._products.keys())

    def check_capability(self, product_type: ProductType, capability_name: str) -> bool:
        desc = self.get_descriptor(product_type)
        return getattr(desc.capabilities, capability_name, False)
