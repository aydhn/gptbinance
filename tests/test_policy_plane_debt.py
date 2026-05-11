import pytest
from app.policy_plane.debt import record_waiver_debt


def test_record_waiver_debt():
    debt = record_waiver_debt("waiver-123", "Expired waiver")
    assert debt.source_type == "waiver"
    assert debt.source_id == "waiver-123"
    assert debt.resolved is False
