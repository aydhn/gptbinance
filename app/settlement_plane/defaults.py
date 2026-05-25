from app.settlement_plane.models import DefaultRecord, DefaultClass

def evaluate_defaults(default_record: DefaultRecord):
    if not default_record.cured:
        return {"status": "active_default", "default_id": default_record.id, "class": default_record.default_class.value}
    return {"status": "cured", "default_id": default_record.id}
