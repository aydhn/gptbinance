from .models import *
from .exceptions import *

def check_remedy_adjudication_linkage(ref_id: str, adjudication_id: str) -> dict:
    """Ensures remedy linkage does not bypass determination posture."""
    if not adjudication_id:
        return {"safe": False, "caution": f"Explicit caution: no adjudication posture for remedy"}
    return {"safe": True, "caution": None, "ref": ref_id, "adjudication_id": adjudication_id}
