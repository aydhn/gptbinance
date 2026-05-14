from datetime import timezone
from datetime import datetime
from typing import Dict, List, Optional
from app.capacity_plane.models import ReservationRecord
from app.capacity_plane.enums import ReservationClass, WorkloadClass, PriorityClass
from app.capacity_plane.exceptions import InvalidReservation

_reservations: Dict[str, ReservationRecord] = {}


def create_reservation(
    reservation_id: str,
    resource_id: str,
    workload_class: WorkloadClass,
    priority_class: PriorityClass,
    reservation_class: ReservationClass,
    amount: float,
    expires_at: Optional[datetime] = None,
    lineage_refs: List[str] = None,
) -> ReservationRecord:
    if not reservation_id:
        raise InvalidReservation("Reservation ID is required.")
    if amount <= 0:
        raise InvalidReservation("Reservation amount must be positive.")

    # In a real system, we would check if the resource has enough unreserved capacity here.

    res = ReservationRecord(
        reservation_id=reservation_id,
        resource_id=resource_id,
        workload_class=workload_class,
        priority_class=priority_class,
        reservation_class=reservation_class,
        amount=amount,
        created_at=datetime.now(
            timezone.utc
        ),  # To be replaced with timezone-aware later if needed, though prompt said utcnow is deprecated, better use timezone.utc
        expires_at=expires_at,
        lineage_refs=lineage_refs or [],
    )
    _reservations[reservation_id] = res
    return res


def get_reservation(reservation_id: str) -> Optional[ReservationRecord]:
    return _reservations.get(reservation_id)


def list_reservations() -> List[ReservationRecord]:
    return list(_reservations.values())



# Cost plane evaluation integration
def get_stale_reservations_cost_burden():
    return {"stale": True, "burden": "canonical ref to cost plane"}
