from app.cost_plane.reservations import ReservationManager

def test_reservation_manager():
    manager = ReservationManager()
    record = manager.record_reservation("c-1", 100.0, 80.0, 5.0, "USD")
    assert record.cost_of_unused == 100.0
