import argparse
import sys
from .tradeoff_plane import tradeoff_registry, tradeoff_storage, tradeoff_reporter
from .tradeoff_plane.models import TradeoffObject

def handle_tradeoff_commands(args):
    if getattr(args, 'show_tradeoff_registry', False):
        print("Canonical Tradeoff Registry Families:")
        for family in tradeoff_registry._families:
            print(f"  - {family}")
        return True

    tradeoff_id = getattr(args, 'tradeoff_id', None)

    if getattr(args, 'show_tradeoff_object', False):
        if not tradeoff_id:
             print("Error: --tradeoff-id is required")
             return True
        obj = tradeoff_storage.get_object(tradeoff_id)
        if obj:
            print(tradeoff_reporter.generate_summary(obj))
        else:
            print(f"Tradeoff {tradeoff_id} not found")
        return True

    return False
