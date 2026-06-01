from app.assurance_plane.models import AssuranceRecord

def generate_summary(record: AssuranceRecord) -> str:
    summary = f"Assurance ID: {record.assurance_obj.assurance_id}\n"
    summary += f"Class: {record.assurance_obj.class_type.value}\n"
    summary += f"Owner: {record.assurance_obj.owner}\n"
    summary += f"Complete Cases: {sum(1 for c in record.cases if c.is_complete)}\n"
    summary += f"Contradictions: {len(record.contradictions)}\n"
    summary += f"Certifications: {len(record.certifications)}\n"
    return summary
