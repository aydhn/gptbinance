from app.telegram.templates import (
    format_qualification_completed,
    format_certification_blocked,
    format_forbidden_action_failed,
    format_evidence_incomplete,
    format_waiver_expiring,
    format_go_no_go_summary,
)


class QualificationNotifier:
    def notify_completed(self, run_id: str, profile: str, verdict: str):
        print(f"TELEGRAM: {format_qualification_completed(run_id, profile, verdict)}")

    def notify_blocked(self, run_id: str, profile: str, blockers: list):
        print(f"TELEGRAM: {format_certification_blocked(run_id, profile, blockers)}")

    def notify_forbidden_failed(self, run_id: str, action: str):
        print(f"TELEGRAM: {format_forbidden_action_failed(run_id, action)}")

    def notify_evidence_incomplete(self, run_id: str):
        print(f"TELEGRAM: {format_evidence_incomplete(run_id)}")

    def notify_waiver_expiring(self, waiver_id: str, finding_id: str):
        print(f"TELEGRAM: {format_waiver_expiring(waiver_id, finding_id)}")

    def notify_go_no_go(self, run_id: str, profile: str, go_no_go: str):
        print(f"TELEGRAM: {format_go_no_go_summary(run_id, profile, go_no_go)}")
