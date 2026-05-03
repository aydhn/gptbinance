class ReleaseManifest:
    def __init__(self, version: str):
        self.version = version
        self.perf_baseline_refs: list[str] = []
        self.tested_host_classes: list[str] = []

    def set_perf_data(self, baselines: list, host_classes: list) -> None:
        self.perf_baseline_refs = baselines
        self.tested_host_classes = host_classes
