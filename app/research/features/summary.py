from app.research.features.models import FeatureSet


class FeatureSummaryGenerator:
    @staticmethod
    def generate_summary(feature_set: FeatureSet) -> str:
        report = feature_set.report
        lineage = report.lineage
        quality = report.quality

        lines = []
        lines.append("=" * 50)
        lines.append(f"FEATURE SET SUMMARY: {feature_set.name}")
        lines.append("=" * 50)
        lines.append(f"Symbol: {lineage.symbol}")
        lines.append(f"Interval: {lineage.interval}")
        lines.append(f"Run ID: {lineage.run_id}")
        lines.append(f"Timestamp: {lineage.timestamp.isoformat()}")
        lines.append(f"Generation Time: {report.generation_time_ms:.2f} ms")
        lines.append("-" * 50)
        lines.append(f"Quality Status: {quality.status.value.upper()}")
        lines.append(f"Overall Null %: {quality.null_percentage:.2f}%")
        lines.append(f"Leakage Checks Passed: {quality.leakage_checks_passed}")

        if quality.warnings:
            lines.append("Warnings:")
            for w in quality.warnings:
                lines.append(f"  - {w}")

        lines.append("-" * 50)
        lines.append("Columns:")
        for col in lineage.columns_meta:
            lines.append(f"  - {col.column_name}")
            lines.append(f"    Spec: {col.spec.name} ({col.spec.category.value})")
            lines.append(f"    Null Count: {col.null_count}")
            lines.append(f"    Warmup Period: {col.warmup_period}")

        lines.append("=" * 50)
        return "\n".join(lines)
