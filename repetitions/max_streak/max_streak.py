current_streak = 0

max_streak = 0

while True:
    line = input()
    if line == "":
        break
    value = int(line)

    if value == 1:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0

print(f"Maximum streak: {max_streak}")
