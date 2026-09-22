a = int(input())
if a<3*(10**9):
    print("Radio Waves")
elif 3*(10**9)<=a<3*(10**12):
    print("Microwaves")
elif 3*(10**12)<=a<4.3*(10**14):
    print("Infrared Light")
elif 4.3*(10**14)<=a<7.5*(10**14):
    print("Visible Light")
elif 7.5*(10**14)<=a<3*(10**17):
    print("Ultraviolet Light")
elif 3*(10**17)<=a<3*(10**19):
    print("X-Rays")
elif a>=3*(10*19):
    print("Gamma Rays")
