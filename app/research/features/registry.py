from typing import Dict, Type, List, Optional
from app.research.features.base import BaseFeatureCalculator
from app.research.features.exceptions import UnsupportedFeatureError


class FeatureRegistry:
    """
    Central registry for all feature calculators.
    """

    _calculators: Dict[str, Type[BaseFeatureCalculator]] = {}

    @classmethod
    def register(
        cls, calculator_class: Type[BaseFeatureCalculator]
    ) -> Type[BaseFeatureCalculator]:
        """
        Decorator to register a feature calculator.
        """
        name = calculator_class.get_name()
        if name in cls._calculators:
            raise ValueError(
                f"Feature calculator with name '{name}' is already registered."
            )
        cls._calculators[name] = calculator_class
        return calculator_class

    @classmethod
    def get(cls, name: str) -> BaseFeatureCalculator:
        """
        Get an instance of a feature calculator by name.
        """
        if name not in cls._calculators:
            raise UnsupportedFeatureError(f"Feature '{name}' is not registered.")
        return cls._calculators[name]()

    @classmethod
    def get_all_names(cls) -> List[str]:
        """Return a list of all registered feature names."""
        return list(cls._calculators.keys())

    @classmethod
    def get_by_category(cls, category: str) -> List[str]:
        """Return names of features in a specific category."""
        return [
            name
            for name, calc_class in cls._calculators.items()
            if calc_class.get_category() == category
        ]

    @classmethod
    def clear(cls) -> None:
        """Clear the registry (mostly for testing)."""
        cls._calculators.clear()


# Global registry instance is technically the class itself due to @classmethod design.
