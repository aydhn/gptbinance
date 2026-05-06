from typing import Dict, Any, List


class IntakeNormalizer:
    def normalize(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        return raw_data


class IntakeManager:
    def __init__(self):
        self.normalizer = IntakeNormalizer()

    def process_intake(self, source: str, raw_data: Dict[str, Any]):
        normalized = self.normalizer.normalize(raw_data)
        return normalized

    def handle_duplicates(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # Duplicate removal logic
        return data
