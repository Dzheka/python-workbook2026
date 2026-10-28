a=int(input())

if a >= 100 and a <= 199 : 
    print("Informational")
elif a >= 200 and a <= 299 :
    print("Success")
elif a >= 300 and a <= 399 :
    print("Redirection")
elif a >= 400 and a <= 499 :
    print("Client Error")
elif a >= 500 and a <= 599 :
    print("Server Error")
else :
    print("Unknown status code")