import pytest
from app.policy_plane.actions import create_execute_action, create_approve_action
from app.policy_plane.enums import ActionClass


def test_execute_action():
    act = create_execute_action()
    assert act.action_class == ActionClass.EXECUTE


def test_approve_action():
    act = create_approve_action()
    assert act.action_class == ActionClass.APPROVE
