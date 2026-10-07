frequency = float(input())

if frequency < 3 * 10**9:
    print("Radio Waves")
elif frequency < 3 * 10**12:
    print("Microwaves")
elif frequency < 4.3 * 10**14:
    print("Infrared Light")
elif frequency < 7.5 * 10**14:
    print("Visible Light")
elif frequency < 3 * 10**17:
    print("Ultraviolet Light")
elif frequency < 3 * 10**19:
    print("X-Rays")
else:
    print("Gamma Rays")