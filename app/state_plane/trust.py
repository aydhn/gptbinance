from .models import StateTrustVerdict
from .registry import state_registry
from .enums import TrustVerdict

def evaluate_trust(state_id: str) -> StateTrustVerdict:
    obj = state_registry.get_object(state_id)
    if not obj:
        raise ValueError(f"State object {state_id} not found")

    reasons = []
    verdict = TrustVerdict.TRUSTED

    # Priority 1: BLOCKED
    if obj.split_brain:
        verdict = TrustVerdict.BLOCKED
        reasons.append("Split-brain detected")

    # Priority 2: CAUTION
    elif obj.reconciled and not obj.reconciled.is_converged:
        verdict = TrustVerdict.CAUTION
        reasons.append("State not converged")

    # Priority 3: DEGRADED
    elif not obj.transitions:
        verdict = TrustVerdict.DEGRADED
        reasons.append("No transition lineage")

    # Accumulate all reasons even if priority changes
    if obj.split_brain and not obj.transitions:
        pass # Already blocked, just ensuring logic is clear, reasons handled above if we want all

    if obj.split_brain:
        verdict = TrustVerdict.BLOCKED
    elif obj.reconciled and not obj.reconciled.is_converged:
        verdict = TrustVerdict.CAUTION
    elif not obj.transitions:
        verdict = TrustVerdict.DEGRADED

    # More robust accumulation
    final_verdict = TrustVerdict.TRUSTED
    final_reasons = []

    if not obj.transitions:
        final_verdict = TrustVerdict.DEGRADED
        final_reasons.append("No transition lineage")

    if obj.reconciled and not obj.reconciled.is_converged:
        final_verdict = TrustVerdict.CAUTION
        final_reasons.append("State not converged")

    if obj.split_brain:
        final_verdict = TrustVerdict.BLOCKED
        final_reasons.append("Split-brain detected")

    return StateTrustVerdict(
        state_id=state_id,
        verdict=final_verdict.value,
        reasons=final_reasons
    )
