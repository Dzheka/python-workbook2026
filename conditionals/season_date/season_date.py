month_name = input().strip().lower()
day = int(input())

m_str = "janfebmaraprmayjunjulaugsepoctnovdec"
month = (m_str.find(month_name[:3]) // 3) + 1

date_score = month * 100 + day

if 320 <= date_score <= 620:
    print("Spring")
elif 621 <= date_score <= 921:
    print("Summer")
elif 922 <= date_score <= 1220:
    print("Fall")
else:
    print("Winter")
