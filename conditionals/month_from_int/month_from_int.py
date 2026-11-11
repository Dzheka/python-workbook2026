months = ["Invalid month number", 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

i = int(input())

if i <= len(months) - 1 and (i > 0):
    print(months[i])
else:
    print(months[0])


"""Examples
Example 1:

1
January
Example 2:

6
June
Example 3:

13
Invalid month number"""