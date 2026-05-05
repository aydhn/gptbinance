# Stub for replay timeline refs
class ReplayTimeline:
    def __init__(self):
        self.events = []

    def add_event(self, event, truth_ref):
        self.events.append({"event": event, "truth_ref": truth_ref})
