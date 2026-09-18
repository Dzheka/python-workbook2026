"""Shape Names
Sides	Shape Name
3	Triangle
4	Quadrilateral
5	Pentagon
6	Hexagon
7	Heptagon
8	Octagon
9	Nonagon
10	Decagon
Examples
Example 1:

3
Triangle"""
shapes = ['Invalid number of sides', 'Invalid number of sides', 'Invalid number of sides', 'Triangle', 'Quadrilateral',
'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon']

n = int(input())

if n > 10 or n < 0:
    print('Invalid number of sides')
else:
    print(shapes[n])