from app.experiments.base import ExperimentRunnerBase
from app.experiments.models import ExperimentRun
from app.experiments.enums import EvaluationSurface
import uuid
from datetime import datetime, timezone


class OfflineExperimentRunner(ExperimentRunnerBase):
    def run(self, pack_id: str) -> str:
        run_id = str(uuid.uuid4())
        # Dummy implementation of offline run
        ExperimentRun(
            run_id=run_id,
            pack_id=pack_id,
            evaluation_surface=EvaluationSurface.OFFLINE_BACKTEST,
            status="completed",
            completed_at=datetime.now(timezone.utc),
            results={"pnl_delta": 0.05, "friction_reduction": 0.1},
        )
        return run_id
