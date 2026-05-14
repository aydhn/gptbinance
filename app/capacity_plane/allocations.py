from datetime import datetime, timezone
from typing import Dict, List, Optional
from app.capacity_plane.models import AllocationRecord
from app.capacity_plane.exceptions import InvalidAllocation

_allocations: Dict[str, AllocationRecord] = {}


def create_allocation(
    allocation_id: str,
    resource_id: str,
    actor: str,
    amount: float,
    exclusive: bool = False,
    reservation_id: Optional[str] = None,
) -> AllocationRecord:
    if not allocation_id:
        raise InvalidAllocation("Allocation ID is required.")
    if not actor:
        raise InvalidAllocation("Allocation without traceable actor is prohibited.")

    alloc = AllocationRecord(
        allocation_id=allocation_id,
        resource_id=resource_id,
        actor=actor,
        amount=amount,
        exclusive=exclusive,
        reservation_id=reservation_id,
        created_at=datetime.now(timezone.utc),
    )
    _allocations[allocation_id] = alloc
    return alloc


def list_allocations() -> List[AllocationRecord]:
    return list(_allocations.values())
