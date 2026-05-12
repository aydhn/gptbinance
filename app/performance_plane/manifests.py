class PerformanceWindowManifest:
    def __init__(
        self,
        window_id: str,
        release_candidate_ref: str = None,
        observability_trust_ref: str = None,
        rollout_stage_ref: str = None,
    ):
        self.window_id = window_id
        self.release_candidate_ref = release_candidate_ref
        self.rollout_stage_ref = rollout_stage_ref


class PerformanceComparativeAnalyzer:
    def compare_canary_vs_full(self, release_plane_context: dict):
        # Comparison tied to release plane
        pass
