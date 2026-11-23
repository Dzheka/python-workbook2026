total_seconds = int(input())

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{total_seconds} second(s) = {minutes} minute(s) and {seconds} second(s)")