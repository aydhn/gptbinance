import os
import json


class SecurityStorage:
    def save_record(self, dir_path: str, filename: str, data: str):
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, filename), "w") as f:
            f.write(data)
