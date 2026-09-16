#10

#Final velocity: 14.00 m/s

#vf = √(vi² + 2ad) where:

#vi = 0 (initial velocity, dropped)
#a = 9.8 m/s² (acceleration due to gravity)
#d = height (distance fallen)


n=float(input("Enter the height in meters: "))
vf = (2 * 9.8 * n) ** 0.5
print(f"Final velocity: {vf:.2f} m/s")
