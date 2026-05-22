from typing import Dict, Any

class ComplianceFindings:
    @staticmethod
    def generate_findings(context: Dict[str, Any]) -> list:
        findings = []
        if context.get("attestation_laundering"):
            findings.append("attestation_laundering_detected")
        if context.get("documentation_gaming"):
            findings.append("documentation_gaming_detected")
        return findings
