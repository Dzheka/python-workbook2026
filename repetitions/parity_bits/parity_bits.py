while True:
    n = input()
    if n == "":
        break
    if len(n) != 8:
        print("Error: input must be exactly 8 bits")
        continue
    count = 0
    for bit in n:
        if bit == "1":
            count += 1
    print("Parity bit:", count % 2)