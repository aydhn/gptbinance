from app.security.evidence import EvidenceChain
from app.security.enums import EvidenceStatus

def test_evidence_chain(tmp_path):
    chain_file = tmp_path / "chain.jsonl"
    chain = EvidenceChain(storage_path=str(chain_file))

    e1 = chain.append_event("TEST", {"msg": "1"})
    e2 = chain.append_event("TEST", {"msg": "2"})

    assert e2.previous_hash == e1.payload_hash
    assert chain.verify_chain() == EvidenceStatus.VALID
