class StorageManager:
    def __init__(self):
        self.data = {}

    def save(self, key: str, value: any):
        self.data[key] = value

    def load(self, key: str) -> any:
        return self.data.get(key)
