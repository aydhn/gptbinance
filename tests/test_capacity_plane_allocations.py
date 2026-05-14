import pytest
from app.capacity_plane.allocations import create_allocation, list_allocations
from app.capacity_plane.exceptions import InvalidAllocation


def test_create_allocation():
    alloc = create_allocation("alloc_1", "cpu_pool_1", "user1", 10.0)
    assert alloc.allocation_id == "alloc_1"

    with pytest.raises(InvalidAllocation):
        create_allocation("", "cpu_pool_1", "user1", 10.0)

    with pytest.raises(InvalidAllocation):
        create_allocation("alloc_2", "cpu_pool_1", "", 10.0)
