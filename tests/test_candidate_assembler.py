from app.governance.candidate_assembler import CandidateAssembler


def test_candidate_assembler():
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {"strategy_presets": ["p1"]})
    assert bundle.bundle_id.startswith("bundle_")
    assert bundle.spec.strategy_preset_refs == ["p1"]
    assert bundle.lineage.refresh_run_id == "run1"
