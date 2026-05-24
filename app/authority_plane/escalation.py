from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import EscalationRecord
from .enums import EscalationClass

class EscalationManager:
    def __init__(self):
        self.records: Dict[str, EscalationRecord] = {}

    def get_authority_transfer(self) -> List[EscalationRecord]:
        return [r for r in self.records.values() if r.class_type == EscalationClass.AUTHORITY_TRANSFER]

    def get_deadlock_break(self) -> List[EscalationRecord]:
        return [r for r in self.records.values() if r.class_type == EscalationClass.DEADLOCK_BREAK]

    def get_emergency(self) -> List[EscalationRecord]:
        return [r for r in self.records.values() if r.class_type == EscalationClass.EMERGENCY_ESCALATION]

    def get_unresolved(self) -> List[EscalationRecord]:
        return [r for r in self.records.values() if r.class_type == EscalationClass.UNRESOLVED]

# OBLIGATION PLANE INTEGRATION
def evaluate_escalation(escalation_available: bool, escalation_duty_executed: bool) -> str:
    # escalation available but escalation duty missed explicit caution
    if escalation_available and not escalation_duty_executed:
        return "CAUTION: Escalation path available but mandatory escalation duty missed."
    return "Escalation handled correctly."
