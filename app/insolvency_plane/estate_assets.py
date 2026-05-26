# estate_assets.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import EstateAssetRecord

class EstateAssetManager:
    def __init__(self):
        self.assets: Dict[str, EstateAssetRecord] = {}

    def add_asset(self, asset: EstateAssetRecord):
        self.assets[asset.asset_id] = asset

    def get_asset(self, asset_id: str) -> Optional[EstateAssetRecord]:
        return self.assets.get(asset_id)

    def list_assets(self) -> List[EstateAssetRecord]:
        return list(self.assets.values())
