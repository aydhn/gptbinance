import os

def remove_unused(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if file_path == "app/performance_plane/base.py" and "from typing import Optional" in line:
            continue
        if file_path == "app/performance_plane/baselines.py" and "from app.performance_plane.enums import BenchmarkClass" in line:
            continue
        if file_path == "app/performance_plane/baselines.py" and "from typing import List" in line:
            continue
        if file_path == "app/performance_plane/equivalence.py" and "from typing import List" in line:
            continue
        if file_path == "app/performance_plane/risk_adjusted.py" and "from typing import List" in line:
            continue
        if file_path == "app/performance_plane/windows.py" and "from datetime import timezone" in line:
            continue
        if file_path == "app/performance_plane/windows.py" and "from typing import List" in line:
            continue

        new_lines.append(line)

    with open(file_path, "w") as f:
        f.writelines(new_lines)

files_to_fix = [
    "app/performance_plane/base.py",
    "app/performance_plane/baselines.py",
    "app/performance_plane/equivalence.py",
    "app/performance_plane/risk_adjusted.py",
    "app/performance_plane/windows.py"
]

for file in files_to_fix:
    remove_unused(file)
