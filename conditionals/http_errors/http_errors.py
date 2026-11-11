a=str(input())
if a[0] == "1" and len(a) == 3:
    print("Informational")
elif a[0] == "2" and len(a) == 3:
    print("Success")
elif a[0] == "3" and len(a) == 3:
    print("Redirection")
elif a[0] == "4" and len(a) == 3:
    print("Client Error")
elif a[0] == "5" and len(a) == 3:
    print("Server Error")
else:
    print("Unknown status code")
