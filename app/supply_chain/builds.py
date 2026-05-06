from typing import List
from app.supply_chain.models import (
    BuildInputManifest,
    BuildArtifactRecord,
    BuildOutputManifest,
)
from app.supply_chain.manifests import ManifestBuilder
from app.supply_chain.environments import EnvironmentSnapshotter
from app.supply_chain.enums import ArtifactClass


class BuildProvenanceAssembler:
    def assemble(
        self,
        src_id: str,
        dep_id: str,
        artifacts: List[BuildArtifactRecord],
        art_class: ArtifactClass,
    ) -> BuildOutputManifest:
        env_snap = EnvironmentSnapshotter().create_snapshot()
        inputs = BuildInputManifest(
            source_snapshot_id=src_id,
            dependency_snapshot_id=dep_id,
            environment_snapshot=env_snap,
        )
        return ManifestBuilder().build(inputs, artifacts, art_class)
