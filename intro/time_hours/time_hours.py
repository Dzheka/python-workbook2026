h=float(input())
d=h//24
hl=(h-(24*d))%60
m=(hl%1)*60
print(f"{h} hours = {int(d)} days, {int(hl)} hours, and {int(m)} minutes")