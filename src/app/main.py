from login import *
from pracownik import *

def main():
    print("\n1. PRACOWNIK")
    print("2. KLIENT")
    tryb = int(input("Wybierz tryb: "))
    if(tryb == 1):
        interfejs_pracownik()
    elif(tryb == 2):
        interfejs_logowanie_rejestracja()
    else:
        print("BŁĘDNY WYBÓR")
        return main()

main()