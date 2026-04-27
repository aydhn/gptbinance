
from app.research.regime.registry import regime_registry
from app.research.regime.trend_regime import TrendPersistenceEvaluator
from app.research.regime.volatility_regime import VolatilityExpansionEvaluator
from app.research.regime.mean_reversion_regime import MeanReversionProneEvaluator
from app.research.regime.structure_regime import StructureBreakoutEvaluator

# Register default evaluators
regime_registry.register("trend_persistence", TrendPersistenceEvaluator())
regime_registry.register("volatility_expansion", VolatilityExpansionEvaluator())
regime_registry.register("mean_reversion_prone", MeanReversionProneEvaluator())
regime_registry.register("structure_breakout", StructureBreakoutEvaluator())
