from app.shadow_state.twin import twin_assembler


def test_twin_assembler():
    twin = twin_assembler.assemble_twin("test_prof", "test_ws")
    assert twin.venue_truth is not None
    assert twin.local_derived is not None
