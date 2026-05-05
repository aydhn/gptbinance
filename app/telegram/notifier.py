import json

class TelegramActivationNotifier:
    @staticmethod
    def notify_intent_created(intent_id: str):
        print(f"[TELEGRAM] Activation intent created: {intent_id}")

    @staticmethod
    def notify_probation_started(intent_id: str):
        print(f"[TELEGRAM] Activation probation started: {intent_id}")

    @staticmethod
    def notify_hold_required(intent_id: str):
        print(f"[TELEGRAM] Activation hold required: {intent_id}")

    @staticmethod
    def notify_halt_recommended(intent_id: str):
        print(f"[TELEGRAM] Activation halt recommended: {intent_id}")

    @staticmethod
    def notify_reverted(intent_id: str):
        print(f"[TELEGRAM] Activation reverted: {intent_id}")
