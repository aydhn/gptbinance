import pytest
from uuid import uuid4
from datetime import datetime, timedelta, timezone
from app.identity.enums import SessionClass
from app.identity.sessions import session_manager


def test_session_validity():
    principal_id = uuid4()
    future = datetime.now(timezone.utc) + timedelta(hours=1)
    past = datetime.now(timezone.utc) - timedelta(hours=1)

    valid_session = session_manager.issue_session(
        principal_id, SessionClass.REVIEW, future
    )
    assert session_manager.validate_session(valid_session.session_id) == True

    expired_session = session_manager.issue_session(
        principal_id, SessionClass.REVIEW, past
    )
    assert session_manager.validate_session(expired_session.session_id) == False
