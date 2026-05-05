import json
from app.data_governance.models import (
    DataContract,
    DataSchema,
    DatasetQualityReport,
    SchemaDiffReport,
    TrustVerdict,
    DownstreamImpactReport,
)


class GovernanceReporter:
    @staticmethod
    def format_contract(contract: DataContract) -> str:
        return f"Contract ID: {contract.contract_id}\nType: {contract.contract_type.value}\nSchema: {contract.schema_ref.schema_id} (v{contract.schema_ref.version})\nRequired Fields: {', '.join(contract.required_fields)}"

    @staticmethod
    def format_schema(schema: DataSchema) -> str:
        fields_str = "\n  ".join(
            [f"- {f.name}: {f.dtype} (Nullable: {f.nullable})" for f in schema.fields]
        )
        return f"Schema ID: {schema.schema_id}\nVersion: {schema.version}\nFields:\n  {fields_str}"

    @staticmethod
    def format_quality_report(report: DatasetQualityReport) -> str:
        score_pct = report.overall_score * 100
        lines = [
            f"Quality Report for {report.dataset_ref.dataset_id} (v{report.dataset_ref.version})",
            f"Run ID: {report.run_id}",
            f"Status: {report.status.value} (Score: {score_pct:.1f}%)",
            f"Breakdown: {report.breakdown.passed_rules}/{report.breakdown.total_rules} passed",
            "Rule Results:",
        ]
        for res in report.results:
            status_marker = "✓" if res.passed else "✗"
            lines.append(
                f"  [{status_marker}] {res.rule_name} (Severity: {res.severity.value}) - {res.evidence}"
            )
        return "\n".join(lines)

    @staticmethod
    def format_trust_verdict(verdict: TrustVerdict) -> str:
        score_pct = verdict.score * 100
        lines = [
            f"Trust Verdict for {verdict.dataset_ref.dataset_id} (v{verdict.dataset_ref.version})",
            f"Verdict: {verdict.verdict.value} (Score: {score_pct:.1f}%)",
            "Reasons:",
        ]
        if verdict.reasons:
            for r in verdict.reasons:
                lines.append(f"  - {r}")
        else:
            lines.append("  None")
        lines.append("Evidence:")
        for k, v in verdict.evidence_breakdown.items():
            lines.append(f"  - {k}: {v}")
        lines.append(f"\nRecommendation: {verdict.usage_recommendation}")
        return "\n".join(lines)

    @staticmethod
    def format_impact_report(report: DownstreamImpactReport) -> str:
        lines = [
            f"Impact Report for {report.dataset_ref.dataset_id} (v{report.dataset_ref.version})",
            f"Severity: {report.severity.value}",
            f"Impacted Components: {', '.join(report.impacted_components) if report.impacted_components else 'None'}",
            f"Recommended Checks: {', '.join(report.recommended_checks) if report.recommended_checks else 'None'}",
            f"Likely Blockers: {', '.join(report.likely_blockers) if report.likely_blockers else 'None'}",
        ]
        return "\n".join(lines)

    @staticmethod
    def format_schema_diff(report: SchemaDiffReport) -> str:
        lines = [
            f"Schema Diff: {report.from_schema.schema_id} (v{report.from_schema.version}) -> {report.to_schema.schema_id} (v{report.to_schema.version})",
            f"Breaking Change: {'Yes' if report.is_breaking else 'No'}",
            "Changes:",
        ]
        has_changes = False
        for change_type, items in report.changes.items():
            if items:
                has_changes = True
                lines.append(f"  {change_type.value}:")
                for item in items:
                    lines.append(f"    - {item}")
        if not has_changes:
            lines.append("  No changes detected.")
        return "\n".join(lines)
