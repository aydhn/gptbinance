from app.capacity_plane.registry import capacity_registry
from app.capacity_plane.reservations import list_reservations
from app.capacity_plane.saturation import list_saturation_records
from app.capacity_plane.trust import evaluate_capacity_trust


def generate_capacity_summary() -> str:
    res_count = len(capacity_registry.list_resources())
    quota_count = len(capacity_registry.list_quotas())
    rsv_count = len(list_reservations())
    sat_count = len(list_saturation_records())
    trust = evaluate_capacity_trust()

    report = f"Capacity Summary:\n"
    report += f"- Resources: {res_count}\n"
    report += f"- Quotas: {quota_count}\n"
    report += f"- Reservations: {rsv_count}\n"
    report += f"- Saturation Events: {sat_count}\n"
    report += f"- Trust Verdict: {trust.verdict.value}\n"

    return report
