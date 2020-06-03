import pymysql

def k_logowanie(login, haslo):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "SELECT klient.k_login FROM klient WHERE k_login LIKE %s;"
    sql1= "SELECT klient.k_haslo FROM klient WHERE k_haslo LIKE %s;"

    if (cur.execute(sql, login) ) and (cur.execute(sql1,haslo)) ==1:
        print("logowanie pomyslne")
    else:
        print("logowanie nie udało się")
    connection.close()

def p_logowanie(login, haslo):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "SELECT pracownik.p_login FROM pracownik WHERE p_login LIKE %s;"
    sql1= "SELECT pracownik.p_haslo FROM pracownik WHERE p_haslo LIKE %s;"

    if (cur.execute(sql, login) ) and (cur.execute(sql1,haslo)) == 1:
        print("logowanie pomyslne")
    else:
        print("logowanie nie udało się")

    connection.close()


# 1 WYPISANIE PRODUKTOW W ZALEZNOSCI OD CENY
def wypisanie_produktow():
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    cur.execute(
        "SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;")
    i = 1
    for row in cur.fetchall():
        print("Pozycja: ", i, " ", row[0], "|", row[1])
        i += 1

    connection.close()

#2 DODANIE PRACOWNIKA
def dodanie_pracownika(imie, nazwisko, pensja, stanowisko, login, haslo):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "INSERT INTO pracownik (id_pracownik, imie, nazwisko, pensja, id_stanowisko, p_login, p_haslo) VALUES (NULL, %s, %s, %s, (SELECT id_stanowisko FROM stanowisko where stanowisko LIKE %s), %s, %s);"

    cur.execute(sql, (imie, nazwisko, pensja, stanowisko, login, haslo))
    connection.commit()
    connection.close()

#3 WYSTAWIENIE FAKTURY
def faktura(klogin):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql1 = "INSERT INTO faktura (id_faktura, wartosc, id_klient) VALUES (NULL, NULL, (SELECT id_klient FROM klient WHERE k_login LIKE %s));"
    cur.execute(sql1, klogin)
    connection.commit()

    pomoc = "SELECT MAX(id_faktura) FROM faktura;"
    cur.execute(pomoc)


    sql2 = "UPDATE zamowienie SET id_faktura = (SELECT MAX(id_faktura) FROM faktura) WHERE id_faktura IS NULL AND klogin LIKE %s;"
    cur.execute(sql2, klogin)
    connection.commit()

    wartosc = 0

    pomoc2 = "SELECT MIN(id_zamowienie), MAX(id_zamowienie) FROM zamowienie WHERE klogin = %s;"
    cur.execute(pomoc2, klogin)
    for row in cur.fetchall():
        min = row[0]
        max = row[1]

    for i in range(min, max+1, 1):
        cena = "SELECT cena from cena where id_cena = (SELECT id_cena FROM produkt WHERE id_produkt = (SELECT id_produkt FROM zamowienie WHERE id_zamowienie = %s) );"
        cur.execute(cena, i)
        for row in cur.fetchall():
            temp1 = row[0]
        ilosc = "SELECT ilosc FROM zamowienie WHERE id_zamowienie = %s;"
        cur.execute(ilosc, i)
        for row in cur.fetchall():
            temp2 = row[0]
        wynik = temp1*temp2
        wartosc += wynik

    sql3 = "UPDATE faktura SET wartosc = %s WHERE id_faktura = (SELECT MAX(id_faktura) FROM faktura);"

    cur.execute(sql3, wartosc)
    connection.commit()

    connection.close()

