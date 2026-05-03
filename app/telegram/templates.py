# Placeholder for templates
REPLAY_COMPLETED_TEMPLATE = "Replay {run_id} completed. Verdict: {verdict}"
REPLAY_MISMATCH_TEMPLATE = "Mismatch detected in replay {run_id}."
FORENSIC_SUMMARY_TEMPLATE = "Forensic bundle ready for replay {run_id}."
REPLAYABILITY_LOW_TEMPLATE = "Low replayability score for {run_id}."
COUNTERFACTUAL_CAUTION_TEMPLATE = (
    "Counterfactual caution for {run_id}: this is not historical data."
)


class KnowledgeTemplates:
    @staticmethod
    def stale_runbook_warning(item_id: str, severity: str, warnings: list) -> str:
        w_str = "\n".join(f"- {w}" for w in warnings)
        return (
            f"🚨 [STALE KNOWLEDGE] {item_id}\nSeverity: {severity}\nWarnings:\n{w_str}"
        )

    @staticmethod
    def lesson_adopted(item_id: str, title: str) -> str:
        return f"📚 [LESSON ADOPTED] {item_id}\nTitle: {title}"

    @staticmethod
    def readiness_expiring(operator_id: str, reasons: list) -> str:
        r_str = "\n".join(f"- {r}" for r in reasons)
        return f"⚠️ [READINESS EXPIRING] {operator_id}\nReasons:\n{r_str}"

    @staticmethod
    def knowledge_gap(action_type: str) -> str:
        return (
            f"⚠️ [KNOWLEDGE GAP] Missing applicable runbook for action: {action_type}"
        )
