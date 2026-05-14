class ExperimentRecommendationExporter:
    def export_to_release_candidate(self, recommendation_id: str, candidate_input: dict):
        # Promote-input recommendations typed exported to release candidate creation
        pass

    def separate_winner_claim_from_release(self):
        # Experiment winner claim != releasable candidate distinction
        pass


class ExperimentRecommendationEvaluator:
    def link_failure_learnings(self, experiment_id: str, lessons: list):
        pass

class ExperimentRecommendation:
    def link_decision(self, decision_id: str):
        pass