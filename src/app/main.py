from login import *
from pracownik import *


print("1. PRACOWNIK")
print("2. KLIENT")
tryb = int(input("Wybierz tryb: "))

if(tryb == 1):
    interfejs_pracownik()
elif(tryb == 2):
    interfejs_logowanie_rejestracja()
else:
    print("BŁĘDNY WYBÓR")



#test()
#wypisanie_produktow()

#
# nazwa = input("Podaj nazwe produktu: ")
# #nazwa_produkt(nazwa)
#
# #10
# #wypisanie_pracownikow()
#
# aktualizacja_ceny(nazwa)
#wypisanie_produktow()


# for i in range(8):
#     print(i)
# print(i)
