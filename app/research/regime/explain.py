from app.research.regime.models import (
    RegimeEvaluationResult,
    RegimeTransition,
    RegimeContext,
)


def explain_evaluation(eval_result: RegimeEvaluationResult) -> str:
    """Returns a human-readable explanation of an evaluation."""
    exp = f"[{eval_result.label.family.name}] Evaluated as {eval_result.label.name} "
    exp += f"(Score: {eval_result.score.score:.2f}, Quality: {eval_result.quality.quality.name}).\n"
    exp += f"Rationale: {eval_result.rationale}\n"
    if eval_result.quality.warnings:
        exp += f"Warnings: {', '.join(eval_result.quality.warnings)}\n"
    return exp


def explain_transition(transition: RegimeTransition) -> str:
    """Returns a human-readable explanation of a transition."""
    return f"[{transition.from_label.family.name}] Transition detected: {transition.from_label.name} -> {transition.to_label.name} ({transition.transition_type.name})"


def explain_context(context: RegimeContext) -> str:
    """Returns a full textual summary of the current regime context."""
    lines = [
        f"=== REGIME CONTEXT ({context.symbol} {context.interval}) @ {context.timestamp} ===",
        f"Overall Quality: {context.overall_quality.name}",
    ]

    lines.append("\nEvaluations:")
    for fam, res in context.evaluations.items():
        lines.append(explain_evaluation(res))

    lines.append("\nRecent Transitions:")
    for fam, trans in context.transitions.items():
        if trans:
            lines.append(explain_transition(trans))
        else:
            lines.append(f"[{fam.name}] No recent transition.")

    lines.append("\nStrategy Suitability:")
    for sfam, comp in context.suitability.compatibilities.items():
        lines.append(
            f"- {sfam}: {comp.verdict.name} (Score: {comp.suitability_score:.2f}) -> {comp.rationale}"
        )

    return "\n".join(lines)
