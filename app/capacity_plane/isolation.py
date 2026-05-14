from typing import Dict, List

# Simulating isolation rules / breaches
_isolation_breaches: List[Dict] = []


def report_isolation_breach(
    environment: str,
    breaching_workload: str,
    impacted_live_path: bool,
    description: str,
) -> None:
    _isolation_breaches.append(
        {
            "environment": environment,
            "breaching_workload": breaching_workload,
            "impacted_live_path": impacted_live_path,
            "description": description,
        }
    )


def check_live_isolation() -> bool:
    # A true system would evaluate active reservations/allocations
    return not any(b["impacted_live_path"] for b in _isolation_breaches)


def list_isolation_breaches() -> List[Dict]:
    return _isolation_breaches
