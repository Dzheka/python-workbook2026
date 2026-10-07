n=101
print (f"{"Celsius":<11}Fahrenheit")
for i in range (0,101,10):
    print (f"{i:<11}{i*9/5+32:.1f}")