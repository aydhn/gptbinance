from app.execution_plane.guards import ExecutionGuards


def test_guards():
    res1 = ExecutionGuards.check_preflight_guards(True, True, True, False)
    assert len(res1) == 0

    res2 = ExecutionGuards.check_preflight_guards(False, True, True, False)
    assert "allocation_not_trusted" in res2
