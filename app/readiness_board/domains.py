from typing import List
from app.readiness_board.enums import ReadinessDomain, DomainVerdict, EvidenceClass
from app.readiness_board.models import EvidenceSubmission, ReadinessDomainVerdict


class DomainEvaluator:
    def evaluate(
        self, domain: ReadinessDomain, evidence: List[EvidenceSubmission]
    ) -> ReadinessDomainVerdict:
        if domain == ReadinessDomain.POLICY:
            return self._evaluate_policy(evidence)
        elif domain == ReadinessDomain.MARKET_TRUTH:
            return self._evaluate_market_truth(evidence)
        elif domain == ReadinessDomain.SHADOW_TRUTHFULNESS:
            return self._evaluate_shadow(evidence)
        # Default fallback
        return ReadinessDomainVerdict(
            domain=domain,
            verdict=DomainVerdict.UNKNOWN,
            blockers=["Domain evaluator not fully implemented"],
        )

    def _evaluate_policy(
        self, evidence: List[EvidenceSubmission]
    ) -> ReadinessDomainVerdict:
        policy_evidences = [
            e
            for e in evidence
            if e.evidence_class == EvidenceClass.POLICY_DECISION_PROOFS
        ]
        if not policy_evidences:
            return ReadinessDomainVerdict(
                domain=ReadinessDomain.POLICY,
                verdict=DomainVerdict.UNKNOWN,
                blockers=["No policy evidence found"],
            )

        blockers = []
        caveats = []
        refs = []
        for e in policy_evidences:
            refs.append(e.submission_id)
            if e.content.get("has_hard_blocks", False):
                blockers.append("Hard policy blocks detected")
            if e.content.get("has_warnings", False):
                caveats.append("Policy warnings detected")

        verdict = (
            DomainVerdict.BLOCK
            if blockers
            else (DomainVerdict.CAUTION if caveats else DomainVerdict.PASS)
        )
        return ReadinessDomainVerdict(
            domain=ReadinessDomain.POLICY,
            verdict=verdict,
            blockers=blockers,
            caveats=caveats,
            evidence_refs=refs,
        )

    def _evaluate_market_truth(
        self, evidence: List[EvidenceSubmission]
    ) -> ReadinessDomainVerdict:
        mt_evidences = [
            e
            for e in evidence
            if e.evidence_class == EvidenceClass.MARKET_TRUTH_EVIDENCE
        ]
        if not mt_evidences:
            return ReadinessDomainVerdict(
                domain=ReadinessDomain.MARKET_TRUTH,
                verdict=DomainVerdict.UNKNOWN,
                blockers=["No market truth evidence found"],
            )

        blockers = []
        refs = []
        for e in mt_evidences:
            refs.append(e.submission_id)
            if e.content.get("stale", False):
                blockers.append("Market truth is stale")

        verdict = DomainVerdict.BLOCK if blockers else DomainVerdict.PASS
        return ReadinessDomainVerdict(
            domain=ReadinessDomain.MARKET_TRUTH,
            verdict=verdict,
            blockers=blockers,
            evidence_refs=refs,
        )

    def _evaluate_shadow(
        self, evidence: List[EvidenceSubmission]
    ) -> ReadinessDomainVerdict:
        sh_evidences = [
            e for e in evidence if e.evidence_class == EvidenceClass.SHADOW_TRUTHFULNESS
        ]
        if not sh_evidences:
            return ReadinessDomainVerdict(
                domain=ReadinessDomain.SHADOW_TRUTHFULNESS,
                verdict=DomainVerdict.UNKNOWN,
                caveats=["No shadow evidence found"],
            )
        return ReadinessDomainVerdict(
            domain=ReadinessDomain.SHADOW_TRUTHFULNESS,
            verdict=DomainVerdict.PASS,
            evidence_refs=[e.submission_id for e in sh_evidences],
        )
