import sys
from app.resolution_plane.cli import main as resolution_cli_main

def main():
    if len(sys.argv) > 1 and sys.argv[1].startswith("--show-"):
        resolution_cli_main()
    else:
        print("Usage: python -m app.main [options]")
        print("Use --help for available options.")

if __name__ == "__main__":
    main()
