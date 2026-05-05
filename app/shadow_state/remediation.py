from app.remediation.models import RemediationFindingRef
from app.remediation.compiler import RemediationCompiler


class ShadowRemediationIntegration:
    def process_drift_finding(self, finding: RemediationFindingRef):
        compiler = RemediationCompiler()
        pack = compiler.compile_pack(finding)
        return pack
