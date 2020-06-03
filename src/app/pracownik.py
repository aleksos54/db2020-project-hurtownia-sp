from polecenia_bazy import *
import getpass

def interfejs_pracownik():
    print("ZALOGUJ SIE")
    login = input("LOGIN: ")
    haslo = getpass.getpass("Podaj haslo: ")
    p_logowanie(login,haslo)
    print("Witamy")
    pracownik(login)


def pracownik(login):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()
    sql = "SELECT stanowisko.stanowisko FROM stanowisko INNER JOIN pracownik ON stanowisko.id_stanowisko = pracownik.id_stanowisko WHERE p_login = %s;"

    cur.execute(sql, login)
    for row in cur.fetchall():
        stanowisko = (row[0])

    connection.close()

    if(stanowisko == "Prezes"):
        print("\nDostępne opcje: ")
        print("1. Dodanie pracownika ")
        print("2. Aktualizacja ceny ")
        print("3. Aktualizacja pensji ")
        print("4. Dodanie produktów ")
        print("5. Sprawdzenie produktów ")
        print("6. Aktualizacja magazynu ")
        print("7. Wyjscie")
        opcja = int(input("Co chce Pan zrobić Prezesie? "))
        if(opcja == 1):
            imie = input("Prosze wprowadzić imie: ")
            nazwisko = input("Prosze wprowadzić nazwisko: ")
            pensja = float(input("Prosze wprowadzić pensje: "))
            stanowisko = input("Prosze wprowadzić stanowisko: ")
            plogin = input("Prosze wprowadzić login pracownika: ")
            phaslo = input("Prosze wprowadzić haslo pracownika: ")
            dodanie_pracownika(imie, nazwisko, pensja, stanowisko, plogin, phaslo)
            print("Dziękujemy pracownik zarejestrowany poprawnie")
            return pracownik(login)
        elif(opcja == 2):
            nazwa = input("Proszę wprowadzić nazwe produktu: ")
            zmiana = float(input("Proszę wprowadzić o ile ma zmienić sie cena: : "))
            aktualizacja_ceny(zmiana, nazwa)
            print("Cena zmieniona")
            return pracownik(login)
        elif(opcja == 3):
            imie = input("Prosze wprowadzić imie osoby, której pensja ulegnie zmianie: ")
            nazwisko = input("Prosze wprowadzić nazwisko osoby, której pensja ulegnie zmianie: ")
            zmiana = float(input("O ile zmieni się pensja wskazanej osoby: "))
            aktualizacja_pensji(zmiana, imie, nazwisko)
            print("Pensja zmieniona")
            return pracownik(login)
        elif(opcja == 4):
            nazwa = input("Podaj nazwe dodawaniego produktu: ")
            sekcja = input("Podaj nazwe sekcji dodawanego produktu: ")
            cena = input("Podaj cene dodawanego produktu: ")
            dodanie_produktu(cena, sekcja, nazwa)
            return pracownik(login)
        elif(opcja == 5):
            wszystkie_produkty()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif(opcja == 6):
            nazwa = input("Wprowadź nazwe produktu: ")
            zmiana = int(input("Wprowadź ilość produktów: "))
            aktualizacja_ilosc(zmiana, nazwa)
            return pracownik(login)
        elif opcja == 7:
            exit()
        else:
            print("BŁĘDNY WYÓR")
            return pracownik(login)
    elif(stanowisko == "Kierownik"):
        print("\nDostępne opcje: ")
        print("1. Sprawdzenie produktu")
        print("2. Aktualizacja magazynu")
        print("3. Dodanie produktów")
        print("4. Usunięcie produktu")
        print("5. Wypisanie zamówień")
        print("6. Przydzielanie zamówień")
        print("7. Wyjscie")
        opcja = int(input("Co chcesz zrobić?: "))
        if(opcja == 1):
            wszystkie_produkty()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif(opcja == 2):
            nazwa = input("Wprowadź nazwe produktu: ")
            zmiana = int(input("Wprowadź ilość produktów: "))
            aktualizacja_ilosc(zmiana, nazwa)
            return pracownik(login)
        elif(opcja == 3):
            nazwa = input("Podaj nazwe dodawaniego produktu: ")
            sekcja = input("Podaj nazwe sekcji dodawanego produktu: ")
            cena = input("Podaj cene dodawanego produktu: ")
            dodanie_produktu(cena, sekcja, nazwa)
            return pracownik(login)
        elif(opcja == 4):
            nazwa = input("Który produkt usunąć: ")
            usuniecie_produktu(nazwa)
            return pracownik(login)
        elif (opcja == 5):
            zamowienie_2()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif (opcja == 6):
            imie = input("Podaj imie pracownika: ")
            nazwisko = input("Podaj nazwisko pracownika: ")
            numer = int(input("Podaj numer zamówienia: : "))
            zadanie(imie, nazwisko, numer)
            return pracownik(login)
        elif opcja == 7:
            exit()
        else:
            print("BŁĘDNY WYBÓR")
            return pracownik(login)
    elif(stanowisko == "Magazynier"):
        print("\nDostępne opcje: ")
        print("1. Sprawdzenie produktu")
        print("2. Sprawdzenie miejsca")
        print("3. Wypisanie zamówień")
        print("4. Wyjscie")
        opcja = int(input("Co chcesz zrobić: "))
        if(opcja == 1):
            wszystkie_produkty()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif (opcja == 2):
            nazwa = input("Podaj nazwe produktu: ")
            connection = pymysql.Connect(
                host='localhost',
                user="root",
                password="",
                db="hurtownia2",
            )
            cur = connection.cursor()
            sql = "SELECT sekcja.sektor_hurtowni FROM sekcja INNER JOIN produkt ON sekcja.id_sekcja = produkt.id_sekcja WHERE produkt.nazwa_produktu LIKE %s;"
            cur.execute(sql, nazwa)
            for row in cur.fetchall():
                print(row[0])
            connection.close()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif (opcja == 3):
            zamowienie_2()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif opcja == 4:
            exit()
        else:
            print("BŁĘDNY WYBÓR")
            return pracownik(login)
    elif (stanowisko == "Kasjer"):
        print("\nWitamy Kasjera")
        print("Dostępne opcje:")
        print("1. Wypisanie produktów: ")
        print("2. Tworzenie faktury: ")
        print("3. Wypisanie faktur")
        print("4. Wyjscie")
        opcja = int(input("Co chce Pan zrobić? "))
        if (opcja == 1):
            wypisanie_produktow()
            pytanie = input("Naciśnij ENTER aby zakończyć")
            if pytanie:
                return pracownik(login)
            return pracownik(login)
        elif(opcja == 2):
            klogin = input("Prosze wprowadzić login klienta: ")
            faktura(klogin)
            return pracownik(login)
        elif opcja == 3:
            wypisanie_faktur_kasjer()
            return pracownik(login)
        elif opcja == 4:
            exit()
        else:
            print("BŁĘDNY WYBÓR")
            return pracownik(login)