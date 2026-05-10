class ActivationHistory:
    def __init__(self):
        self._history = []

    def store_research_manifest(self):
        pass

    def record_stage_activation(self, stage: str, release_ref: str, rollout_stage_ref: str, rollback_eligible: bool):
        """
        Stores stage activation release refs, rollout stage refs, and rollback eligibility.
        """
        self._history.append({
            "stage": stage,
            "release_ref": release_ref,
            "rollout_stage_ref": rollout_stage_ref,
            "rollback_eligible": rollback_eligible,
        })

    def export_stage_diffs(self) -> list:
        """
        Exports stage-to-stage release diffs lineage.
        """
        return [{"lineage": "mocked_diff"}]
