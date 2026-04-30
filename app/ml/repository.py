from app.ml.storage import MlStorage


class MlRepository:
    def __init__(self):
        self.storage = MlStorage()

    def get_dataset(self, dataset_id):
        pass

    def save_run(self, run):
        pass
