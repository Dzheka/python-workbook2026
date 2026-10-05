seconds = int(input())

days = seconds // (24 * 60 * 60)
hours = (seconds % (24 * 60 * 60)) // (60 * 60)
minutes = (seconds % (60 * 60)) // 60
remaining_seconds = seconds % 60

print(f"{days}:{hours:02d}:{minutes:02d}:{remaining_seconds:02d}")
