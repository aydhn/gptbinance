from app.governance.storage import GovernanceStorage
from app.governance.candidate_assembler import CandidateAssembler


def test_storage():
    storage = GovernanceStorage()
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {})
    storage.save_bundle(bundle)
    assert bundle.bundle_id in storage.bundles
