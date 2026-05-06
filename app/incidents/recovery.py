from .models import RecoveryPlan, IncidentRecord
from .enums import RecoveryVerdict
from .recovery_gates import RecoveryGates


class RecoveryPlanner:
    @staticmethod
    def evaluate(incident: IncidentRecord) -> RecoveryPlan:
        blockers = RecoveryGates.check_gates(incident)
        verdict = RecoveryVerdict.NOT_READY if blockers else RecoveryVerdict.CONDITIONAL
        return RecoveryPlan(
            verdict=verdict,
            unresolved_blockers=blockers,
            cleared_gates=["No active signal streams"] if not blockers else [],
        )
