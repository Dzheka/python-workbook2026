
"""Logic
If age >= 18: can vote
If age < 18: cannot vote
Note
Voting age is 18 in most countries
Use the simple comparison operator
Handle integer ages"""
age = int(input())

if age >= 18:
    print("can vote")
else:
    print("cannot vote")
