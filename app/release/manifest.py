# Mock Release Manifest
class ReleaseManifest:
    def __init__(self, version: str):
        self.version = version
        self.qualification_refs = []
        self.certified_fingerprints = {}

    def add_qualification_ref(self, run_id: str, profile: str):
        self.qualification_refs.append({"run_id": run_id, "profile": profile})
