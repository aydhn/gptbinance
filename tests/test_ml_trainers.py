from app.ml.trainers import Trainer
from app.ml.enums import ModelFamily


def test_trainer():
    trainer = Trainer()
    run = trainer.train("ds_123", ModelFamily.LOGISTIC_REGRESSION, {"C": 1.0})

    assert run.dataset_id == "ds_123"
    assert run.model_family == ModelFamily.LOGISTIC_REGRESSION
    assert run.config_snapshot["C"] == 1.0
