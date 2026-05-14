from app.cost_plane.storage import CostStorage

class CostRepository:
    def __init__(self, storage: CostStorage):
        self.storage = storage

    def save_cost_object(self, cost_id: str, data: dict):
        self.storage.save("costs", cost_id, data)

    def get_latest_trusted_cost(self, cost_id: str):
        return self.storage.get("costs", cost_id)
