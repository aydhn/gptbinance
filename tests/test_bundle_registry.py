from app.governance.bundle_registry import BundleRegistry
from app.governance.candidate_assembler import CandidateAssembler
from app.governance.enums import BundleStage


def test_registry():
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {})

    registry = BundleRegistry()
    registry.register(bundle)

    retrieved = registry.get(bundle.bundle_id)
    assert retrieved == bundle

    registry.update_stage(bundle.bundle_id, BundleStage.REVIEWED)
    assert registry.get(bundle.bundle_id).stage_state.stage == BundleStage.REVIEWED
