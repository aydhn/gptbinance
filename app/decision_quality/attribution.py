from typing import List, Dict
from .models import DecisionFrictionRecord
from .enums import FrictionClass


class FrictionAttributor:
    """
    Attributes friction records to broad system domains for analysis.
    """

    def aggregate_friction(
        self, frictions: List[DecisionFrictionRecord]
    ) -> Dict[str, int]:
        """
        Aggregates friction records by class to show top friction sources.
        """
        summary = {}
        for friction in frictions:
            class_name = friction.friction_class.value
            summary[class_name] = summary.get(class_name, 0) + 1
        return summary

    def determine_primary_block_domain(
        self, frictions: List[DecisionFrictionRecord]
    ) -> FrictionClass:
        """
        Determines the primary domain responsible for a block based on severity or order.
        """
        if not frictions:
            return FrictionClass.UNKNOWN_MIXED

        # Simplified logic: return highest severity, or first if equal
        sorted_frictions = sorted(frictions, key=lambda x: x.severity, reverse=True)
        return sorted_frictions[0].friction_class
