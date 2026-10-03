print(f"{"Celsius":<10} {"Fahrenheit"}")
c = 0
for c in range(0,101,10):
    F = c * 9/5 + 32
    print(f"{c:<10} {F}") 