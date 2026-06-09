from .models import *
from .exceptions import *

def manage_debt(record_data: dict) -> dict:
    """Manages debt records with strict adjudication governance."""
    if "theater" in str(record_data).lower():
        raise AdjudicationTheaterViolation("Theater detected in debt")
    return {"status": "managed", "module": "debt", "data": record_data}
