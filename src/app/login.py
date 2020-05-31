from polecenia_bazy import *
from klient import *


def interfejs_logowanie_rejestracja():
    print("Witamy w hurtowni SP")
    print("1. ZAREJESTRUJ")
    print("2. ZALOGUJ")
    opcja = int(input("Co chcesz zrobić: "))

    if opcja == 1:
        print("Wybrano opcje ZAREJESTRUJ")
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        NIP = input("Podaj NIP: ")
        login = input("Podaj login: ")
        haslo = input("Podaj haslo: ")
        rejestracja(imie, nazwisko, NIP, login, haslo)
        print("REJESTRACJA POPRAWNA")
        klient()
    elif opcja == 2:
        print("Wybrano opcje ZALOGUJ")
        login = input("Podaj login: ")
        haslo = input("Podaj haslo: ")
        # if k_logowanie(login, haslo) == 1:
        k_logowanie(login,haslo)
        klient()
    else:
        print("Wybrano nieprawidłową opcje!!!")

