import os
import re

def fix_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            if file_path.endswith("tests/test_risk_policies.py") and "from app.risk.enums import ExposureScope, ExposureScope" in line:
                line = line.replace("ExposureScope, ExposureScope", "ExposureScope")
            f.write(line)

for root, _, files in os.walk("tests"):
    for file in files:
        if file.endswith(".py"):
            fix_file(os.path.join(root, file))
