import pytest
from app.migration_plane.trust import TrustManager, TrustEvaluator
from app.migration_plane.enums import TrustVerdict

def test_trust_manager():
    evaluator = TrustEvaluator()
    manager = TrustManager(evaluator)
    result = manager.generate_verdict("mig_001")
    assert result.verdict == TrustVerdict.TRUSTED
