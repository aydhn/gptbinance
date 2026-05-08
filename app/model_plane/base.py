from abc import ABC, abstractmethod
from typing import List, Optional
from app.model_plane.models import (
    ModelDefinition,
    InferenceContract,
    CalibrationRecord,
    TrustedSignalVerdictSummary,
    ModelCheckpointRecord,
)


class ModelRegistryBase(ABC):
    @abstractmethod
    def register_model(self, model: ModelDefinition) -> None:
        pass

    @abstractmethod
    def get_model(self, model_id: str) -> Optional[ModelDefinition]:
        pass

    @abstractmethod
    def list_models(self) -> List[ModelDefinition]:
        pass


class InferenceContractEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_contract(self, model_id: str, checkpoint_id: str) -> InferenceContract:
        pass

    @abstractmethod
    def validate_contract(self, contract: InferenceContract) -> bool:
        pass


class CalibrationEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_calibration(self, checkpoint_id: str) -> CalibrationRecord:
        pass

    @abstractmethod
    def check_calibration_freshness(self, record: CalibrationRecord) -> bool:
        pass


class TrustedSignalBuilderBase(ABC):
    @abstractmethod
    def build_verdict(
        self, model_id: str, checkpoint_id: str
    ) -> TrustedSignalVerdictSummary:
        pass
