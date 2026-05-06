from .enums import IncidentSeverity, SignalType
from .models import IncidentSignal, IncidentScope


class SeverityMatrix:
    @staticmethod
    def evaluate_initial(signal: IncidentSignal) -> IncidentSeverity:
        critical_types = [
            SignalType.MARKET_TRUTH_BROKEN,
            SignalType.CROSS_BOOK_CONFLICT,
        ]
        major_types = [
            SignalType.SHADOW_DRIFT_CRITICAL,
            SignalType.CAPITAL_FREEZE_ESCALATED,
            SignalType.POLICY_HARD_BLOCK,
        ]

        if signal.type in critical_types:
            return IncidentSeverity.CRITICAL_INCIDENT
        if signal.type in major_types:
            return IncidentSeverity.MAJOR_INCIDENT
        return IncidentSeverity.INCIDENT

    @staticmethod
    def escalate(
        current: IncidentSeverity, new_signal: IncidentSignal
    ) -> IncidentSeverity:
        new_sev = SeverityMatrix.evaluate_initial(new_signal)
        levels = list(IncidentSeverity)
        if levels.index(new_sev) > levels.index(current):
            return new_sev
        return current
