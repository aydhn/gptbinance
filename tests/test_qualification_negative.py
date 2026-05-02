from app.qualification.negative import ForbiddenActionRunner


def test_forbidden_action_runner():
    runner = ForbiddenActionRunner()
    results = runner.run_forbidden_checks(["stale_approval_deny"])
    assert len(results) > 0
    assert all(r.was_blocked for r in results)
