import os
import glob

# For all facade modules in app/precedent_plane, we need some basic functionality.
facades = glob.glob("app/precedent_plane/*.py")
for f in facades:
    if os.path.basename(f) in ["__init__.py", "models.py", "enums.py", "exceptions.py", "base.py", "registry.py"]:
        continue

    with open(f, "r") as file:
        content = file.read()

    # We will replace 'pass' in process method with some basic returns
    if "def process(self, *args, **kwargs):" in content:
        content = content.replace("        pass", "        return True")
        with open(f, "w") as file:
            file.write(content)
