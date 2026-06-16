from app.waterfall_plane.storage import WaterfallStorage

class WaterfallRepository:
    def __init__(self, storage: WaterfallStorage):
        self.storage = storage

    def save_record(self, record_id: str, data: dict):
        self.storage.save(record_id, data)

    def get_record(self, record_id: str) -> dict:
        return self.storage.load(record_id)
