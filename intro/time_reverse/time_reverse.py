#186330

#2:03:45:30

total_seconds=int(input("Enter the total number of seconds: "))
days=total_seconds//(24*60*60)
remaining_seconds=total_seconds%(24*60*60)
hours=remaining_seconds//(60*60)
remaining_seconds=remaining_seconds%(60*60)
minutes=remaining_seconds//60
remaining_seconds=remaining_seconds%60
print(f"{days}:{hours:02d}:{minutes:02d}:{remaining_seconds:02d}")  
