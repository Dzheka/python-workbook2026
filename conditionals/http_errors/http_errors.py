n=int(input())
if n>=100 and n<=199 :
    print("Informational")
elif n>=200 and n<=299 :
    print("Success")
elif n>=300 and n<=399 :
    print("Redirection")
elif n>=400 and n<=499 :
    print("Client Error")
elif n>=500 and n<=599 :
    print("Server Error")
else :
    print("Unknown status code")