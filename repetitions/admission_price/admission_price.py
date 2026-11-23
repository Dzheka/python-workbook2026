total_cost = 0.0

while True:
    line = input()
    if line == "":  # Если строка пустая, выходим из цикла
        break
    
    age = int(line)  # Преобразуем возраст в число
    
    if age <= 2:
        total_cost += 0.0
    elif 3 <= age <= 12:
        total_cost += 14.0
    elif age >= 65:
        total_cost += 18.0
    else:
        total_cost += 23.0

print(f"${total_cost:.2f}")