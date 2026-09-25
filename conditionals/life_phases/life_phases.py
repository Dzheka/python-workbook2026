"""Write a program that reads a person's age and determines their life phase.

Life Phase Classifications
Age Range	Life Phase
0-1	Infant
2-4	Toddler
5-10	Child
11-17	Adolescent
18-39	Young Adult
40-64	Middle-aged
65+	Senior"""

age = int(input("Enter age: "))

if age < 0:
    phase = "Invalid age"
elif age <= 1:
    phase = "Infant"
elif age <= 4:
    phase = "Toddler"
elif age <= 10:
    phase = "Child"
elif age <= 17:
    phase = "Adolescent"
elif age <= 39:
    phase = "Young Adult"
elif age <= 64:
    phase = "Middle-aged"
else:
    phase = "Senior"

print(phase)