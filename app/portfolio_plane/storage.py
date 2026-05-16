# Mock storage module tying it all together.
class StorageBackend:
    def __init__(self):
        self.data = {}

    def save(self, key: str, value: str):
        self.data[key] = value

    def load(self, key: str) -> str:
        return self.data.get(key)
