from typing import Dict
class ResilienceStorage:
    _data: Dict[str, dict] = {}

    @classmethod
    def save(cls, key: str, value: dict):
        cls._data[key] = value

    @classmethod
    def load(cls, key: str):
        return cls._data.get(key)
