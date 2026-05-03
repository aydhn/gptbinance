import abc
from typing import List, Dict, Optional
from datetime import datetime
from app.universe.models import ProductInstrument, UniverseProfileConfig, UniverseEligibilityResult, InstrumentRef, LiquiditySnapshot, SpreadSnapshot, TradabilityReport
from app.universe.enums import InstrumentType
from app.workspaces.enums import ProfileType

class InstrumentSourceAdapter(abc.ABC):
    @abc.abstractmethod
    def fetch_instruments(self) -> List[Dict]:
        pass

    @abc.abstractmethod
    def get_source_freshness(self) -> datetime:
        pass

class MetadataNormalizer(abc.ABC):
    @abc.abstractmethod
    def normalize(self, raw_data: Dict) -> ProductInstrument:
        pass

    @abc.abstractmethod
    def get_canonical_symbol(self, symbol: str, product_type: InstrumentType) -> str:
        pass

class EligibilityEvaluator(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, instrument: ProductInstrument, profile_config: UniverseProfileConfig, profile: ProfileType) -> UniverseEligibilityResult:
        pass

class LiquidityScorer(abc.ABC):
    @abc.abstractmethod
    def score_liquidity(self, ref: InstrumentRef, market_data: Dict) -> LiquiditySnapshot:
        pass

    @abc.abstractmethod
    def score_spread(self, ref: InstrumentRef, market_data: Dict) -> SpreadSnapshot:
        pass
