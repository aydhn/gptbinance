class StrategyEngine:
    def __init__(self):
        self.effective_config_manifest_ref = None

    def set_config(self, manifest_ref):
        self.effective_config_manifest_ref = manifest_ref
