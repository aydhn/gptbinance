import subprocess
import os
from datetime import datetime, timezone
from app.supply_chain.models import SourceSnapshot
from app.supply_chain.enums import SourceClass
from app.supply_chain.hashes import generate_hash, stable_serialize


class GitSourceSnapshotter:
    def create_snapshot(self, path: str = ".") -> SourceSnapshot:
        try:
            commit_hash = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=path, text=True
            ).strip()
            status = subprocess.check_output(
                ["git", "status", "--porcelain"], cwd=path, text=True
            ).strip()
            is_clean = len(status) == 0

            tracked_files_output = subprocess.check_output(
                ["git", "ls-tree", "-r", "HEAD", "--name-only"], cwd=path, text=True
            ).strip()
            tracked_files = (
                tracked_files_output.split("\n") if tracked_files_output else []
            )

            snapshot_data = {
                "ref": commit_hash,
                "is_clean": is_clean,
                "tracked_files": tracked_files,
            }

            return SourceSnapshot(
                id=f"src_{generate_hash(commit_hash)[:8]}",
                source_class=SourceClass.GIT_COMMIT,
                ref=commit_hash,
                timestamp=datetime.now(timezone.utc),
                is_clean=is_clean,
                tracked_files=tracked_files,
                hash=generate_hash(stable_serialize(snapshot_data)),
            )
        except subprocess.CalledProcessError:
            # Fallback for detached/non-git
            return SourceSnapshot(
                id=f"src_detached_{int(datetime.now(timezone.utc).timestamp())}",
                source_class=SourceClass.DETACHED_SNAPSHOT,
                ref="unknown",
                timestamp=datetime.now(timezone.utc),
                is_clean=False,
                tracked_files=[],
                hash=generate_hash("detached"),
            )
