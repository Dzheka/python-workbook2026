# Display table header
print("Celsius    Fahrenheit")

# Loop through temperatures from 0 to 100 in steps of 10
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:<11}{fahrenheit:.1f}")
