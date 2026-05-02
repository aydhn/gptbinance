from typing import List
from app.security.models import SecretInventoryEntry, SecretRef
from app.security.enums import SecretStatus


class SecretInventory:
    def get_inventory(self) -> List[SecretInventoryEntry]:
        return [
            SecretInventoryEntry(
                ref=SecretRef(key="BINANCE_API_KEY", description="Binance API Key"),
                status=SecretStatus.SAFE,
                used_by=["app.exchange.client"],
                blast_radius="High",
            )
        ]
