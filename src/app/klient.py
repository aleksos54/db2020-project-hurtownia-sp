from polecenia_bazy import *
import datetime

def klient(login):
    print("\nDostępne opcje: ")
    print("1. Wypisanie produktów")
    print("2. Wyszukanie produktu")
    print("3. Złożenie zamówienia")
    print("4. Wypisanie wszystkich faktur")
    print("5. Wyjscie")
    opcja = int(input("Co chcesz zrobić "))
    if opcja == 1:
        wypisanie_produktow()
        return klient(login)
    elif opcja == 2:
        nazwa = input("Prosze podać nazwe produktu: ")
        nazwa_produkt(nazwa)
        return klient(login)
    elif opcja == 3:
        while(True):
            data = datetime.date.today()
            nazwa = input("Prosze podać nazwe produktu: ")
            ilosc = int(input("Prosze podać ilość: "))
            pytanie = input("Czy chcesz zakończyć: ")
            zamowienie(nazwa, data, ilosc, login)
            if pytanie.lower() == "tak":
                return klient(login)
    elif opcja == 4:
        wypisanie_faktur(login)
        temp = input("Czy chcesz zobaczyć szczegóły faktury ")
        if(temp.lower() == "tak"):
            numer = int(input("Podaj numer faktury: "))
            szczegoly(numer)
            return klient(login)
        else:
            return klient(login)
    elif opcja == 5:
        exit()



