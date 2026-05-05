from app.readiness_board.models import (
    CandidateRecord,
    ReadinessDossier,
    GoNoGoDecision,
    FinalDecisionMemo,
)


class ReportingFormatter:
    @staticmethod
    def format_candidate(record: CandidateRecord) -> str:
        return f"Candidate [{record.candidate_id}]\nClass: {record.candidate_class.value}\nScope: {record.scope.model_dump()}"

    @staticmethod
    def format_dossier(dossier: ReadinessDossier) -> str:
        out = [f"Dossier [{dossier.dossier_id}] for Candidate [{dossier.candidate_id}]"]
        out.append(f"Snapshot: {dossier.snapshot_id}")
        out.append("Domain Verdicts:")
        for dom, v in dossier.domain_verdicts.items():
            out.append(
                f"  - {dom.value}: {v.verdict.value} (Blockers: {len(v.blockers)}, Caveats: {len(v.caveats)})"
            )
        out.append(f"Admissible Evidence: {len(dossier.admissible_evidence_refs)}")
        out.append(f"Inadmissible Evidence: {len(dossier.inadmissible_evidence_refs)}")
        out.append(f"Conflicts: {len(dossier.conflicts)}")
        return "\n".join(out)

    @staticmethod
    def format_decision(decision: GoNoGoDecision) -> str:
        out = [f"Decision [{decision.decision_id}]"]
        out.append(f"Verdict: {decision.verdict.value}")
        out.append(f"Rationale: {decision.rationale}")
        if decision.conditional_terms:
            out.append(f"Conditions: {decision.conditional_terms.conditions}")
            out.append(f"Scope: {[s.value for s in decision.conditional_terms.scopes]}")
            out.append(f"Expires: {decision.conditional_terms.expires_at}")
        return "\n".join(out)

    @staticmethod
    def format_memo(memo: FinalDecisionMemo) -> str:
        out = [f"Memo [{memo.memo_id}] ({memo.memo_class.value})"]
        out.append(f"Summary: {memo.executive_summary}")
        out.append(f"Accepted Risks: {memo.accepted_risks}")
        out.append(f"Next Steps: {memo.next_steps}")
        return "\n".join(out)
