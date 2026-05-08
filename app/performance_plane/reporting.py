from app.performance_plane.models import (
    PerformanceManifest,
    ReturnSurface,
    AttributionTree,
    PerformanceTrustVerdict,
    BenchmarkRelativeReport,
)


class PerformanceReporter:
    @staticmethod
    def format_manifest_summary(manifest: PerformanceManifest) -> str:
        return f"Manifest [{manifest.manifest_id}] Window: {manifest.window.window_class.value} Complete: {manifest.window.is_complete}"

    @staticmethod
    def format_return_summary(surface: ReturnSurface) -> str:
        return f"Return [{surface.surface_id}] Domain: {surface.domain.value} Target: {surface.target_id} Value: {surface.value} {surface.currency}"

    @staticmethod
    def format_attribution_summary(tree: AttributionTree) -> str:
        lines = [f"Attribution [{tree.tree_id}] for Surface [{tree.surface_id}]:"]
        for node in tree.nodes:
            lines.append(
                f"  - {node.attribution_class.value}: {node.contribution_value} {node.currency}"
            )
        lines.append(f"  - RESIDUAL: {tree.residual_value} {tree.currency}")
        return "\n".join(lines)

    @staticmethod
    def format_trust_summary(verdict: PerformanceTrustVerdict) -> str:
        blockers_str = ", ".join(verdict.blockers) if verdict.blockers else "None"
        return f"Trust [{verdict.verdict_id}] Verdict: {verdict.verdict.value} Blockers: {blockers_str}"

    @staticmethod
    def format_benchmark_relative(report: BenchmarkRelativeReport) -> str:
        cautions = (
            ", ".join(report.mismatch_cautions) if report.mismatch_cautions else "None"
        )
        return f"Benchmark Relative [{report.report_id}] Value: {report.relative_value} Cautions: {cautions}"
