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
    
# 4 ZAKTUALIZOWANIE CENY
def aktualizacja_ceny(nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "UPDATE cena SET cena.cena = cena.cena* 0.5 WHERE id_cena = (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE %s);"

    cur.execute(sql, nazwa)
    connection.commit()
    connection.close()