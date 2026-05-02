from typing import List
from app.control.models import ApprovalRecord, CommandJournalEntry


class ControlReporter:
    @staticmethod
    def format_pending_approvals(records: List[ApprovalRecord]) -> str:
        if not records:
            return "No pending approvals."
        lines = ["Pending Approvals:"]
        for r in records:
            lines.append(
                f"  - [{r.request.id}] {r.request.action_type.value} by {r.request.requester.id}"
            )
        return "\n".join(lines)

    @staticmethod
    def format_journal(entries: List[CommandJournalEntry]) -> str:
        if not entries:
            return "Journal is empty."
        lines = ["Command Journal:"]
        for e in entries:
            lines.append(
                f"  - [{e.timestamp.isoformat()}] Req: {e.request_id} | Action: {e.action_type.value} | Status: {e.status.value}"
            )
        return "\n".join(lines)


reporter = ControlReporter()
