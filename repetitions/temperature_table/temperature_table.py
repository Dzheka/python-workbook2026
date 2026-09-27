print(f"{'Celsius':<11}Fahrenheit")

for celsius in range(0, 101, 10):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:<11}{fahrenheit:.1f}")