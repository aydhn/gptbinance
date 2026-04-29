import os

files_to_fix = [
    "app/optimizer/storage.py",
    "tests/test_walkforward_windowing.py"
]

for filepath in files_to_fix:
    with open(filepath, "r") as f:
        content = f.read()

    # Fix trailing whitespace in storage.py
    if "storage.py" in filepath:
        content = content.replace(" \n", "\n")

    # Fix boolean comparison in tests
    if "test_walkforward_windowing.py" in filepath:
        content = content.replace("== True", "is True")

    with open(filepath, "w") as f:
        f.write(content)
