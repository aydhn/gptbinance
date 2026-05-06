from uuid import uuid4
from app.identity.separation import sod_checker


def test_sod_conflict():
    user_a = uuid4()
    user_b = uuid4()

    # Same producer and reviewer
    assert sod_checker.check_conflict(user_a, user_a) == True

    # Different
    assert sod_checker.check_conflict(user_a, user_b) == False

    # Producer is adjudicator
    assert sod_checker.check_conflict(user_a, user_b, user_a) == True
