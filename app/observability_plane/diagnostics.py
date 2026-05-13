from typing import Dict, List, Optional
from .models import DiagnosticSignal

class DiagnosticSignalBuilder:
    def __init__(self):
        self._signals: Dict[str, DiagnosticSignal] = {}

    def register_signal(self, signal: DiagnosticSignal) -> None:
        self._signals[signal.signal_id] = signal

    def get_signal(self, signal_id: str) -> Optional[DiagnosticSignal]:
        return self._signals.get(signal_id)

    def list_signals(self) -> List[DiagnosticSignal]:
        return list(self._signals.values())

class SecurityDetectionDiagnosticSignal(DiagnosticSignal):
    pass
