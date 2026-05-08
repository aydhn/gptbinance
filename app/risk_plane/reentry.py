import uuid

from .models import ReentryGate, RiskState
from .enums import RiskDomain


class ReentryEvaluator:
    def evaluate(
        self,
        domain: RiskDomain,
        target_id: str,
        state: RiskState,
        active_cooldowns: bool,
    ) -> ReentryGate:
        requirements = []
        cleared = True
        proof_notes = []

        if active_cooldowns:
            requirements.append("Cooldown period must expire.")
            cleared = False
            proof_notes.append("Active cooldown blocks reentry.")

        if not state.authoritative:
            requirements.append("Authoritative risk state required.")
            cleared = False
            proof_notes.append("State is approximate, blocking reentry.")

        if state.liquidation and state.liquidation.liquidation_class in [
            "PROXIMITY",
            "CRITICAL",
        ]:
            requirements.append("Liquidation risk must be SAFE or WARNING.")
            cleared = False
            proof_notes.append("Liquidation proximity blocks reentry.")

        if cleared:
            proof_notes.append("All gates cleared.")

        return ReentryGate(
            gate_id=str(uuid.uuid4()),
            target_domain=domain,
            target_id=target_id,
            requirements=requirements,
            cleared=cleared,
            proof_notes=proof_notes,
        )
