def enforce_release_assurance():
    """
    Release candidates are not trusted without linked governed change refs,
    verification posture, and no open change exception burden.
    """
    pass

class ReleaseReadinessEvaluator:
    def evaluate(self, release_candidate):
        # Pseudo-logic to enforce change governance requirements
        if not getattr(release_candidate, "linked_change_refs", None):
            return "BLOCKED: Missing linked governed change refs."
        if not getattr(release_candidate, "verification_posture", None):
            return "CAUTION: Missing or weak verification posture."
        if getattr(release_candidate, "open_change_exception_burden", False):
            return "BLOCKED: Release under open change exception burden."
        return "TRUSTED"
