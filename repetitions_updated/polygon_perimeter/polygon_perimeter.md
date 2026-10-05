# Compute the Perimeter of a Polygon

Calculate the perimeter of a polygon by reading coordinate points from the user.

## Task
- Read x and y coordinates for the first point
- Continue reading coordinate pairs until user enters blank for x
- Calculate distance between consecutive points
- Add distance from last point back to first point
- Display the total perimeter

## Formula
Distance between two points: `√((x₂ - x₁)² + (y₂ - y₁)²)`

## Example
```
Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the next x-coordinate (blank to quit): 1
Enter the next y-coordinate: 0
Enter the next x-coordinate (blank to quit): 0
Enter the next y-coordinate: 1
Enter the next x-coordinate (blank to quit): 
The perimeter of that polygon is 3.414213562373095
```
