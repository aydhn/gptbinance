from app.main import main
import sys

sys.argv = ["app/main.py", "--show-command-registry"]
try:
    main()
except Exception as e:
    print(f"Error: {e}")
