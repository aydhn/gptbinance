import hashlib
import json
from typing import Any


def generate_hash(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def generate_file_hash(filepath: str) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()


def stable_serialize(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def hash_dict(data: dict) -> str:
    return generate_hash(stable_serialize(data))
