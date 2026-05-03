import re

with open("tests/test_replay_timeline.py", "r") as f:
    content = f.read()

# Remove trailing commas inside imports to avoid syntax errors
content = re.sub(r',\s*\)', ')', content)
content = re.sub(r',\s*,', ',', content)
content = re.sub(r'from app.replay.enums import \n', '', content)

with open("tests/test_replay_timeline.py", "w") as f:
    f.write(content)

with open("tests/test_replay_snapshots.py", "r") as f:
    content = f.read()

content = re.sub(r',\s*\)', ')', content)
content = re.sub(r',\s*,', ',', content)

with open("tests/test_replay_snapshots.py", "w") as f:
    f.write(content)
