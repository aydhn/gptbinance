from datetime import datetime, timezone
import json
import subprocess
from app.supply_chain.models import DependencySnapshot, DependencyItem
from app.supply_chain.enums import DependencyClass
from app.supply_chain.hashes import generate_hash, stable_serialize


class PoetryDependencyInventory:
    def create_snapshot(self, path: str = ".") -> DependencySnapshot:
        try:
            # Attempt to parse poetry.lock or use pip freeze as fallback
            # For this simple implementation, we'll try pip freeze to get a snapshot
            output = subprocess.check_output(["pip", "freeze"], text=True).strip()
            deps = []
            for line in output.split("\n"):
                if "==" in line:
                    name, version = line.split("==", 1)
                    deps.append(
                        DependencyItem(
                            name=name,
                            version=version,
                            dependency_class=DependencyClass.DIRECT,
                        )
                    )

            # Simple lock hash
            lock_hash = generate_hash(output)

            snap_data = stable_serialize([d.model_dump() for d in deps])

            return DependencySnapshot(
                id=f"dep_{generate_hash(snap_data)[:8]}",
                timestamp=datetime.now(timezone.utc),
                dependencies=deps,
                lock_hash=lock_hash,
                hash=generate_hash(snap_data),
            )
        except Exception:
            return DependencySnapshot(
                id=f"dep_unknown_{int(datetime.now(timezone.utc).timestamp())}",
                timestamp=datetime.now(timezone.utc),
                dependencies=[],
                lock_hash="unknown",
                hash="unknown",
            )
