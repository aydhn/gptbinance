import logging
from typing import Dict, List, Optional
from datetime import datetime, timezone
from app.universe.models import ProductInstrument, InstrumentRef
from app.universe.enums import InstrumentType, InstrumentStatus

logger = logging.getLogger(__name__)

class InstrumentRegistry:
    def __init__(self):
        # Format: {canonical_symbol: {product_type: ProductInstrument}}
        self._instruments: Dict[str, Dict[InstrumentType, ProductInstrument]] = {}
        self._last_update: Optional[datetime] = None

    def upsert_instrument(self, instrument: ProductInstrument):
        canonical = instrument.ref.canonical_symbol
        p_type = instrument.ref.product_type

        if canonical not in self._instruments:
            self._instruments[canonical] = {}

        self._instruments[canonical][p_type] = instrument
        self._last_update = datetime.now(timezone.utc)

    def get_instrument(self, symbol: str, product_type: InstrumentType) -> Optional[ProductInstrument]:
        canonical = symbol.upper().replace("-", "").replace("/", "")
        return self._instruments.get(canonical, {}).get(product_type)

    def get_all_active(self) -> List[ProductInstrument]:
        active = []
        for p_map in self._instruments.values():
            for inst in p_map.values():
                if inst.status == InstrumentStatus.TRADING:
                    active.append(inst)
        return active

    def get_all_instruments(self) -> List[ProductInstrument]:
        all_inst = []
        for p_map in self._instruments.values():
            for inst in p_map.values():
                all_inst.append(inst)
        return all_inst

    def get_last_update_time(self) -> Optional[datetime]:
        return self._last_update
