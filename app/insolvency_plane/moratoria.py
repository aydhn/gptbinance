# moratoria.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class MoratoriumRecord(BaseModel):
    moratorium_id: str
    moratorium_type: str # payment, enforcement, partial
    description: str
    is_breached: bool = False
    lineage_refs: List[str]

class MoratoriumManager:
    def __init__(self):
        self.moratoria: Dict[str, MoratoriumRecord] = {}

    def enter_moratorium(self, moratorium: MoratoriumRecord):
        self.moratoria[moratorium.moratorium_id] = moratorium

    def get_moratorium(self, moratorium_id: str) -> Optional[MoratoriumRecord]:
        return self.moratoria.get(moratorium_id)

    def list_moratoria(self) -> List[MoratoriumRecord]:
        return list(self.moratoria.values())
