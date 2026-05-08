from typing import Optional
from app.performance_plane.storage import global_performance_storage
from app.performance_plane.models import PerformanceManifest, ReturnSurface


class PerformanceRepository:
    @staticmethod
    def save_manifest(manifest: PerformanceManifest) -> None:
        global_performance_storage.save_manifest(manifest.manifest_id, manifest.dict())

    @staticmethod
    def get_manifest(manifest_id: str) -> Optional[PerformanceManifest]:
        data = global_performance_storage.get_manifest(manifest_id)
        if data:
            return PerformanceManifest(**data)
        return None

    @staticmethod
    def save_return_surface(surface: ReturnSurface) -> None:
        global_performance_storage.save_return(surface.surface_id, surface.dict())

    @staticmethod
    def get_return_surface(surface_id: str) -> Optional[ReturnSurface]:
        data = global_performance_storage.get_return(surface_id)
        if data:
            return ReturnSurface(**data)
        return None
