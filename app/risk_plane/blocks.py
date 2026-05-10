from typing import List, Dict
from pydantic import BaseModel
from .enums import RiskDomain


class BlockState(BaseModel):
    block_id: str
    domain: RiskDomain
    target_id: str
    block_type: str  # NO_NEW_EXPOSURE, FREEZE
    lineage_refs: List[str]
    expiry: str


class BlockManager:
    def __init__(self):
        self._blocks: Dict[str, BlockState] = {}

    def add_block(self, block: BlockState):
        self._blocks[block.block_id] = block

    def is_blocked(self, domain: RiskDomain, target_id: str) -> bool:
        for b in self._blocks.values():
            if b.domain == domain and b.target_id == target_id:
                return True
        return False


global_block_manager = BlockManager()


class RiskBlockEvaluator:
    def sticky_blocks_active(self, risk_event: str, preventive_actions_verified: bool) -> bool:
        return not preventive_actions_verified
