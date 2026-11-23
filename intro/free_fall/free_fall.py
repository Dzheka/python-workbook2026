import math
height = int(input())
vi = 0
a = 9.8  
vf = math.sqrt(vi**2 + 2 * a * height) 
print(f"Final velocity: {vf:.2f} m/s")