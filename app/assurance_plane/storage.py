import json
from app.assurance_plane.models import AssuranceRecord

def serialize_record(record: AssuranceRecord) -> str:
    return record.json()

def deserialize_record(data: str) -> AssuranceRecord:
    return AssuranceRecord.parse_raw(data)
