a = int(input())

if a<= 300000000 :
 print("Radio Waves")
elif a>= 300000000 and a<= 300000000000 :
 print("Microwaves")
elif a>= 300000000000 and a<= 43000000000000 :
 print("Infrared Light")
elif a>= 43000000000000 and a<= 75000000000000:
 print("Visible Light")
elif a>= 75000000000000 and a<=300000000000000000:
 print("Ultraviolet Light")
elif a>=300000000000000000 and a<=30000000000000000000:
 print("X-Rays")
else:
 print("Gamma Rays")