from app.stressrisk.storage import StressStorage


class StressRepository:
    def __init__(self, storage: StressStorage):
        self.storage = storage

    def store_run(self, run):
        self.storage.save_run(run)

    def fetch_run(self, run_id):
        return self.storage.get_run(run_id)
