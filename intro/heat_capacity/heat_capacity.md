# Exercise: Heat Capacity

Write a program that calculates the energy (kWh) required to heat water and the cost in dollars (electricity costs `$0.04/kWh` in Tajikistan).

## Examples

**Example 1:**

```
Enter volume of water (liters): 2
Enter temperature change (°C): 90
```

```
Energy required: 0.21 kWh
Cost to heat water: $0.01
```

**Example 2:**

```
Enter volume of water (liters): 5
Enter temperature change (°C): 80
```

```
Energy required: 0.47 kWh
Cost to heat water: $0.02
```

**Example 3:**

```
Enter volume of water (liters): 10
Enter temperature change (°C): 75
```

```
Energy required: 0.87 kWh
Cost to heat water: $0.03
```

## Formula

- Energy: `q = m × C × 𝚫T` where `C = 4.186 J/(g·°C)`
- Convert to kWh: 1 kWh = 3,600,000 J
- Cost: `cost = kWh × 0.04`
