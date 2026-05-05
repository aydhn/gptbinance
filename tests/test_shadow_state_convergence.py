from app.shadow_state.convergence import convergence_engine
from app.shadow_state.twin import twin_assembler


def test_convergence_engine():
    twin = twin_assembler.assemble_twin("test_prof", "test_ws")
    run = convergence_engine.run_convergence(twin)
    assert run.global_verdict.value == "clean"
