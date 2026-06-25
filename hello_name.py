
import sys

if len(sys.argv) < 2:
    print("Error: Missing Name.")
    sys.exit(1) 

name = sys.argv[1]
print(f"Hello, {name}")
