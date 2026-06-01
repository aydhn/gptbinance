from app.assurance_plane.models import AssuranceRecord

def check_quality(record: AssuranceRecord) -> list:
    warnings = []
    if not record.cases or not any(c.is_complete for c in record.cases):
        warnings.append("false_assurance_warning: No complete assurance case.")
    if record.expiry and record.expiry.is_expired:
        warnings.append("stale_certificate_warning: Assurance is expired.")
    if any(c.is_material and not c.is_resolved for c in record.contradictions):
        warnings.append("contradiction_warning: Unresolved material contradictions exist.")
    return warnings
