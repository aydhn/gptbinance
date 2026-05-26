# preferences.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class PreferenceRiskRecord(BaseModel):
    preference_id: str
    transfer_ref: str
    risk_level: str # high, stale, disputed
    description: str
    lineage_refs: List[str]

class PreferenceRiskManager:
    def __init__(self):
        self.preferences: Dict[str, PreferenceRiskRecord] = {}

    def register_preference_risk(self, preference: PreferenceRiskRecord):
        self.preferences[preference.preference_id] = preference

    def get_preference_risk(self, preference_id: str) -> Optional[PreferenceRiskRecord]:
        return self.preferences.get(preference_id)

    def list_preference_risks(self) -> List[PreferenceRiskRecord]:
        return list(self.preferences.values())
