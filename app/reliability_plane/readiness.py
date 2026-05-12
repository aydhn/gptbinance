class ReadinessIntegrator:
    def __init__(self, registry, trust_manager, budget_manager):
        self.registry = registry
        self.trust = trust_manager
        self.budgets = budget_manager

    def gather_readiness_evidence(self, service_id: str) -> dict:
        service = self.registry.get_service(service_id)
        verdict = self.trust.get_latest_verdict(service_id)
        # Check budgets...
        return {
            "service_id": service_id,
            "trust_verdict": verdict.verdict.value if verdict else "unknown",
            "is_ready": verdict is not None and verdict.verdict.value == "trusted",
        }
