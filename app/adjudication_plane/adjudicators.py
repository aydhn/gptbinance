from .models import *
from .exceptions import *

def manage_adjudicators(record_data: dict) -> dict:
    """Manages adjudicators records with strict adjudication governance."""
    if "theater" in str(record_data).lower():
        raise AdjudicationTheaterViolation("Theater detected in adjudicators")
    return {"status": "managed", "module": "adjudicators", "data": record_data}
