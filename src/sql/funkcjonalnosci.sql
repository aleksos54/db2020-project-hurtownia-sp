#1
SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;
#2
INSERT INTO pracownik (id_pracownik, imie, nazwisko, pensja, id_stanowisko) VALUES (NULL, "przyklad_imie", "przyklad_nazwisko", 9999, (SELECT id_stanowisko FROM stanowisko where id_stanowisko=2));
#3
INSERT INTO faktura (id_faktura, wartosc, id_klient) VALUES (NULL, NULL, 1)
INSERT INTO zamowienie (id_zamowienie,id_produkt, data_zamowienia, id_pracownik, ilosc, id_faktura) VALUES (NULL, (SELECT id_produkt FROM produkt WHERE id_produkt = 5), "2020-05-17", (SELECT id_pracownik FROM pracownik WHERE id_pracownik= 4), 2, (SELECT id_faktura FROM faktura WHERE id_faktura = 3));
UPDATE faktura SET faktura.wartosc = (SELECT ilosc FROM zamowienie WHERE id_zamowienie = 2) * (SELECT cena FROM cena INNER JOIN produkt ON cena.id_cena = produkt.id_cena WHERE produkt.id_produkt = 5) WHERE id_faktura = 3;
#4
UPDATE cena SET cena.cena = cena.cena*0.5 WHERE (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE "Jacuzzi");
#5
DELETE FROM produkt WHERE nazwa_produktu LIKE "Jacuzzi";
#6
INSERT INTO produkt (id_produkt,id_cena, id_sekcja , nazwa_produktu, ilosc_produktow) VALUES (0, (SELECT id_cena FROM cena WHERE cena = 7000), (SELECT id_sekcja FROM sekcja WHERE sekcja LIKE "Ogrodnicza"), "Jacuzzi", 2);
#7
UPDATE pracownik SET pensja = pensja + 100 WHERE imie LIKE "Krzysztof" AND nazwisko LIKE "Krawczyk";
#8
SELECT COUNT(produkt.id_produkt) AS rodzaje,SUM(produkt.ilosc_produktow) as produkty, sekcja.sekcja FROM produkt INNER JOIN sekcja ON produkt.id_sekcja = sekcja.id_sekcja GROUP BY sekcja;
#9
INSERT INTO klient (id_klient, imie, nazwisko, NIP) VALUES (NULL, "przyklad", "przyklad", "9999999999");
#10
SELECT stanowisko.stanowisko, pracownik.imie, pracownik.nazwisko FROM pracownik INNER JOIN stanowisko ON pracownik.id_stanowisko = stanowisko.id_stanowisko ORDER BY stanowisko.stanowisko DESC;
#11
SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE nazwa_produktu LIKE "Jacuzzi";
#12
SELECT nazwa_produktu, ilosc_produktow FROM produkt;

