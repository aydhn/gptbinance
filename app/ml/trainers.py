from datetime import datetime, timezone
from app.ml.models import TrainRun, ModelArtifact, ModelCard
from app.ml.enums import ModelFamily


class Trainer:
    def train(self, dataset_id: str, family: ModelFamily, config: dict) -> TrainRun:
        # setup simple deterministic models
        # logistic regression, etc.
        return TrainRun(
            run_id=f"run_{int(datetime.now(timezone.utc).timestamp())}",
            dataset_id=dataset_id,
            model_family=family,
            config_snapshot=config,
            seed=42,
        )
