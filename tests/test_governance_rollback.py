from app.governance.rollback import RollbackManager
from app.governance.candidate_assembler import CandidateAssembler


def test_rollback_ref_creation():
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {})
    rm = RollbackManager()
    ref = rm.prepare_rollback_ref(bundle)
    assert ref.bundle_id == bundle.bundle_id
