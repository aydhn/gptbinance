from datetime import datetime


class IngestionReceipt:
    def __init__(self, source_id: str, ingest_time: datetime, record_count: int):
        self.source_id = source_id
        self.ingest_time = ingest_time
        self.record_count = record_count
