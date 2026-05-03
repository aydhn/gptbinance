import re

def fix_init():
    with open("app/replay/__init__.py", "w") as f:
         f.write("from .engine import DefaultReplayEngine\nfrom .repository import replay_repository\n\n__all__ = ['DefaultReplayEngine', 'replay_repository']\n")

def fix_base():
    with open("app/replay/base.py", "r") as f:
         c = f.read()
    c = re.sub(r'ReplaySourceRef,?\s*', '', c)
    c = re.sub(r'CounterfactualResult,?\s*', '', c)
    c = re.sub(r'ReplayabilityScore,?\s*', '', c)
    with open("app/replay/base.py", "w") as f:
         f.write(c)

def fix_path():
    with open("app/replay/decision_path.py", "r") as f:
         c = f.read()
    c = re.sub(r'Dict,\s*', '', c)
    c = re.sub(r'Any,?\s*', '', c)
    with open("app/replay/decision_path.py", "w") as f:
         f.write(c)

def fix_engine():
    with open("app/replay/engine.py", "r") as f:
         c = f.read()
    c = re.sub(r'datetime,\s*', '', c)
    c = re.sub(r'timezone,?\s*', '', c)
    c = re.sub(r'from typing import Optional\n', '', c)
    with open("app/replay/engine.py", "w") as f:
         f.write(c)

def fix_sources():
    with open("app/replay/sources.py", "r") as f:
         c = f.read()
    c = re.sub(r'ReplaySourceRef,?\s*', '', c)
    with open("app/replay/sources.py", "w") as f:
         f.write(c)

def fix_storage():
    with open("app/replay/storage.py", "r") as f:
         c = f.read()
    c = re.sub(r'Any,?\s*', '', c)
    with open("app/replay/storage.py", "w") as f:
         f.write(c)

def fix_tests():
    with open("tests/test_replay_snapshots.py", "r") as f:
         c = f.read()
    c = re.sub(r'ReplaySourceRef,?\s*', '', c)
    c = re.sub(r'ReplaySourceType,?\s*', '', c)
    with open("tests/test_replay_snapshots.py", "w") as f:
         f.write(c)

fix_init()
fix_base()
fix_path()
fix_engine()
fix_sources()
fix_storage()
fix_tests()
