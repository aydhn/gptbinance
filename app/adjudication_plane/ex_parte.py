from .models import *
from .exceptions import *

def manage_ex_parte(record_data: dict) -> dict:
    """Manages ex_parte records with strict adjudication governance."""
    if "theater" in str(record_data).lower():
        raise AdjudicationTheaterViolation("Theater detected in ex_parte")
    return {"status": "managed", "module": "ex_parte", "data": record_data}
