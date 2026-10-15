import sys

nums = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    nums.append(int(line))
print(f"Minimum: {min(nums)}")
print(f"Maximum: {max(nums)}")
