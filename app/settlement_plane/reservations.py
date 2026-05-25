from app.settlement_plane.models import ReservationRecord, ReservationClass

def evaluate_reservation(reservation: ReservationRecord):
    if reservation.reservation_class == ReservationClass.AMBIGUOUS:
        return {"status": "caution", "reservation_id": reservation.id, "warning": "Ambiguous reservation"}
    return {"status": "valid", "reservation_id": reservation.id, "class": reservation.reservation_class.value}
