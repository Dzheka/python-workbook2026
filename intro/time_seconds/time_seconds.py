second = int(input())
minutes = second // 60
to_seconds = second - (second // 60 * 60)
print(f"{second} second(s) = {minutes} minute(s) and {to_seconds} second(s)")
