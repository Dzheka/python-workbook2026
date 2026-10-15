# Exercise: Distance Between Two Points on Earth

Write a program that calculates the distance (in kilometers) between two points on Earth's surface, given each point's latitude and longitude in degrees, using the great circle distance formula.

## Examples

**Example 1: Dushanbe to Khujand (Tajikistan)**

```
Enter latitude of first point: 38.5598
Enter longitude of first point: 68.7870
Enter latitude of second point: 40.2789
Enter longitude of second point: 69.6210
```

```
Distance: 204.14 km
```

**Example 2: Dushanbe to Moscow (Russia)**

```
Enter latitude of first point: 38.5598
Enter longitude of first point: 68.7870
Enter latitude of second point: 55.7558
Enter longitude of second point: 37.6176
```

```
Distance: 2991.43 km
```

**Example 3: Moscow to New York (USA)**

```
Enter latitude of first point: 55.7558
Enter longitude of first point: 37.6176
Enter latitude of second point: 40.7128
Enter longitude of second point: -74.0060
```

```
Distance: 7510.29 km
```

## Formula

First convert every coordinate from degrees to radians, then:

`distance = 6371.01 × arccos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lon1 - lon2))`

where `lat1, lat2, lon1, lon2` are the radian values, and `6371.01` is
Earth's average radius in kilometers.
