# Track current winning streak
current_streak = 0

# Track maximum streak
max_streak = 0

while True:
    line = input()
    if line == "":
        break
    value = int(line)

    if value == 1:
        # Win: increment current streak
        current_streak += 1
        # Update max if needed
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        # Loss (0): reset current streak
        current_streak = 0

print(f"Maximum streak: {max_streak}")
