import pytest
import sys

def main():
    try:
        pytest.main(["tests/"])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
