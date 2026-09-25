max_streak = 0
current_streak = 0
while True:
    n = input()
    if n == '':
        break
    if int(n) == 1:
        current_streak += 1
        if max_streak < current_streak:
            max_streak = current_streak
    else:
        current_streak = 0

print("Maximum streak:", max_streak)