S1=float(input("Enter the first side of the triangle: ".strip()))
S2=float(input("Enter the second side of the triangle: ".strip()))
S3=float(input("Enter the third side of the triangle: ".strip()))
S= (S1 + S2 + S3) / 2
area= (S * (S - S1) * (S - S2) * (S - S3)) ** 0.5
print(f"{area:.2f}")

"""s = (s1 + s2 + s3) / 2 (semi-perimeter)
Area = √(s × (s - s1) × (s - s2) × (s - s3))"""

