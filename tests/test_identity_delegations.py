import pytest
from uuid import uuid4
from datetime import datetime, timedelta, timezone
from app.identity.enums import CapabilityClass
from app.identity.delegations import delegation_manager


def test_delegation_non_delegable():
    delegator = uuid4()
    delegatee = uuid4()
    future = datetime.now(timezone.utc) + timedelta(hours=1)

    with pytest.raises(ValueError, match="is non-delegable"):
        delegation_manager.delegate(
            delegator, delegatee, [CapabilityClass.FINALIZE_POSTMORTEM], future
        )


def test_delegation_success():
    delegator = uuid4()
    delegatee = uuid4()
    future = datetime.now(timezone.utc) + timedelta(hours=1)

    record = delegation_manager.delegate(
        delegator, delegatee, [CapabilityClass.REQUEST_REVIEW], future
    )
    assert record is not None
