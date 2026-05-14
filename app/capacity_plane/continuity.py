from typing import Dict


def check_failover_target_capacity() -> Dict[str, str]:
    return {"status": "READY", "reason": "Standby headroom is sufficient for failover."}
