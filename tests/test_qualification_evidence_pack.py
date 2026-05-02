from app.qualification.evidence_pack import EvidencePackAssembler


def test_evidence_pack_assembler():
    assembler = EvidencePackAssembler()
    pack = assembler.assemble("run-123", ["security_refs"])
    assert pack.run_id == "run-123"
    assert len(pack.security_refs) > 0
    assert pack.is_complete is True
