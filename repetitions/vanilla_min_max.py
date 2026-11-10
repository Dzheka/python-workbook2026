import sys

inputs = sys.stdin.read().split()
if inputs:
    try:
        numbers = [int(x) for x in inputs]
        print(f"Minimum: {min(numbers)}")
        print(f"Maximum: {max(numbers)}")
    except Exception:
        pass
