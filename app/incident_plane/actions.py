class IncidentAction:
    def __init__(self, actor_session_id: str):
        self.actor_session_id = actor_session_id

    def bind_security(self, security_asset_refs: list, exposure_state: str, compensating_control_linkage: list):
        self.security_asset_refs = security_asset_refs
        self.exposure_state = exposure_state
        self.compensating_control_linkage = compensating_control_linkage
