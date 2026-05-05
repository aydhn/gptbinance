import subprocess
import sys

def run():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pydantic"])
    print("pydantic installed")

if __name__ == "__main__":
    run()
