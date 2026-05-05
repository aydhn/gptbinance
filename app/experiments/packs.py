from app.experiments.models import (
    ExperimentPack,
    ExperimentDefinition,
    BaselineReference,
    CandidateReference,
)
import uuid


class ExperimentPackBuilder:
    def __init__(self, definition: ExperimentDefinition, baseline: BaselineReference):
        self.definition = definition
        self.baseline = baseline
        self.candidates = []

    def add_candidate(self, candidate: CandidateReference):
        self.candidates.append(candidate)
        return self

    def build(self) -> ExperimentPack:
        return ExperimentPack(
            pack_id=str(uuid.uuid4()),
            definition=self.definition,
            baseline=self.baseline,
            candidates=self.candidates,
        )
