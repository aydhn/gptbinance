class HiddenImpersonationSignal:
    pass


class TelemetryAnomalyIncidentSignal:
    def __init__(self, telemetry_id: str, trust_degraded: bool):
        self.telemetry_id = telemetry_id
        self.trust_degraded = trust_degraded
