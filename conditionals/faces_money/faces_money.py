money = {
    1: "Mirzo Tursunzoda",
    3: "Shirinsho Shotemur",
    5: "Sadriddin Ayni",
    10: "Mir Said Ali Hamadoni",
    20: "Abuali ibni Sino",
    50: "Bobojon Gafurov",
    100: "Ismoili Somoni",
    200: "Nusratullo Makhsum",
    500: "Abuabdullo Rudaki"
}

a = input()

if a.isdigit():
    a = int(a)
    if a in money:
        print(money[a])
    else:
        print("Invalid denomination")
else:
    print("Invalid denomination")