from typing import Dict, Optional
from app.supply_chain_plane.models import PackageRecord


class PackageRegistry:
    def __init__(self):
        self._packages: Dict[str, PackageRecord] = {}

    def register_package(self, package: PackageRecord) -> None:
        self._packages[package.package_id] = package

    def get_package(self, package_id: str) -> Optional[PackageRecord]:
        return self._packages.get(package_id)
