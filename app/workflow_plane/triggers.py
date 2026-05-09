from app.workflow_plane.models import TriggerDefinition

class TriggerRegistry:
    def __init__(self):
        self._triggers = {}

    def register(self, trigger: TriggerDefinition):
        self._triggers[trigger.trigger_class] = trigger
