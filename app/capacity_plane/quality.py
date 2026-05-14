from typing import Any
from typing import Dict, List


def evaluate_capacity_quality() -> Dict[str, Any]:
    warnings = []
    # Placeholder for checking unallocated reservations, etc
    return {
        "verdict": "GOOD" if not warnings else "NEEDS_IMPROVEMENT",
        "warnings": warnings,
    }
