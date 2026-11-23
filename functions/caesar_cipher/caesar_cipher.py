def caesar_cipher(t,s):
    ans=""
    for i in range(0,len(t)):
        if t[i].isupper():
            x=((ord(t[i])-65)+s)%26
            ans += chr(x+65)
        elif t[i].islower():
            x=((ord(t[i])-97)+s)%26
            ans += chr(x+97)
        else :
            ans+=t[i]

    return ans
