s = input().strip()
if len(s) != 8 or set(s) - {"0", "1"}:
    print("error")
else:
    print(s.count("1") % 2)
