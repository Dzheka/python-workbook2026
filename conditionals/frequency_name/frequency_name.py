a = int(input())
if a < 3e9:
    print("Radio Waves")
elif a<3e12:
    print("Microwaves")
elif a< 4.3e14:
    print("Infrared Light")
elif a<7.5e14:
    print("Visible Light")
elif a<3e17:
    print("Ultraviolet Light")
elif a<3e19:
    print("X-Rays")
else:
    print("Gamma Rays")


