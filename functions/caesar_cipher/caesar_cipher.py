def caesar_cipher(text, shift):
    result = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in text:
        if i in lower:
         position = lower.find(i)
         new_position = (position + shift) % 26
         result += lower[new_position]
        elif i in upper:
         position = upper.find(i)
         new_position = (position + shift) % 26
         result += upper[new_position]
        else:
           result+=i
    return result
print(caesar_cipher("abc", 1))
        
