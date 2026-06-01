from app.assurance_plane.models import SurveillanceCycleRecord
from app.assurance_plane.enums import SurveillanceClass

def create_surveillance_cycle(cycle_id: str, assurance_id: str, surv_class: SurveillanceClass, findings: list, next_check=None) -> SurveillanceCycleRecord:
    return SurveillanceCycleRecord(
        cycle_id=cycle_id,
        assurance_id=assurance_id,
        surveillance_class=surv_class,
        findings=findings,
        next_check=next_check
    )
