from app.resilience_plane.storage import ResilienceStorage
class ResilienceRepository:
    def get_latest_trusted(self, resilience_id: str):
        return ResilienceStorage.load(f"trust_{resilience_id}")
