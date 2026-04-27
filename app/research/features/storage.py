import os
import json
import pandas as pd
from typing import Optional
from app.core.paths import PATHS
from app.research.features.models import FeatureSet, FeatureGenerationReport


class FeatureStorage:
    """
    Handles saving and loading feature sets and their metadata (lineage, manifest).
    """

    def __init__(self, base_dir: Optional[str] = None):
        self.base_dir = base_dir or os.path.join(PATHS.processed_data, "features")
        os.makedirs(self.base_dir, exist_ok=True)

    def _get_set_dir(self, feature_set_name: str) -> str:
        d = os.path.join(self.base_dir, feature_set_name)
        os.makedirs(d, exist_ok=True)
        return d

    def save(self, df: pd.DataFrame, feature_set: FeatureSet) -> str:
        """
        Saves the dataframe as parquet and the metadata as JSON.
        Returns the path to the directory.
        """
        set_dir = self._get_set_dir(feature_set.name)

        # Save dataframe
        df_path = os.path.join(
            set_dir,
            f"{feature_set.report.lineage.symbol}_{feature_set.report.lineage.interval}.parquet",
        )
        df.to_parquet(df_path)

        feature_set.storage_path = df_path

        # Save metadata (manifest)
        manifest_path = os.path.join(
            set_dir,
            f"{feature_set.report.lineage.symbol}_{feature_set.report.lineage.interval}_manifest.json",
        )
        with open(manifest_path, "w") as f:
            f.write(feature_set.model_dump_json(indent=2))

        return set_dir

    def load_metadata(
        self, feature_set_name: str, symbol: str, interval: str
    ) -> FeatureSet:
        set_dir = self._get_set_dir(feature_set_name)
        manifest_path = os.path.join(set_dir, f"{symbol}_{interval}_manifest.json")

        if not os.path.exists(manifest_path):
            raise FileNotFoundError(f"Manifest not found at {manifest_path}")

        with open(manifest_path, "r") as f:
            data = json.load(f)

        return FeatureSet(**data)

    def load_data(self, feature_set: FeatureSet) -> pd.DataFrame:
        if not feature_set.storage_path or not os.path.exists(feature_set.storage_path):
            raise FileNotFoundError(
                f"Data file not found at {feature_set.storage_path}"
            )

        return pd.read_parquet(feature_set.storage_path)
