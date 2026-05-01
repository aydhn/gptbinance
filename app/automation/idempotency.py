import hashlib
import json
from typing import Any, Dict


def generate_run_key(
    job_id: str, inputs: Dict[str, Any], scheduled_time: str = ""
) -> str:
    """Generate a unique idempotency key for a job run."""
    raw = f"{job_id}:{json.dumps(inputs, sort_keys=True)}:{scheduled_time}"
    return hashlib.sha256(raw.encode()).hexdigest()
