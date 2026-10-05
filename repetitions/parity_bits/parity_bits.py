n = input()
while n != "":
    if len(n) != 8:
        print("Error")
    else:
        count = n.count("1")
        if count % 2 == 0:
            print("Parity bit: 0")
        else:
            print("Parity bit: 1")
    n = input()