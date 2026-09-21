a = int(input())
if 100<=a<=199:
    print("Informational")
elif 200<=a<=299:
    print("Success")
elif 300<=a<=399:
    print("Redirection")
elif 400<=a<=499:
    print("Client Error")
elif 500<=a<=599:
    print("Server Error")
else :
    print ("Unknown status code")