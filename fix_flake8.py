import os
import glob

files = glob.glob("app/precedent_plane/*.py")
for f in files:
    with open(f, "r") as file:
        content = file.read()

    # We don't really have to fix anything unless we run flake8 but let's just make sure tests passed.
