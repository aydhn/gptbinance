from .models import *
from .exceptions import *

def manage_comparisons(record_data: dict) -> dict:
    """Manages comparisons records with strict adjudication governance."""
    if "theater" in str(record_data).lower():
        raise AdjudicationTheaterViolation("Theater detected in comparisons")
    return {"status": "managed", "module": "comparisons", "data": record_data}
