from app.postmortems.models import CorrectiveAction, PreventiveAction
from typing import List


class CAPARegistry:
    def __init__(self):
        self.corrective_actions: List[CorrectiveAction] = []
        self.preventive_actions: List[PreventiveAction] = []

    def register_corrective(self, action: CorrectiveAction):
        self.corrective_actions.append(action)

    def register_preventive(self, action: PreventiveAction):
        self.preventive_actions.append(action)

    def get_all(self):
        return {
            "corrective": self.corrective_actions,
            "preventive": self.preventive_actions,
        }
