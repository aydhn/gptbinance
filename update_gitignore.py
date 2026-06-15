import os

gitignore_path = ".gitignore"
content_to_append = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Pytest
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log
"""

if not os.path.exists(gitignore_path):
    with open(gitignore_path, 'w') as f:
        f.write(content_to_append)
else:
    with open(gitignore_path, 'r') as f:
        content = f.read()
    if "__pycache__/" not in content:
        with open(gitignore_path, 'a') as f:
            f.write(content_to_append)

print("Updated .gitignore")
