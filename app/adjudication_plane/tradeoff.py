from .models import *
from .exceptions import *

def check_tradeoff_adjudication_linkage(ref_id: str, adjudication_id: str) -> dict:
    """Ensures tradeoff linkage does not bypass determination posture."""
    if not adjudication_id:
        return {"safe": False, "caution": f"Explicit caution: no adjudication posture for tradeoff"}
    return {"safe": True, "caution": None, "ref": ref_id, "adjudication_id": adjudication_id}
