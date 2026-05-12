from typing import Dict, List, Optional
from .models import TelemetryIngestionRecord

class IngestionRegistry:
    def __init__(self):
        self._records: Dict[str, TelemetryIngestionRecord] = {}

    def register_ingestion(self, record: TelemetryIngestionRecord) -> None:
        self._records[record.ingestion_id] = record

    def get_ingestion(self, ingestion_id: str) -> Optional[TelemetryIngestionRecord]:
        return self._records.get(ingestion_id)

    def list_ingestion(self) -> List[TelemetryIngestionRecord]:
        return list(self._records.values())
