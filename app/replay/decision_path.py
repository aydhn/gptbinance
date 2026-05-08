class ReplayDecisionPath:
    def build_path(self, manifest_ref: str, budget_ref: str, trust_verdict: str):
        # Replay-only divergence appears as explicit caution
        pass

class ReplayDecisionPathExecutionExtension:
    def __init__(self):
        self.execution_manifest_refs = []
        self.caveats = ["replay_only_execution_reconstruction"]
