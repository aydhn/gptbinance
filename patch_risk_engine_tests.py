import re

with open('app/risk/engine.py', 'r') as f:
    content = f.read()

# Let's see what app/risk/engine.py looks like
print(content[:1000])
