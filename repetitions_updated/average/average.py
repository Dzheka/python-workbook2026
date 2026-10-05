# Initialize sum and count
total = 0
count = 0

# Read first value
value = float(input())

# Loop until 0 is entered
while value != 0:
    total += value
    count += 1
    value = float(input())

# Calculate and display average
average = total / count
print(f"The average is {average}")
