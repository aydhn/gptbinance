from app.readiness_board.domains import DomainEvaluator
from app.readiness_board.models import EvidenceSubmission
from app.readiness_board.enums import ReadinessDomain, EvidenceClass, DomainVerdict


def test_domain_policy_evaluator():
    evaluator = DomainEvaluator()
    ev_pass = EvidenceSubmission(
        submission_id="s1",
        candidate_id="c1",
        evidence_class=EvidenceClass.POLICY_DECISION_PROOFS,
        content={"has_hard_blocks": False},
        source_ref="src",
    )
    res1 = evaluator.evaluate(ReadinessDomain.POLICY, [ev_pass])
    assert res1.verdict == DomainVerdict.PASS

    ev_block = EvidenceSubmission(
        submission_id="s2",
        candidate_id="c1",
        evidence_class=EvidenceClass.POLICY_DECISION_PROOFS,
        content={"has_hard_blocks": True},
        source_ref="src",
    )
    res2 = evaluator.evaluate(ReadinessDomain.POLICY, [ev_block])
    assert res2.verdict == DomainVerdict.BLOCK


def test_domain_market_truth_evaluator():
    evaluator = DomainEvaluator()
    ev = EvidenceSubmission(
        submission_id="s1",
        candidate_id="c1",
        evidence_class=EvidenceClass.MARKET_TRUTH_EVIDENCE,
        content={"stale": True},
        source_ref="src",
    )
    res = evaluator.evaluate(ReadinessDomain.MARKET_TRUTH, [ev])
    assert res.verdict == DomainVerdict.BLOCK
