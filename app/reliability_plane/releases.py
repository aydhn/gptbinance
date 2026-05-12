class ReleaseLinkManager:
    def __init__(self):
        self._links = {}

    def link_release(self, service_id: str, release_id: str, posture: str) -> None:
        if service_id not in self._links:
            self._links[service_id] = []
        self._links[service_id].append({"release_id": release_id, "posture": posture})

    def get_links(self, service_id: str) -> list:
        return self._links.get(service_id, [])
