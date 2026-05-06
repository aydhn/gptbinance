import json
from app.supply_chain.models import SupplyChainEvidenceBundle


class SupplyChainReporter:
    def generate_summary(self, bundle: SupplyChainEvidenceBundle) -> str:
        report = []
        report.append("=== SUPPLY CHAIN INTEGRITY SUMMARY ===")
        report.append(f"Artifact ID: {bundle.artifact_id}")
        report.append(f"Trust Verdict: {bundle.verdict.verdict.value.upper()}")
        report.append("\nTrust Factors:")
        for k, v in bundle.verdict.factors.items():
            report.append(f"  - {k}: {v}")

        report.append(
            "\nProvenance Completeness: " + str(bundle.provenance.completeness_score)
        )
        report.append(f"Attestations: {len(bundle.attestations)}")
        report.append(f"Lock Integrity Intact: {bundle.lock_integrity.is_intact}")

        if bundle.reproducibility:
            report.append(
                f"Reproducibility: {bundle.reproducibility.reproducibility_class.value}"
            )

        return "\n".join(report)
