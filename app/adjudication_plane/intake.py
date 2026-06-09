from .models import *
from .exceptions import *

def manage_intake(record_data: dict) -> dict:
    """Manages intake records with strict adjudication governance."""
    if "theater" in str(record_data).lower():
        raise AdjudicationTheaterViolation("Theater detected in intake")
    return {"status": "managed", "module": "intake", "data": record_data}
