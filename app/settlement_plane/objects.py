from pydantic import BaseModel
class SettlementObject(BaseModel):
    id: str
    type: str
    owner_metadata: dict
    lifecycle_state: str
