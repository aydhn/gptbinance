from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

from app.qualification.models import (
    QualificationRun,
    QualificationProfile,
    QualificationConfig,
    ScenarioResult,
    ContractCheckResult,
    QualificationFinding,
    QualificationScore,
    QualificationVerdict,
    EvidencePack,
)


class BaseScenarioSuite(ABC):
    @property
    @abstractmethod
    def suite_id(self) -> str:
        pass

    @abstractmethod
    def run(self, config: QualificationConfig) -> List[ScenarioResult]:
        pass


class BaseContractVerifier(ABC):
    @abstractmethod
    def verify(self, config: QualificationConfig) -> List[ContractCheckResult]:
        pass


class BaseEvidenceCollector(ABC):
    @abstractmethod
    def collect(self, run_id: str, profile: QualificationProfile) -> EvidencePack:
        pass


class BaseVerdictEvaluator(ABC):
    @abstractmethod
    def evaluate(self, run: QualificationRun) -> QualificationVerdict:
        pass


class BaseQualificationRunner(ABC):
    @abstractmethod
    def run(
        self, profile: QualificationProfile, config: QualificationConfig
    ) -> QualificationRun:
        pass
