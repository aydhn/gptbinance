class Reporter:
    def __init__(self, registry, trust_manager):
        self._registry = registry
        self._trust = trust_manager

    def generate_service_summary(self, service_id: str) -> str:
        service = self._registry.get_service(service_id)
        if not service:
            return f"Service {service_id} not found."

        verdict = self._trust.get_latest_verdict(service_id)
        verdict_str = verdict.verdict.value if verdict else "UNKNOWN"

        return f"Service: {service.service_id}\nClass: {service.service_class.value}\nTrust Verdict: {verdict_str}\n"
