class ControlLinkManager:
    def __init__(self):
        self._links = {}

    def record_control_action(self, service_id: str, action: str, impact: str) -> None:
        if service_id not in self._links:
            self._links[service_id] = []
        self._links[service_id].append({"action": action, "impact": impact})

    def get_links(self, service_id: str) -> list:
        return self._links.get(service_id, [])
