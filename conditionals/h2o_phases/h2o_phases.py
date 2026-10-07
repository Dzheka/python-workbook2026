"""Write a program that determines the phase of water based on temperature.

Temperature Ranges
Temperature (°C)	Phase
Below 0	solid
0 to 100	liquid
Above 100	gas"""

i = int(input())

if i < 0:
    print('solid')
elif i == 0:
    print("solid or liquid")
elif 0 < i < 100:
    print('liquid')
elif i == 100:
    print("liquid or gas")
elif i > 100:
    print('gas')