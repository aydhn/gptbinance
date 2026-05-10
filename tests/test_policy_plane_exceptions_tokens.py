import pytest
from app.policy_plane.exceptions_tokens import issue_scoped_exception
from app.policy_plane.enums import ExceptionClass


def test_issue_scoped_exception():
    exception = issue_scoped_exception(
        "POL-002", "admin", "Hotfix", 120, {"stage": "probation"}
    )
    assert exception.exception_id is not None
    assert exception.exception_class == ExceptionClass.SCOPED
    assert exception.policy_id == "POL-002"
    assert exception.issuer_id == "admin"
    assert exception.ttl_minutes == 120
    assert exception.scope_constraints == {"stage": "probation"}
