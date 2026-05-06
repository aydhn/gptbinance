from typing import Dict, Any


def export_activation_failure(failure_id: str):
    pass


def export_probation_pass_fail_rates() -> Dict[str, Any]:
    return {"pass_rate": 1.0, "fail_density": 0.0, "repeated_halts": 0}
