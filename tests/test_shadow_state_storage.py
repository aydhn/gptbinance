from app.shadow_state.storage import shadow_storage
from app.shadow_state.repository import shadow_repository
from app.shadow_state.twin import twin_assembler
from app.shadow_state.convergence import convergence_engine


def test_shadow_storage():
    twin = twin_assembler.assemble_twin("test", "test")
    run = convergence_engine.run_convergence(twin)

    shadow_repository.save_twin(twin)
    shadow_repository.save_run(run)

    assert shadow_storage._twins[twin.twin_id] == twin
    assert shadow_storage._runs[run.run_id] == run
