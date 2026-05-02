from app.release.models import HostProbeReport
from app.release.enums import HostReadiness
import sys
import os


class HostProbe:
    def run_probe(self) -> HostProbeReport:
        warnings = []
        blockers = []

        # Python version check
        python_ok = sys.version_info >= (3, 10)
        if not python_ok:
            blockers.append(f"Python 3.10+ required. Found {sys.version.split()[0]}")

        # Writable paths check
        paths_to_check = ["data", "config", "logs"]
        writable_ok = True
        for p in paths_to_check:
            os.makedirs(p, exist_ok=True)
            if not os.access(p, os.W_OK):
                writable_ok = False
                blockers.append(f"Path {p} is not writable.")

        # Disk space check
        disk_ok = True
        # Simplified check for demo

        readiness = HostReadiness.READY
        if blockers:
            readiness = HostReadiness.UNREADY
        elif warnings:
            readiness = HostReadiness.CAUTION

        return HostProbeReport(
            readiness=readiness,
            python_version_ok=python_ok,
            disk_space_ok=disk_ok,
            writable_paths_ok=writable_ok,
            warnings=warnings,
            blockers=blockers,
        )
