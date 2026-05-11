from typing import List, Dict, Any


class ComplianceQualityChecker:
    def check_missing_mappings(
        self, req_ids: List[str], mapped_req_ids: List[str]
    ) -> List[str]:
        return list(set(req_ids) - set(mapped_req_ids))
