from .registry import registry
def generate_report(obj_id: str):
    obj = registry.get(obj_id)
    return {"report_id": f"rep_{obj_id}", "summary": obj} if obj else {}
