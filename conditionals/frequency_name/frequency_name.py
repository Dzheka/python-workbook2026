n=int(input())
if n<3*(10**9):
    print("Radio Waves")
elif n>=3*(10**9) and n<3*(10**12) :
    print("Microwaves")
elif n>=3*(10*12) and n<4.3*(10**14) :
    print("Infrared Light")
elif  n>=4.3*(10**14) and n<7.5*(10**14):
    print("Visible Light")
elif n>=7.5*(10**14) and n<3*(10**17):
    print("Ultraviolet Light")
elif n>=3*(10**17) and n<3*(10**19) :
    print("X-Rays")
else :
    print("Gamma Rays")