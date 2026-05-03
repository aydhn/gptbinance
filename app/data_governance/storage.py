import json
import os
from typing import Dict, Any, List
from pathlib import Path

class GovernanceStorage:
    def __init__(self, base_path: str = "data/governance"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _write_json(self, subpath: str, filename: str, data: Dict[str, Any]):
        dir_path = self.base_path / subpath
        dir_path.mkdir(parents=True, exist_ok=True)
        with open(dir_path / filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def _read_json(self, subpath: str, filename: str) -> Dict[str, Any]:
        file_path = self.base_path / subpath / filename
        if not file_path.exists():
            return None
        with open(file_path, 'r') as f:
            return json.load(f)

    def _list_json(self, subpath: str) -> List[Dict[str, Any]]:
        dir_path = self.base_path / subpath
        if not dir_path.exists():
            return []
        items = []
        for file in dir_path.glob("*.json"):
            with open(file, 'r') as f:
                 items.append(json.load(f))
        return items

    def save_contract(self, contract_id: str, data: Dict[str, Any]):
        self._write_json("contracts", f"{contract_id}.json", data)

    def get_contract(self, contract_id: str) -> Dict[str, Any]:
        return self._read_json("contracts", f"{contract_id}.json")

    def list_contracts(self) -> List[Dict[str, Any]]:
        return self._list_json("contracts")

    def save_schema(self, schema_id: str, version: str, data: Dict[str, Any]):
        self._write_json(f"schemas/{schema_id}", f"{version}.json", data)

    def get_schema(self, schema_id: str, version: str) -> Dict[str, Any]:
        return self._read_json(f"schemas/{schema_id}", f"{version}.json")

    def save_quality_report(self, run_id: str, data: Dict[str, Any]):
         self._write_json("quality", f"{run_id}.json", data)

    def save_trust_verdict(self, dataset_id: str, version: str, data: Dict[str, Any]):
         self._write_json(f"trust/{dataset_id}", f"{version}.json", data)

    def get_trust_verdict(self, dataset_id: str, version: str) -> Dict[str, Any]:
         return self._read_json(f"trust/{dataset_id}", f"{version}.json")
