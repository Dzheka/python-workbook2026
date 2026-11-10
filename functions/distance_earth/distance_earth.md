# Distance on Earth

Write a function that calculates the great-circle distance between two points on Earth.

## Task
- Create a function `distance_earth(lat1, lon1, lat2, lon2)` 
- Takes latitude and longitude of two points in degrees
- Return the distance in kilometers

## Examples

| Call                                                    | Returns  |
|---------------------------------------------------------|----------|
| `distance_earth(0, 0, 0, 0)`                            | `0.0`    |
| `distance_earth(40.7128, -74.0060, 34.0522, -118.2437)` | ~5574 km |

## Formula (Haversine)
- Convert degrees to radians
- a = sin²(Δlat/2) + cos(lat1) × cos(lat2) × sin²(Δlon/2)
- c = 2 × atan2(√a, √(1-a))
- distance = R × c (where R = 6371 km, Earth's radius)
