total_seconds = int(input())

days = total_seconds // 86400
hours = (total_seconds % 86400) // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{days}:{hours:02d}:{minutes:02d}:{seconds:02d}")
