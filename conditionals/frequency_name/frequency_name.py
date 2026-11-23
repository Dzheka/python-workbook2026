frequency = int(input())

if frequency < 3_000_000_000:
    print("Radio Waves")
elif frequency < 3_000_000_000_000:
    print("Microwaves")
elif frequency < 430_000_000_000_000:
    print("Infrared Light")
elif frequency < 750_000_000_000_000:
    print("Visible Light")
elif frequency < 300_000_000_000_000_000:
    print("Ultraviolet Light")
elif frequency < 30_000_000_000_000_000_000:
    print("X-Rays")
else:
    print("Gamma Rays")
