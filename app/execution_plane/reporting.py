import json


class ExecutionReporter:
    @staticmethod
    def format_venue_registry(registry) -> str:
        res = []
        for v in registry.list_venues():
            res.append(
                f"Venue: {v.venue_id} | Class: {v.venue_class.value} | Product: {v.product_class.value}"
            )
        return "\n".join(res)

    @staticmethod
    def format_venue_filters(registry) -> str:
        res = []
        for v in registry.list_venues():
            c = v.constraints
            res.append(
                f"Venue: {v.venue_id}\n  Min Qty: {c.min_qty} | Min Notional: {c.min_notional}\n  Tick: {c.tick_size} | Step: {c.step_size}\n  Reduce-Only: {c.reduce_only_allowed} | Fresh: {c.is_fresh}"
            )
        return "\n".join(res)

    @staticmethod
    def format_json(obj: dict) -> str:
        return json.dumps(obj, indent=2)
