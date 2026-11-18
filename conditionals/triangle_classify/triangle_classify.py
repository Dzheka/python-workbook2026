"""A triangle can be classified based on the lengths of its sides as equilateral, isosceles, or scalene. Write a program that reads the lengths of three sides and determines the triangle's type.

Triangle Classifications
Equilateral: All three sides have the same length
Isosceles: Two sides have the same length, and the third side has a different length
Scalene: All three sides have different lengths
"""
a = int(input())
b = int(input())
c =int(input())

if a == b and b == c and c == a:
    print('equilateral')
elif a == b or b == c or c == a:
    print('isosceles')
else:
    print('scalene')