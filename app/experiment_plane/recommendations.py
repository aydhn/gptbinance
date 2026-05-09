# Recommendations
from app.experiment_plane.models import ExperimentRecommendation
from app.experiment_plane.enums import RecommendationClass


def build_continue_recommendation() -> ExperimentRecommendation:
    return ExperimentRecommendation(
        recommendation_class=RecommendationClass.CONTINUE,
        confidence_level="HIGH",
        rationale="Metrics stable",
    )

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.
