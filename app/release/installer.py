from app.release.models import InstallPlan, ReleaseManifest
from app.release.host_probe import HostProbe
from app.release.enums import InstallVerdict, HostReadiness


class Installer:
    def __init__(self):
        self.host_probe = HostProbe()

    def create_plan(self, target_release: ReleaseManifest) -> InstallPlan:
        probe = self.host_probe.run_probe()

        verdict = InstallVerdict.PASS
        warnings = []

        if probe.readiness == HostReadiness.UNREADY:
            verdict = InstallVerdict.FAIL
        elif probe.readiness == HostReadiness.CAUTION:
            verdict = InstallVerdict.CAUTION
            warnings = probe.warnings

        return InstallPlan(
            target_release=target_release,
            host_probe=probe,
            verdict=verdict,
            warnings=warnings,
        )
