import json
import os


class MlStorage:
    def __init__(self, base_dir="data/ml"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def save_manifest(self, manifest):
        pass

    def save_artifact(self, artifact):
        pass

    def load_artifact(self, run_id):
        pass
