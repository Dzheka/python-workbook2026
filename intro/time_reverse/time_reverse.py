s=int(input())
d=s//86400
h=(s%86400)//3600
m=(s%3600)//60
sl=s%60
print(f"{d}:{h:02d}:{m:02d}:{sl:02d}")