from polecenia_bazy import *
from klient import *
import getpass

def interfejs_logowanie_rejestracja():
    print("Witamy w hurtowni SP")
    print("1. ZAREJESTRUJ")
    print("2. ZALOGUJ")
    print("3. WYJŚCIE")
    opcja = int(input("Co chcesz zrobić: "))

    if opcja == 1:
        print("Wybrano opcje ZAREJESTRUJ")
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        NIP = input("Podaj NIP: ")
        login = input("Podaj login: ")
        haslo = getpass.getpass("Podaj haslo: ")
        rejestracja(imie, nazwisko, NIP, login, haslo)
        print("REJESTRACJA POPRAWNA")
        print("Witamy!")
        klient(login)
    elif opcja == 2:
        print("Wybrano opcje ZALOGUJ")
        login = input("Podaj login: ")
        haslo = getpass.getpass("Podaj haslo: ")
        k_logowanie(login, haslo)
        print("Witamy!")
        klient(login)
    elif opcja == 3:
        exit()
    else:
        print("Wybrano nieprawidłową opcje!!!")
        return interfejs_logowanie_rejestracja()