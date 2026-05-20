from app.temporal_plane.models import TemporalObjectRef, TemporalArtifactManifest, TemporalTrustVerdict
from app.temporal_plane.enums import TrustVerdict
from typing import List

class TemporalManifestBuilder:
    def __init__(self):
        pass

    def build_manifest(self, t_objs: List[TemporalObjectRef]) -> TemporalArtifactManifest:
        return TemporalArtifactManifest(
            manifest_id="TM-001",
            temporal_objects=t_objs,
            verdict=TemporalTrustVerdict(verdict=TrustVerdict.TRUSTED, reasons=["Manifest built"])
        )

class ManifestsManager:
    def __init__(self):
        self.builder = TemporalManifestBuilder()

    def evaluate(self, ref: TemporalObjectRef) -> dict:
        return {"status": "ok"}
