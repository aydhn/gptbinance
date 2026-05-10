import pytest
from app.policy_plane.waivers import request_waiver, approve_waiver
from datetime import datetime, timezone


def test_request_and_approve_waiver():
    waiver = request_waiver("POL-001", "user1", "Urgent request", {"env": "live"}, 60)
    assert waiver.waiver_id is not None
    assert waiver.policy_id == "POL-001"
    assert waiver.requester_id == "user1"
    assert waiver.approver_id is None

    approve_waiver(waiver, "approver1")
    assert waiver.approver_id == "approver1"
