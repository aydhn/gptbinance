from app.control.journal import journal
from app.control.models import CommandJournalEntry
from app.control.enums import SensitiveActionType, CommandStatus
from datetime import datetime, timezone


def test_journal_append():
    entry = CommandJournalEntry(
        id="j-123",
        request_id="req-123",
        action_type=SensitiveActionType.START_LIVE_SESSION,
        requester_id="op1",
        status=CommandStatus.REQUESTED,
        timestamp=datetime.now(timezone.utc),
    )
    journal.append(entry)
    entries = journal.get_all()
    assert len(entries) > 0
    assert entries[-1].id == "j-123"
