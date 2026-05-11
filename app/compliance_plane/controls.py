from app.compliance_plane.models import ControlObjective
from app.compliance_plane.enums import ControlClass


def create_control_objective(
    control_id: str,
    control_class: ControlClass,
    owner_id: str,
    cadence_days: int,
    is_automated: bool,
    is_preventive: bool,
    is_detective: bool,
    is_corrective: bool,
    is_compensating: bool = False,
) -> ControlObjective:
    return ControlObjective(
        control_id=control_id,
        control_class=control_class,
        owner_id=owner_id,
        cadence_days=cadence_days,
        is_automated=is_automated,
        is_preventive=is_preventive,
        is_detective=is_detective,
        is_corrective=is_corrective,
        is_compensating=is_compensating,
    )
