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
