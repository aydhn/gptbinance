class StrategyLifecycleManager:
    def transition_to_live(self, strategy_id: str, release_bundle_ref: str):
        if not release_bundle_ref:
            raise Exception("Cannot transition to live/probation without active release bundle ref.")
        pass

    def check_retirement_blocks(self, strategy_id: str):
        # Retired/frozen strategy is a release bundle entry blocker
        pass

class StrategyTransition:
    def validate_decision_manifest(self, manifest_id: str):
        pass