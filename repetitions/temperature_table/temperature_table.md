# Temperature Conversion Table

Display a temperature conversion table for Celsius and Fahrenheit.

## Task
- Create a table with temperatures from 0°C to 100°C
- Include only multiples of 10 (0, 10, 20, ..., 100)
- Show both Celsius and Fahrenheit values
- Include appropriate column headings

## Example Output
```
Celsius    Fahrenheit
0          32.0
10         50.0
20         68.0
30         86.0
40         104.0
50         122.0
60         140.0
70         158.0
80         176.0
90         194.0
100        212.0
```

## Logic
- Use a for loop with `range(0, 101, 10)` for multiples of 10
- Convert Celsius to Fahrenheit using: `F = C × 9/5 + 32`
- Display each row with formatted output
