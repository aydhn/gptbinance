import os

def append_to_gitignore(entries):
    gitignore_path = '.gitignore'
    content = ""
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            content = f.read()

    new_entries = []
    for entry in entries:
        if entry not in content:
            new_entries.append(entry)

    if new_entries:
        with open(gitignore_path, 'a') as f:
            f.write('\n' + '\n'.join(new_entries) + '\n')
        print(f"Added to .gitignore: {new_entries}")
    else:
        print("All entries already in .gitignore")

append_to_gitignore([
    '__pycache__/',
    '*.pyc',
    '.pytest_cache/',
    '*.tmp'
])
