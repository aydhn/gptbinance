# Mock Telegram Templates
def format_qualification_completed(run_id: str, profile: str, verdict: str) -> str:
    return (
        f"🟢 Qualification Completed [{run_id}]\nProfile: {profile}\nVerdict: {verdict}"
    )


def format_certification_blocked(run_id: str, profile: str, blockers: list) -> str:
    return f"🔴 Certification BLOCKED [{run_id}]\nProfile: {profile}\nBlockers: {', '.join(blockers)}"


def format_forbidden_action_failed(run_id: str, action: str) -> str:
    return (
        f"🔴 Forbidden Action Verification FAILED [{run_id}]\nAction allowed: {action}"
    )


def format_evidence_incomplete(run_id: str) -> str:
    return f"⚠️ Evidence Pack Incomplete [{run_id}]"


def format_waiver_expiring(waiver_id: str, finding_id: str) -> str:
    return f"⚠️ Waiver Expiring Soon\nWaiver: {waiver_id}\nFinding: {finding_id}"


def format_go_no_go_summary(run_id: str, profile: str, go_no_go: str) -> str:
    return f"📋 Go/No-Go Summary [{run_id}]\nProfile: {profile}\nRecommendation: {go_no_go}"
