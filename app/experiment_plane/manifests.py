# Manifests
from app.experiment_plane.models import ExperimentArtifactManifest


def generate_manifest(experiment_id: str) -> ExperimentArtifactManifest:
    return ExperimentArtifactManifest(
        manifest_id=f"man_{experiment_id}",
        experiment_id=experiment_id,
        hashes={},
        lineage_refs={},
    )
