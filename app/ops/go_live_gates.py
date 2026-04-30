import logging
from pydantic import BaseModel
from typing import Dict
from app.products.enums import ProductType
from app.products.registry import ProductRegistry

logger = logging.getLogger(__name__)

class DerivativesReadinessReport(BaseModel):
    product_type: ProductType
    leverage_configured: bool
    liquidation_guard_active: bool
    funding_accounting_active: bool
    status: str # PASS, CAUTION, FAIL

class GoLiveGate:
    def __init__(self, registry: ProductRegistry):
        self.registry = registry

    def check_derivatives_readiness(self) -> Dict[ProductType, DerivativesReadinessReport]:
        reports = {}
        for pt in self.registry.list_supported_products():
            if pt == ProductType.SPOT:
                continue

            # Mock checks - in reality, checks config files, connections, etc.
            report = DerivativesReadinessReport(
                product_type=pt,
                leverage_configured=True,
                liquidation_guard_active=True,
                funding_accounting_active=True,
                status="PASS" if pt.value == "FUTURES_USDM" else "CAUTION"
            )
            reports[pt] = report

        return reports
