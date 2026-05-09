from app.experiment_plane.models import ExperimentBaseline
from app.experiment_plane.enums import BaselineClass


def build_static_baseline(baseline_id: str, desc: str) -> ExperimentBaseline:
    return ExperimentBaseline(
        baseline_id=baseline_id, baseline_class=BaselineClass.STATIC, description=desc
    )
