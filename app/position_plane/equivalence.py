from app.position_plane.models import PositionState, PositionEquivalenceReport
from app.position_plane.enums import EquivalenceVerdict
import uuid


class EquivalenceChecker:
    @staticmethod
    def check_equivalence(
        env_a: str, env_b: str, state_a: PositionState, state_b: PositionState
    ) -> PositionEquivalenceReport:
        verdict = EquivalenceVerdict.EQUIVALENT
        discrepancies = []

        if state_a.quantity != state_b.quantity:
            verdict = EquivalenceVerdict.DIVERGENT
            discrepancies.append(
                f"Quantity mismatch: {state_a.quantity} vs {state_b.quantity}"
            )

        if state_a.average_entry_price != state_b.average_entry_price:
            if verdict == EquivalenceVerdict.EQUIVALENT:
                verdict = EquivalenceVerdict.PARTIAL
            discrepancies.append(
                f"Cost basis mismatch: {state_a.average_entry_price} vs {state_b.average_entry_price}"
            )

        return PositionEquivalenceReport(
            report_id=str(uuid.uuid4()),
            symbol=state_a.symbol,
            verdict=verdict,
            environment_a=env_a,
            environment_b=env_b,
            discrepancies=discrepancies,
        )
