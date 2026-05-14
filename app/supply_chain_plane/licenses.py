from typing import Dict, Optional, List
from app.supply_chain_plane.models import LicenseRecord


class LicenseRegistry:
    def __init__(self):
        self._licenses: Dict[str, LicenseRecord] = {}

    def register_license(self, license_record: LicenseRecord) -> None:
        self._licenses[license_record.license_id] = license_record

    def get_license(self, license_id: str) -> Optional[LicenseRecord]:
        return self._licenses.get(license_id)

    def get_licenses_for_component(self, component_id: str) -> List[LicenseRecord]:
        return [
            l
            for l in self._licenses.values()
            if l.component_ref.component_id == component_id
        ]
