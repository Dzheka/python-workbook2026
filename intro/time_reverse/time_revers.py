total_seconds = int(input())

days = total_seconds // 86400
remaining = total_seconds % 86400

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
seconds = remaining % 60

print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")