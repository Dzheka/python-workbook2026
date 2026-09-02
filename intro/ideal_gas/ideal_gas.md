# Exercise: Ideal Gas Law

Write a program that calculates the amount of gas in moles using the ideal gas law.

## Examples

**Example 1:**

```
Enter pressure (Pascals): 20000000
Enter volume (liters): 12
Enter temperature (°C): 20
```

```
Amount of gas: 98.47 moles
```

**Example 2:**

```
Enter pressure (Pascals): 101325
Enter volume (liters): 22.4
Enter temperature (°C): 0
```

```
Amount of gas: 1.00 moles
```

**Example 3:**

```
Enter pressure (Pascals): 500000
Enter volume (liters): 5
Enter temperature (°C): 25
```

```
Amount of gas: 1.01 moles
```

## Formula

`PV = nRT` → `n = PV / (RT)` where:

- `P` = pressure in Pascals
- `V` = volume in cubic meters (convert from liters: `1 liter = 0.001 m³`)
- `n` = amount in moles
- `R = 8.314 J/(mol·K)` (ideal gas constant)
- `T` = temperature in Kelvin = `°C + 273.15`
