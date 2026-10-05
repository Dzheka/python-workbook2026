# Read two numbers
m = int(input())
n = int(input())

# Initialize d to the smaller of m and n
d = min(m, n)

# Loop until d divides both m and n
while m % d != 0 or n % d != 0:
    d -= 1

# Display result
print(f"The GCD is {d}")
