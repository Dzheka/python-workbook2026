a = input()
if a=="A+":
    print(f"{4:.1f}") 
elif a=="A":
    print(f"{4:.1f}")   
elif a=="A-":
    print("3.7")   
elif a=="B+":
    print(f"3.3")   
elif a=="B":
    print(f"{3:.1f}")   
elif a=="B-":
    print("2.7")   
elif a=="C+":
    print("2.3")   
elif a=="C":
    print(f"{2:.1f}")   
elif a=="C-":
    print("1.7")   
elif a=="D+":
    print("1.3")   
elif a=="D":
    print(f"{1:.1f}")   
elif a=="F":
    print("0.0")   
else:
    print("Invalid grade")