from app.policy_kernel.models import PolicyContext


def detect_stale_context(context: PolicyContext) -> bool:
    # Logic to check if context elements are stale based on timestamps or flags
    # E.g., if context.event_overlay has old timestamps
    return False


def calculate_context_completeness(context: PolicyContext) -> float:
    # A simple score based on populated fields
    fields = [
        context.capital_posture,
        context.event_overlay,
        context.stress_overlay,
        context.cross_book_posture,
        context.qualification_status,
        context.shadow_truthfulness,
        context.lifecycle_health,
        context.remediation_debt,
    ]
    populated = sum(1 for f in fields if f)
    return (populated / len(fields)) * 100


def assemble_policy_context(
    action_type: str, workspace_id: str, profile_id: str, mode: str, **kwargs
) -> PolicyContext:
    return PolicyContext(
        action_type=action_type,
        workspace_id=workspace_id,
        profile_id=profile_id,
        mode=mode,
        capital_posture=kwargs.get("capital_posture", {}),
        event_overlay=kwargs.get("event_overlay", {}),
        stress_overlay=kwargs.get("stress_overlay", {}),
        cross_book_posture=kwargs.get("cross_book_posture", {}),
        qualification_status=kwargs.get("qualification_status", {}),
        shadow_truthfulness=kwargs.get("shadow_truthfulness", {}),
        lifecycle_health=kwargs.get("lifecycle_health", {}),
        remediation_debt=kwargs.get("remediation_debt", {}),
        approvals=kwargs.get("approvals", []),
    )
