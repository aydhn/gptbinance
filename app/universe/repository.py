from typing import List, Optional
from app.universe.models import ProductInstrument, UniverseSnapshot, LifecycleEvent
from app.universe.storage import UniverseStorage
from app.universe.registry import InstrumentRegistry
from app.universe.enums import InstrumentType


class UniverseRepository:
    def __init__(self, storage: UniverseStorage):
        self.storage = storage
        self.registry = InstrumentRegistry()
        self._load_registry()

    def _load_registry(self):
        insts = self.storage.load_registry_snapshot()
        for inst in insts:
            self.registry.upsert_instrument(inst)

    def save_registry(self):
        self.storage.save_registry_snapshot(self.registry.get_all_instruments())

    def get_instrument(
        self, symbol: str, product_type: InstrumentType
    ) -> Optional[ProductInstrument]:
        return self.registry.get_instrument(symbol, product_type)

    def get_active_instruments(self) -> List[ProductInstrument]:
        return self.registry.get_all_active()

    def get_all_instruments(self) -> List[ProductInstrument]:
        return self.registry.get_all_instruments()

    # Placeholder for other repos (snapshots, diffs, lifecycle)
