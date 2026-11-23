#Enter number of sides: 6
#Enter side length: 4

#41.57
#Area = (n × s²) / (4 × tan(π/n)) where:

#n = number of sides
#s = side length

import math


n = int(input("Enter number of sides: "))
s = float(input("Enter side length: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))
print(f"{area:.2f}")