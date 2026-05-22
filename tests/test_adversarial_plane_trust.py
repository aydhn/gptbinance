import pytest
from app.adversarial_plane.trust import DefaultTrustEvaluator
from app.adversarial_plane.enums import TrustVerdict

def test_trust_evaluator():
    evaluator = DefaultTrustEvaluator()
    verdict1 = evaluator.evaluate({"verdict_id": "v1", "blockers": ["exploit_path_found"]})
    assert verdict1.verdict == TrustVerdict.BLOCKED

    verdict2 = evaluator.evaluate({"verdict_id": "v2", "caveats": ["weak_suspicion"]})
    assert verdict2.verdict == TrustVerdict.CAUTION

    verdict3 = evaluator.evaluate({"verdict_id": "v3"})
    assert verdict3.verdict == TrustVerdict.TRUSTED

import os
