from app.research_plane.models import ResearchHypothesis
from app.research_plane.exceptions import InvalidHypothesisError


class HypothesisContractValidator:
    def validate(self, hypothesis: ResearchHypothesis) -> bool:
        if not hypothesis.claimed_effect:
            raise InvalidHypothesisError("Hypothesis must state a claimed effect.")
        if not hypothesis.expected_mechanism:
            raise InvalidHypothesisError(
                "Hypothesis must explain the expected mechanism."
            )
        if not hypothesis.expected_invalidation_triggers:
            raise InvalidHypothesisError(
                "Hypothesis must define invalidation triggers."
            )
        if not hypothesis.benchmark_expectation:
            raise InvalidHypothesisError(
                "Hypothesis must define a benchmark expectation."
            )
        return True
