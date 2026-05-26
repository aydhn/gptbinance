import sys

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        print(f"Executing {cmd} in Recovery Plane")

if __name__ == "__main__":
    main()
