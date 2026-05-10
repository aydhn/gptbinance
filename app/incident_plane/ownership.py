from pydantic import BaseModel
from typing import Optional

class IncidentOwnerAssignment(BaseModel):
    primary: str
    secondary: Optional[str]
    escalation: Optional[str]
    notes: str

class IncidentOwnershipEngine:
    @staticmethod
    def assign_owner(primary: str, secondary: str = None, notes: str = "") -> IncidentOwnerAssignment:
        if not primary:
            raise ValueError("No ownerless critical incident allowed.")
        return IncidentOwnerAssignment(primary=primary, secondary=secondary, escalation=None, notes=notes)
