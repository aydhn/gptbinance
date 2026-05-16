class ReleaseLinkage:
    @staticmethod
    def validate_release_readiness(is_committed: bool, funding_secured: bool) -> bool:
        # No detached roadmap narrative
        return is_committed and funding_secured
