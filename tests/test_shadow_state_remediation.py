from app.shadow_state.remediation import remediation_planner
from app.shadow_state.convergence import convergence_engine
from app.shadow_state.twin import twin_assembler


def test_remediation_planner():
    twin = twin_assembler.assemble_twin("test", "test")
    run = convergence_engine.run_convergence(twin)
    plan = remediation_planner.plan(run)
    assert not plan.requires_review
    assert len(plan.steps) == 0
