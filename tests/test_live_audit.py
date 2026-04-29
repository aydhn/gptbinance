import pytest
from app.execution.live_runtime.audit import LiveAuditWriter
from app.execution.live_runtime.models import LiveAuditRecord, LiveSessionSummary
from app.execution.live_runtime.enums import LiveAuditEventType


def test_live_audit_writer():
    writer = LiveAuditWriter()

    rec = LiveAuditRecord(
        run_id="r1", event_type=LiveAuditEventType.ORDER_SUBMIT, details="Test"
    )
    writer.write_record(rec)

    recs = writer.get_records()
    assert len(recs) == 1
    assert recs[0].event_type == LiveAuditEventType.ORDER_SUBMIT

    summary = LiveSessionSummary(run_id="r1", start_time=None, end_time=None)
    aas = writer.generate_after_action_summary("r1", summary)
    assert aas.run_id == "r1"
    assert len(aas.key_events) == 1
