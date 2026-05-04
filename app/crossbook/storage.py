"""
storage.py
"""
from typing import Any


class CrossBookStorage:
    def __init__(self):
        self.snapshots = {}
        self.graphs = {}
        self.decisions = {}

    def save_snapshot(self, sid: str, data: Any):
        self.snapshots[sid] = data

    def save_graph(self, gid: str, data: Any):
        self.graphs[gid] = data

    def save_decision(self, did: str, data: Any):
        self.decisions[did] = data
