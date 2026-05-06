import sys
import platform
import os
from app.supply_chain.models import BuildEnvironmentSnapshot
from app.supply_chain.hashes import generate_hash, stable_serialize


class EnvironmentSnapshotter:
    def create_snapshot(self) -> BuildEnvironmentSnapshot:
        # Capture minimal safe env vars
        safe_envs = {k: v for k, v in os.environ.items() if k in ["PATH", "LANG", "TZ"]}

        return BuildEnvironmentSnapshot(
            python_version=sys.version.split()[0],
            os_platform=platform.platform(),
            tool_versions={"poetry": "unknown"},  # simplified
            env_vars_hash=generate_hash(stable_serialize(safe_envs)),
            is_deterministic=True,  # Assumption for minimal snapshot
        )
