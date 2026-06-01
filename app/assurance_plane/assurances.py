from app.assurance_plane.models import AssuranceRecord, AssuranceObject

def create_assurance_record(record_id: str, assurance_obj: AssuranceObject) -> AssuranceRecord:
    return AssuranceRecord(
        record_id=record_id,
        assurance_obj=assurance_obj,
        cases=[],
        certifications=[],
        attestations=[],
        surveillance=[],
        caveats=[],
        contradictions=[],
        revocations=[]
    )
