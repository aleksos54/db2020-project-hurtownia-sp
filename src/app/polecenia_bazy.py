import pymysql

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
def faktura(klogin , nazwa, data, plogin, ilosc):
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

    for row in cur.fetchall():
        pomoc = row[0]


    sql2 = "INSERT INTO zamowienie (id_zamowienie,id_produkt, data_zamowienia, id_pracownik, ilosc, id_faktura) VALUES (NULL, (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE %s), %s, (SELECT id_pracownik FROM pracownik WHERE p_login LIKE %s), %s, (SELECT id_faktura FROM faktura WHERE id_faktura = %s));"
    cur.execute(sql2, (nazwa, data, plogin, ilosc, pomoc))
    connection.commit()
    pomoc2 = "UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow - %s WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE %s);"
    cur.execute(pomoc2,(ilosc, nazwa))
    connection.commit()

    sql3 = "UPDATE faktura SET faktura.wartosc = (SELECT ilosc FROM zamowienie WHERE id_zamowienie = (SELECT MAX(id_zamowienie) FROM zamowienie)) * (SELECT cena FROM cena INNER JOIN produkt ON cena.id_cena = produkt.id_cena WHERE produkt.nazwa_produktu LIKE %s) WHERE id_faktura = (SELECT MAX(id_faktura) FROM faktura);"
    cur.execute(sql3, nazwa)
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
def dodanie_produktu(sekcja, nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    sql="INSERT INTO produkt (id_produkt,id_cena, id_sekcja , nazwa_produktu, ilosc_produktow) VALUES (0, (SELECT id_cena FROM cena WHERE cena = 7000), (SELECT id_sekcja FROM sekcja WHERE sekcja LIKE %s), %s, 2);"

    cur.execute(sql ,sekcja , nazwa)
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

