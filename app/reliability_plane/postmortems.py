class PostmortemLinkManager:
    def __init__(self):
        self._links = {}

    def link_postmortem(self, service_id: str, postmortem_id: str, effect: str) -> None:
        if service_id not in self._links:
            self._links[service_id] = []
        self._links[service_id].append(
            {"postmortem_id": postmortem_id, "effect": effect}
        )

    def get_links(self, service_id: str) -> list:
        return self._links.get(service_id, [])
