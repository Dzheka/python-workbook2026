"""Tajikistan Banknote Reference Table
Amount	Individual
1 TJS	Mirzo Tursunzoda
3 TJS	Shirinsho Shotemur
5 TJS	Sadriddin Ayni
10 TJS	Mir Said Ali Hamadoni
20 TJS	Abuali ibni Sino
50 TJS	Bobojon Gafurov
100 TJS	Ismoili Somoni
200 TJS	Nusratullo Makhsum
500 TJS	Abuabdullo Rudaki"""

banknotes = {
    1: "Mirzo Tursunzoda",
    3: "Shirinsho Shotemur",
    5: 'Sadriddin Ayni',
    10: "Mir Said Ali Hamadoni",
    20: "Abuali ibni Sino",
    50: "Bobojon Gafurov",
    100: "Ismoili Somoni",
    200: "Nusratullo Makhsum" ,
    500: "Abuabdullo Rudaki",
}

tjs = int(input())
print(banknotes.get(tjs, "Invalid denomination"))