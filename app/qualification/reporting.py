from app.qualification.models import QualificationRun
from app.qualification.traceability import build_traceability_matrix
import json


def format_qualification_summary(run: QualificationRun) -> str:
    summary = f"=== Qualification Run Summary [{run.run_id}] ===\n"
    summary += f"Profile: {run.profile.value}\n"
    summary += f"Started: {run.started_at}\n"
    summary += f"Completed: {run.completed_at}\n\n"

    if run.score:
        summary += "--- Score Breakdown ---\n"
        summary += f"Overall Score: {run.score.overall_score:.2f}\n"
        summary += f"Golden Path Pass Rate: {run.score.golden_path_pass_rate:.2f}\n"
        summary += f"Negative Test Pass Rate: {run.score.negative_test_pass_rate:.2f}\n"
        summary += f"Contract Verification Score: {run.score.contract_verification_score:.2f}\n"
        summary += f"Evidence Completeness: {run.score.evidence_completeness:.2f}\n"
        summary += f"Critical Findings: {run.score.critical_findings_count}\n"
        summary += f"Waived Findings: {run.score.waived_findings_count}\n\n"

    if run.verdict:
        summary += "--- Verdict ---\n"
        summary += f"Verdict: {run.verdict.verdict.value}\n"
        summary += f"Go/No-Go Recommendation: {run.verdict.go_no_go.value}\n"
        if run.verdict.blockers:
            summary += f"Blockers: {', '.join(run.verdict.blockers)}\n"
        if run.verdict.warnings:
            summary += f"Warnings: {', '.join(run.verdict.warnings)}\n"

    return summary


def format_traceability_matrix() -> str:
    matrix = build_traceability_matrix()
    output = "=== Traceability Matrix ===\n"
    output += (
        f"{'REQ_ID':<10} | {'COVERED':<7} | {'SCENARIOS':<30} | {'EVIDENCE_REFS'}\n"
    )
    output += "-" * 80 + "\n"
    for entry in matrix:
        cov = "YES" if entry.is_covered else "NO"
        scens = ",".join(entry.scenario_ids) if entry.scenario_ids else "N/A"
        evs = ",".join(entry.evidence_refs) if entry.evidence_refs else "N/A"
        output += f"{entry.req_id:<10} | {cov:<7} | {scens:<30} | {evs}\n"
    return output


def format_scenario_results(run: QualificationRun) -> str:
    output = f"=== Scenario Results [{run.run_id}] ===\n"
    for s in run.scenarios:
        status = "PASS" if s.passed else "FAIL"
        output += f"[{status}] {s.scenario_id} ({s.scenario_type.value})\n"
    return output


def format_forbidden_action_results(run: QualificationRun) -> str:
    output = f"=== Forbidden Action Results [{run.run_id}] ===\n"
    for f in run.forbidden_actions:
        status = "BLOCKED" if f.was_blocked else "ALLOWED(FAIL)"
        output += f"[{status}] {f.action_id} - {f.description}\n"
    return output


def format_contract_verification(run: QualificationRun) -> str:
    output = f"=== Contract Verification [{run.run_id}] ===\n"
    for c in run.contracts:
        status = "PASS" if c.passed else "FAIL"
        output += f"[{status}] {c.contract_id}: {c.source_component} -> {c.target_component} ({c.severity.value})\n"
    return output


def format_evidence_pack(run: QualificationRun) -> str:
    output = f"=== Evidence Pack [{run.evidence_pack_id}] for Run [{run.run_id}] ===\n"
    # Placeholder: fetch pack from storage in real implementation
    output += "Pack assembled and validated.\n"
    return output
