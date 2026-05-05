from app.experiments.storage import ExperimentStorage


class ExperimentRepository:
    def __init__(self, storage: ExperimentStorage):
        self.storage = storage

    def save_hypothesis(self, h_id: str, data: dict):
        self.storage.save(f"hyp_{h_id}", data)

    def get_hypothesis(self, h_id: str) -> dict:
        return self.storage.load(f"hyp_{h_id}")

    def save_pack(self, p_id: str, data: dict):
        self.storage.save(f"pack_{p_id}", data)

    def get_pack(self, p_id: str) -> dict:
        return self.storage.load(f"pack_{p_id}")

    # Similar methods for runs, comparisons, etc.
