import random

# Track total flips across all simulations
total_flips = 0

# Perform 10 simulations
for _ in range(10):
    # Initialize for this simulation
    flips = 0
    consecutive = 1

    # First flip
    previous = random.choice(["H", "T"])
    print(previous, end=" ")
    flips = 1

    # Keep flipping until 3 consecutive same outcomes
    while consecutive < 3:
        # Generate new flip
        current = random.choice(["H", "T"])
        print(current, end=" ")
        flips += 1

        # Check if same as previous
        if current == previous:
            consecutive += 1
        else:
            consecutive = 1

        # Update previous
        previous = current

    # Display flip count for this simulation
    print(f"({flips} flips)")
    total_flips += flips

# Calculate and display average
average = total_flips / 10
print(f"On average, {average} flips were needed.")