# 4 ZAKTUALIZOWANIE CENY
def aktualizacja_ceny(zmiana ,nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "UPDATE cena SET cena.cena = cena.cena + %s WHERE id_cena = (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE %s);"

    cur.execute(sql, (zmiana, nazwa))
    connection.commit()
    connection.close()

#5 USUNIECIE PRODUKTU
def usuniecie_produktu(nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "DELETE FROM produkt WHERE nazwa_produktu LIKE %s;"

    cur.execute(sql, nazwa)
    connection.commit()
    connection.close()

#6 DODANIE PRODUKTU DO SPRZEDAŻY
def dodanie_produktu(cena,sekcja, nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    sql="INSERT INTO produkt (id_produkt,id_cena, id_sekcja , nazwa_produktu, ilosc_produktow) VALUES (0, (SELECT id_cena FROM cena WHERE cena = %s), (SELECT id_sekcja FROM sekcja WHERE sekcja LIKE %s), %s, 2);"

    wstaw=(cena,sekcja,nazwa)

    cur.execute(sql ,wstaw)
    connection.commit()
    connection.close()

#7 ZAKTUALIZOWANIE PENSJI PRACOWNIKA
def aktualizacja_pensji(zmiana ,imie, nazwisko):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "UPDATE pracownik SET pensja = pensja + %s WHERE imie LIKE %s AND nazwisko LIKE %s"


    cur.execute(sql, (zmiana, imie, nazwisko))
    connection.commit()
    connection.close()

#8 WYPISANIE ILOSCI RODZAJOW PRODUKTOW, ORAZ SUMARYCZNA ILOSC PRODUKTOW W SEKCJI
def zliczenie_sekcjami():
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    cur.execute("SELECT sekcja.sekcja, COUNT(produkt.id_produkt) AS rodzaje,SUM(produkt.ilosc_produktow) as produkty FROM produkt INNER JOIN sekcja ON produkt.id_sekcja = sekcja.id_sekcja GROUP BY sekcja;")

    for row in cur.fetchall():
        print("Sekcja:", row[0], "| rodzaje produktów: ", row[1],"|", "ilość produktów w danej sekcji:",row[2])

    connection.close()

#9 REJERSTRACJA KLIENTA
def rejestracja(imie, nazwisko, NIP, login, haslo):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "INSERT INTO klient (id_klient, imie, nazwisko, NIP, k_login, k_haslo) VALUES (NULL, %s, %s, %s, %s, %s);"

    cur.execute(sql, (imie, nazwisko, NIP, login, haslo))
    connection.commit()
    connection.close()

#10 WYPISANIE PRACOWNIKOW
def wypisanie_pracownikow():
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()
    cur.execute(
        "SELECT stanowisko.stanowisko, pracownik.imie, pracownik.nazwisko FROM pracownik INNER JOIN stanowisko ON pracownik.id_stanowisko = stanowisko.id_stanowisko ORDER BY stanowisko.stanowisko DESC;")
    i = 1
    for row in cur.fetchall():
        print("Pracownik", i, " ", row[0], "|", row[1], "|", row[2])
        i += 1

    connection.close()


# 11 WYPISANIE PRODUKTU PO NAZWIE
def nazwa_produkt(nazwa):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    sql = "SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE nazwa_produktu LIKE %s;"

    cur.execute(sql, nazwa)
    for row in cur.fetchall():
        print(row[0], "|", row[1])

    connection.close()


# 12 WYPISANIE WSZYSTKICH PRODUKTOW WRAZ Z ICH ILOSCIĄ
def wszystkie_produkty():
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    cur.execute("SELECT nazwa_produktu, ilosc_produktow FROM produkt;")
    i = 1
    for row in cur.fetchall():
        print("Pozycja", i, " ", row[0], "|", row[1])
        i += 1

    connection.close()
#13 Aktualizacja ilości produktów
def aktualizacja_ilosc(zmiana, nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow + %s WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE %s);"

    cur.execute(sql, (zmiana, nazwa))
    connection.commit()
    connection.close()

#14 Złożenie zamówienia
def zamowienie(nazwa, data, ilosc, login):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()
    sql = "INSERT INTO zamowienie (id_zamowienie,id_produkt, data_zamowienia, id_pracownik, ilosc, id_faktura, klogin) VALUES (NULL, (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE %s), %s, 11, %s, NULL, %s);"
    cur.execute(sql, (nazwa, data, ilosc, login))
    connection.commit()
    pomoc2 = "UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow - %s WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE %s);"
    cur.execute(pomoc2, (ilosc, nazwa))
    connection.commit()
    connection.close()

#15 Przydzielenie zadań
def zadanie(imie, nazwisko, numer):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()
    sql = "UPDATE zamowienie SET id_pracownik = (SELECT id_pracownik FROM pracownik WHERE imie LIKE %s AND nazwisko LIKE %s) WHERE id_zamowienie = %s;"
    cur.execute(sql,(imie, nazwisko, numer))
    connection.commit()
    connection.close()

#16 Wypisanie zamówień
def zamowienie_2():
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()
    cur.execute("SELECT zamowienie.id_zamowienie, produkt.nazwa_produktu, zamowienie.data_zamowienia, pracownik.imie, pracownik.nazwisko, zamowienie.ilosc FROM zamowienie INNER JOIN produkt ON zamowienie.id_produkt = produkt.id_produkt INNER JOIN pracownik ON zamowienie.id_pracownik = pracownik.id_pracownik;")
    for row in cur.fetchall():
        print("Numer zamówienia: ", row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "| Ilość:", row[5])
    connection.close()

#17 Wypisanie faktur
def wypisanie_faktur(login):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()
    sql = "SELECT id_faktura, wartosc FROM faktura WHERE id_klient = (SELECT id_klient FROM klient WHERE k_login like %s LIMIT 1);"
    cur.execute(sql, login)
    for row in cur.fetchall():
        print("Faktura numer: ", row[0], "| Wartość", row[1])
    connection.close()

def szczegoly(numer):
        connection = pymysql.Connect(
            host='localhost',
            user="root",
            password="",
            db="hurtownia2",
        )

        cur = connection.cursor()
        sql = "SELECT produkt.nazwa_produktu, zamowienie.ilosc, cena.cena FROM zamowienie INNER JOIN produkt ON zamowienie.id_produkt = produkt.id_produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE zamowienie.id_faktura = %s;"
        cur.execute(sql, numer)
        for row in cur.fetchall():
            print(row[0], " | ", row[1], "*", row[2])
        sql2 = "SELECT wartosc FROM faktura WHERE id_faktura = %s "
        cur.execute(sql2, numer)
        for row in cur.fetchall():
            print("Wartość całkowita: ", row[0])
        connection.close()

#18 Wypisanie wszystkich faktur
def wypisanie_faktur_kasjer():
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()
    sql = ""
    cur.execute(sql)
    for row in cur.fetchall():
        print("Faktura numer: ", row[0], "| Wartość", row[1], "| Login klienta", row[2])
    connection.close()