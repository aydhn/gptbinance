class HiddenImpersonationSignal:
    pass


class TelemetryAnomalyIncidentSignal:
    def __init__(self, telemetry_id: str, trust_degraded: bool):
        self.telemetry_id = telemetry_id
        self.trust_degraded = trust_degraded

class SecretExposureIncidentSignal:
    pass

class StaleCredentialIncidentSignal:
    pass

class BoundaryAnomalyIncidentSignal:
    pass

class ExploitabilitySpikeIncidentSignal:
    pass

class RevokedPrincipalCredentialUseSignal:
    pass

class PatchLagIncidentSignal:
    pass
