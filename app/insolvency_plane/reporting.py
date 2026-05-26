# reporting.py
from typing import Dict, Any

class InsolvencyReporter:
    def __init__(self, repository):
        self.repository = repository

    def generate_summary(self) -> Dict[str, Any]:
        return {
            "insolvency_registry_count": len(self.repository.registry.list_all()),
            "estates_count": len(self.repository.estate_manager.list_estates()),
            "claims_count": len(self.repository.claim_manager.list_claims()),
            "stays_count": len(self.repository.stay_manager.list_stays()),
            "plans_count": len(self.repository.plan_manager.list_plans()),
            "liquidations_count": len(self.repository.liquidation_manager.list_liquidations()),
            "deficits_count": len(self.repository.residual_deficit_manager.list_deficits())
        }
