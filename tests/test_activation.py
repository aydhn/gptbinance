from app.governance.activation import ActivationManager
from app.governance.candidate_assembler import CandidateAssembler


def test_activation_handoff():
    assembler = CandidateAssembler()
    bundle = assembler.assemble("run1", {})
    manager = ActivationManager()
    report = manager.simulate_handoff(bundle, "paper")
    assert not report.is_ready  # Missing rollback and stage isn't approved
