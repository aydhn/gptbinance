from .enums import RecoveryVerdict


class RecoveryGates:
    @staticmethod
    def check_gates(incident):
        blockers = []
        if incident.state != "CONTAINED" and incident.state != "DEGRADED":
            blockers.append("Incident must be contained before recovery.")
        return blockers
