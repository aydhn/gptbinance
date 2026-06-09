from .models import *
from .exceptions import *

def check_autonomy_adjudication_linkage(ref_id: str, adjudication_id: str) -> dict:
    """Ensures autonomy linkage does not bypass determination posture."""
    if not adjudication_id:
        return {"safe": False, "caution": f"Explicit caution: no adjudication posture for autonomy"}
    return {"safe": True, "caution": None, "ref": ref_id, "adjudication_id": adjudication_id}
