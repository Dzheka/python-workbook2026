print("Celsius    Fahrenheit")
for c in range(0, 101, 10):
    print(f"{c:<10} {c * 9 / 5 + 32}")