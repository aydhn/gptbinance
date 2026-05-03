from app.replay.models import DecisionReplayResult


def format_summary(result: DecisionReplayResult) -> str:
    lines = [
        f"--- Replay Run: {result.run_id} ---",
        f"Scope: {result.config.scope.value}",
        f"Mode: {result.config.mode.value}",
        f"Verdict: {result.replayability_score.verdict.value}",
        f"Reproducibility: {result.reproducibility.status.value}",
        f"Diffs: {len(result.diffs)}",
        f"Counterfactuals: {len(result.counterfactual_results)}",
    ]
    return "\n".join(lines)


def format_timeline(result: DecisionReplayResult) -> str:
    lines = [f"--- Timeline for {result.run_id} ---"]
    for ev in result.timeline.events:
        lines.append(
            f"[{ev.timestamp.isoformat()}] {ev.event_type.value} from {ev.component_ref}"
        )
    return "\n".join(lines)


def format_decision_path(result: DecisionReplayResult) -> str:
    lines = [f"--- Decision Path for {result.run_id} ---"]
    for p in result.decision_path:
        lines.append(f"Stage: {p.stage} -> Decision: {p.decision}")
    return "\n".join(lines)


def format_diff(result: DecisionReplayResult) -> str:
    lines = [f"--- Diffs for {result.run_id} ---"]
    if not result.diffs:
        lines.append("No diffs found.")
    for d in result.diffs:
        lines.append(f"{d.severity.value.upper()}: {d.stage} - {d.description}")
    return "\n".join(lines)


def format_counterfactual_summary(result: DecisionReplayResult) -> str:
    lines = [f"--- Counterfactual Summary for {result.run_id} ---"]
    if not result.counterfactual_results:
        lines.append("No counterfactuals run.")
    for c in result.counterfactual_results:
        lines.append(f"Type: {c.spec.type.value}")
        lines.append(f"Historical: {c.historical_outcome}")
        lines.append(f"Counterfactual: {c.counterfactual_outcome}")
        lines.append("---")
    return "\n".join(lines)


def format_replayability_score(result: DecisionReplayResult) -> str:
    lines = [f"--- Replayability Score for {result.run_id} ---"]
    score = result.replayability_score
    lines.append(f"Overall: {score.overall_score}")
    lines.append(f"Verdict: {score.verdict.value}")
    lines.append(f"Source Completeness: {score.source_completeness}")
    return "\n".join(lines)
