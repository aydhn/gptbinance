class ActivationGuard:
    def __init__(self, progression_actor_session_id: str, observability_manifest_id: str = None):
        self.progression_actor_session_id = progression_actor_session_id
        self.observability_manifest_id = observability_manifest_id
