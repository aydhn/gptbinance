from typing import Dict, Any, List
from .models import TradeoffObject

class TradeoffReporter:
    def generate_summary(self, tradeoff_obj: TradeoffObject) -> str:
        lines = []
        lines.append(f"Tradeoff Object: {tradeoff_obj.tradeoff_id} (Class: {tradeoff_obj.tradeoff_class.value})")
        lines.append(f"Owner: {tradeoff_obj.owner} | Scope: {tradeoff_obj.scope}")

        lines.append("\nObjectives:")
        if tradeoff_obj.objective_set and tradeoff_obj.objective_set.objectives:
            for obj in tradeoff_obj.objective_set.objectives:
                lines.append(f"  - [{obj.objective_class.value}] {obj.name}: {obj.description}")
        else:
            lines.append("  - No objectives declared")

        lines.append("\nBurden Posture:")
        if tradeoff_obj.burden_posture:
            for burden in tradeoff_obj.burden_posture:
                hidden_mark = "[HIDDEN] " if burden.is_hidden else ""
                lines.append(f"  - {hidden_mark}[{burden.burden_class.value}] {burden.description}")
        else:
            lines.append("  - No burdens declared")

        lines.append("\nSacrifices:")
        if tradeoff_obj.sacrifices:
             for sacrifice in tradeoff_obj.sacrifices:
                 lines.append(f"  - [{sacrifice.sacrifice_class.value}] {sacrifice.description}")
        else:
            lines.append("  - No explicit sacrifices declared")

        return "\n".join(lines)

tradeoff_reporter = TradeoffReporter()
