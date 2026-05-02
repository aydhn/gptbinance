from app.qualification.contracts import ContractVerifier


def test_contract_verifier():
    verifier = ContractVerifier()
    results = verifier.verify_contracts()
    assert len(results) > 0
    assert all(r.passed for r in results)
