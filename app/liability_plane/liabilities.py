from app.liability_plane.models import LiabilityRecord, LiabilityObject

class LiabilityManager:
    def __init__(self):
        self._records = {}

    def initialize_record(self, liability_obj: LiabilityObject) -> LiabilityRecord:
        record = LiabilityRecord(liability=liability_obj)
        self._records[liability_obj.liability_id] = record
        return record

    def get_record(self, liability_id: str) -> LiabilityRecord:
        return self._records.get(liability_id)

    def list_records(self):
        return list(self._records.values())
