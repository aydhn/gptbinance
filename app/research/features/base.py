from abc import ABC, abstractmethod
import pandas as pd
from typing import Dict, Any, List

from app.research.features.models import FeatureSpec
from app.research.features.exceptions import (
    InvalidFeatureSpecError,
    InsufficientHistoryError,
)


class BaseFeatureCalculator(ABC):
    """
    Abstract base class for all feature calculators.
    Enforces standard input/output contracts.
    """

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """Return the unique name of the feature."""
        pass

    @classmethod
    @abstractmethod
    def get_category(cls) -> str:
        """Return the category of the feature."""
        pass

    @classmethod
    @abstractmethod
    def get_min_history_required(cls, spec: FeatureSpec) -> int:
        """Return the minimum number of rows required to calculate this feature."""
        pass

    def validate_spec(self, spec: FeatureSpec) -> None:
        """
        Validate the parameters in the spec.
        Override this in subclasses for specific validations.
        """
        if spec.name != self.get_name():
            raise InvalidFeatureSpecError(
                f"Spec name '{spec.name}' does not match calculator name '{self.get_name()}'"
            )

    @abstractmethod
    def calculate(
        self, df: pd.DataFrame, spec: FeatureSpec
    ) -> pd.Series | pd.DataFrame:
        """
        Calculate the feature(s).
        Returns a Series (for single column features) or DataFrame (for multi-column features).
        The index of the returned Series/DataFrame MUST match the input DataFrame exactly.
        """
        pass

    def __call__(self, df: pd.DataFrame, spec: FeatureSpec) -> pd.Series | pd.DataFrame:
        """
        Main entry point for calculation, wraps standard validation and logic.
        """
        self.validate_spec(spec)
        min_history = self.get_min_history_required(spec)

        if len(df) < min_history:
            raise InsufficientHistoryError(
                f"Feature {self.get_name()} requires at least {min_history} rows, got {len(df)}"
            )

        result = self.calculate(df, spec)

        # Ensure index matching
        if isinstance(result, pd.Series):
            if not result.index.equals(df.index):
                raise ValueError(
                    f"Output index for {self.get_name()} does not match input dataframe index."
                )
        elif isinstance(result, pd.DataFrame):
            if not result.index.equals(df.index):
                raise ValueError(
                    f"Output index for {self.get_name()} does not match input dataframe index."
                )
        else:
            raise TypeError(
                f"Feature {self.get_name()} must return a pd.Series or pd.DataFrame."
            )

        return result
