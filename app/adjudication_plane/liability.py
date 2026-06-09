from .models import *
from .exceptions import *

def manage_liability(record_data: dict) -> dict:
    """Manages liability records with strict adjudication governance."""
    if "theater" in str(record_data).lower():
        raise AdjudicationTheaterViolation("Theater detected in liability")
    return {"status": "managed", "module": "liability", "data": record_data}
