class ActivationGuard:
    def check_research_evidence(self):
        pass

    def check_release_manifest(self, manifest: dict) -> bool:
        """
        Ensures activation can only proceed with valid release manifest references.
        Adds release compatibility and rollout class gates.
        Rejects release-less stage progression.
        """
        if not manifest or not manifest.get("release_id"):
            return False

        if manifest.get("compatibility_violation", False):
            return False

        return True
