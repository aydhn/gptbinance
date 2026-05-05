from typing import Dict, List, Optional
from app.readiness_board.models import (
    CandidateRecord,
    CandidateFreezeSnapshot,
    EvidenceSubmission,
    EvidenceAdmissibilityReport,
    ReadinessDossier,
    GoNoGoDecision,
    FinalDecisionMemo,
)


class ReadinessBoardStorage:
    def __init__(self):
        self.candidates: Dict[str, CandidateRecord] = {}
        self.snapshots: Dict[str, CandidateFreezeSnapshot] = {}
        self.evidence: Dict[str, EvidenceSubmission] = {}
        self.admissibility: Dict[str, EvidenceAdmissibilityReport] = {}
        self.dossiers: Dict[str, ReadinessDossier] = {}
        self.decisions: Dict[str, GoNoGoDecision] = {}
        self.memos: Dict[str, FinalDecisionMemo] = {}

    def save_candidate(self, record: CandidateRecord):
        self.candidates[record.candidate_id] = record

    def get_candidate(self, candidate_id: str) -> Optional[CandidateRecord]:
        return self.candidates.get(candidate_id)

    def save_snapshot(self, snapshot: CandidateFreezeSnapshot):
        self.snapshots[snapshot.snapshot_id] = snapshot

    def get_snapshot(self, snapshot_id: str) -> Optional[CandidateFreezeSnapshot]:
        return self.snapshots.get(snapshot_id)

    def get_latest_snapshot(
        self, candidate_id: str
    ) -> Optional[CandidateFreezeSnapshot]:
        snapshots = [
            s
            for s in self.snapshots.values()
            if s.candidate_id == candidate_id and s.is_valid
        ]
        return (
            sorted(snapshots, key=lambda x: x.frozen_at, reverse=True)[0]
            if snapshots
            else None
        )

    def save_evidence(self, evidence: EvidenceSubmission):
        self.evidence[evidence.submission_id] = evidence

    def get_evidence(self, submission_id: str) -> Optional[EvidenceSubmission]:
        return self.evidence.get(submission_id)

    def get_evidence_for_candidate(self, candidate_id: str) -> List[EvidenceSubmission]:
        return [e for e in self.evidence.values() if e.candidate_id == candidate_id]

    def save_admissibility(self, report: EvidenceAdmissibilityReport):
        self.admissibility[report.report_id] = report

    def get_admissibility(
        self, report_id: str
    ) -> Optional[EvidenceAdmissibilityReport]:
        return self.admissibility.get(report_id)

    def save_dossier(self, dossier: ReadinessDossier):
        self.dossiers[dossier.dossier_id] = dossier

    def get_dossier(self, dossier_id: str) -> Optional[ReadinessDossier]:
        return self.dossiers.get(dossier_id)

    def save_decision(self, decision: GoNoGoDecision):
        self.decisions[decision.decision_id] = decision

    def get_decision(self, decision_id: str) -> Optional[GoNoGoDecision]:
        return self.decisions.get(decision_id)

    def get_latest_decision(self, candidate_id: str) -> Optional[GoNoGoDecision]:
        # simplified mapping via dossier
        dossiers_for_candidate = {
            d.dossier_id: d
            for d in self.dossiers.values()
            if d.candidate_id == candidate_id
        }
        decisions = [
            d for d in self.decisions.values() if d.dossier_id in dossiers_for_candidate
        ]
        return (
            sorted(decisions, key=lambda x: x.decided_at, reverse=True)[0]
            if decisions
            else None
        )

    def save_memo(self, memo: FinalDecisionMemo):
        self.memos[memo.memo_id] = memo

    def get_memo(self, memo_id: str) -> Optional[FinalDecisionMemo]:
        return self.memos.get(memo_id)
