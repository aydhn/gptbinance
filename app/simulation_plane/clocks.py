class SimulationClock:
    def __init__(self):
        self.caveats = [
            "Time-consistency checks enforced. Event clock must strictly precede fill clock."
        ]
