import tempfile
from pathlib import Path
from typing import Dict, Any
from app.config.models import AppConfig
from app.storage.paths import (
    get_data_dir,
    get_market_data_dir,
    get_metadata_dir,
    get_market_data_index_path,
)
from app.storage.local_store import LocalMarketDataStore


def _test_storage_writable(dir_path: Path) -> bool:
    try:
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
        test_file = dir_path / ".healthcheck_write_test"
        test_file.touch()
        test_file.unlink()
        return True
    except Exception:
        return False


def run_healthcheck(config: AppConfig) -> Dict[str, Any]:
    health_status = {"status": "ok", "storage": {}}

    try:
        data_dir = get_data_dir(config)
        market_data_dir = get_market_data_dir(config)
        metadata_dir = get_metadata_dir(config)
        index_path = get_market_data_index_path(config)

        storage_writable = _test_storage_writable(data_dir)

        health_status["storage"] = {
            "data_dir": str(data_dir),
            "market_data_dir": str(market_data_dir),
            "metadata_dir": str(metadata_dir),
            "storage_format": config.storage.storage_format,
            "prefer_local_data": config.storage.prefer_local_data,
            "save_fetched_data": config.storage.save_fetched_data,
            "market_data_index_exists": index_path.exists(),
            "local_store_writable": storage_writable,
        }

        if not storage_writable:
            health_status["status"] = "warning"
            health_status["message"] = "Storage directory is not writable."

    except Exception as e:
        health_status["status"] = "error"
        health_status["message"] = str(e)

    return health_status
