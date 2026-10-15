"""186330
2:03:45:30
I know that this code is ugly"""
sec = int(input())
days = sec // (60**2*24)
sec -= days * 60**2*24
hours = sec //(60**2)
sec -= hours * 60**2
minutes = sec // 60
sec -= minutes * 60


print(f"{days}:{hours:02d}:{minutes:02d}:{sec:02d}")