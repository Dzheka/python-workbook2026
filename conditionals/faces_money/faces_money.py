amount = int(input())

match amount:
    case 1:
        print("Mirzo Tursunzoda")
    case 3:
        print("Shirinsho Shotemur")
    case 5:
        print("Sadriddin Ayni")
    case 10:
        print("Mir Said Ali Hamadoni")
    case 20:
        print("Abuali ibni Sino")
    case 50:
        print("Bobojon Gafurov")
    case 100:
        print("Ismoili Somoni")
    case 200:
        print("Nusratullo Makhsum ")
    case 500:
        print("Abuabdullo Rudaki")
    case _:
        print("Invalid denomination")