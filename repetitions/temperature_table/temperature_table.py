print(f"{'Celsius':<10} {'Fahrenheit':<10}")

for i in range(0, 101, 10):
    fahrenheit = (i * 9 / 5) + 32
    print(f"{i:<10} {fahrenheit:<10.1f}")
