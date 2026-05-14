import pytest
from app.capacity_plane.reservations import create_reservation, list_reservations
from app.capacity_plane.enums import ReservationClass, WorkloadClass, PriorityClass
from app.capacity_plane.exceptions import InvalidReservation


def test_create_reservation():
    res = create_reservation(
        "res_1",
        "cpu_pool_1",
        WorkloadClass.LIVE_TRADING,
        PriorityClass.CRITICAL,
        ReservationClass.GUARANTEED,
        50.0,
    )
    assert res.reservation_id == "res_1"
    assert res.amount == 50.0

    with pytest.raises(InvalidReservation):
        create_reservation(
            "",
            "cpu_pool_1",
            WorkloadClass.LIVE_TRADING,
            PriorityClass.CRITICAL,
            ReservationClass.GUARANTEED,
            50.0,
        )

    with pytest.raises(InvalidReservation):
        create_reservation(
            "res_2",
            "cpu_pool_1",
            WorkloadClass.LIVE_TRADING,
            PriorityClass.CRITICAL,
            ReservationClass.GUARANTEED,
            0.0,
        )
