from typing import Dict, Any
from app.settlement_plane.instructions import InstructionEvaluator
from app.settlement_plane.ssi import SSIEvaluator
from app.settlement_plane.matching import MatchingEvaluator
from app.settlement_plane.finality import FinalityEvaluator

class SettlementReadinessAggregator:
    def __init__(self):
        self.inst_eval = InstructionEvaluator()
        self.ssi_eval = SSIEvaluator()
        self.match_eval = MatchingEvaluator()
        self.fin_eval = FinalityEvaluator()

    def evaluate_readiness(self, context: Dict[str, Any]) -> Dict[str, Any]:
        inst_res = self.inst_eval.evaluate(context)
        ssi_res = self.ssi_eval.evaluate(context)
        match_res = self.match_eval.evaluate(context)
        fin_res = self.fin_eval.evaluate(context)

        return {
            "instruction_readiness": inst_res.instruction_class.name,
            "ssi_readiness": ssi_res.status,
            "matching_readiness": match_res.match_class.name,
            "finality_readiness": fin_res.finality_class.name,
            "overall_ready": (
                inst_res.instruction_class.name == "VALID_INSTRUCTION" and
                ssi_res.status == "valid" and
                match_res.match_class.name == "CLEAN_MATCH"
            )
        }
