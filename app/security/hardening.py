import os
from app.security.models import SecurityCheckReport, SecurityCheck
from app.security.enums import SecurityVerdict

class SecurityHardening:
    def run_checks(self) -> SecurityCheckReport:
        checks = []
        # Check permissions of .env
        env_path = ".env"
        if os.path.exists(env_path):
            mode = os.stat(env_path).st_mode
            if mode & 0o077:  # Writable/readable by group/others
                checks.append(SecurityCheck(name="env_permissions", verdict=SecurityVerdict.FAIL, message=".env is too permissive"))
            else:
                checks.append(SecurityCheck(name="env_permissions", verdict=SecurityVerdict.PASS, message=".env permissions safe"))
        else:
            checks.append(SecurityCheck(name="env_permissions", verdict=SecurityVerdict.WARN, message=".env missing"))

        return SecurityCheckReport(checks=checks, overall_verdict=SecurityVerdict.WARN if any(c.verdict == SecurityVerdict.WARN for c in checks) else SecurityVerdict.PASS)
