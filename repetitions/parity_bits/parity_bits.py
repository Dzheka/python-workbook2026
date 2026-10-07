"""
while True:
    string = input()
    if string.count("1") % 2 == 0:
        print("0")
    else:
        print("1")
"""
while True:
    try:
        string = input()
    except EOFError:
        break
    if string == "":
        break
    if len(string) != 8 or not set(string).issubset({"0", "1"}):
        print("error")
        continue

    # Output parity bit
    if string.count("1") % 2 == 0:
        print("0")
    else:
        print("1")

