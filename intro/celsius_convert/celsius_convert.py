#Fahrenheit = (Celsius × 9/5) + 32
#Kelvin: K = C + 273.15


C=float(input("Enter the temperature in Celsius: "))
fahrenheit=float((C * 9/5) + 32)
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
print(f"Temperature in Kelvin: {C + 273.15:.f}")
