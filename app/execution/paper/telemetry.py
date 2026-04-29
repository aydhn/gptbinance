"""Telemetry counters for runtime events."""


class RuntimeTelemetry:
    def __init__(self):
        self.signals_generated = 0
        self.risk_vetoes = 0
        self.intents_approved = 0
        self.orders_created = 0
        self.fills_executed = 0

    def inc_signal(self):
        self.signals_generated += 1

    def inc_risk_veto(self):
        self.risk_vetoes += 1

    def inc_intent(self):
        self.intents_approved += 1

    def inc_order(self):
        self.orders_created += 1

    def inc_fill(self):
        self.fills_executed += 1
