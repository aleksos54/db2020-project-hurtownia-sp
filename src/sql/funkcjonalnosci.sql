-- 1 Wypisanie wszystkich produktów i posortowanie ich względem ceny malejąco
SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;
-- 2 Dodanie nowo zatrudnionego pracownika
INSERT INTO pracownik (id_pracownik, imie, nazwisko, pensja, id_stanowisko) VALUES (NULL, "przyklad_imie", "przyklad_nazwisko", 9999, (SELECT id_stanowisko FROM stanowisko where id_stanowisko=2));
-- 3 Wystawienie faktury
INSERT INTO faktura (id_faktura, wartosc, id_klient) VALUES (NULL, NULL, (SELECT id_klient FROM klient WHERE k_login LIKE "kjan"));
UPDATE zamowienie SET id_faktura = (SELECT MAX(id_faktura) FROM faktura) WHERE id_faktura IS NULL AND klogin LIKE "kjan";
UPDATE faktura SET wartosc = 95 WHERE id_faktura = (SELECT MAX(id_faktura) FROM faktura);
-- 4 Zaktualizowanie ceny
UPDATE cena SET cena.cena = cena.cena*0.5 WHERE (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE "Jacuzzi");
-- 5 Wycofanie produktu ze sprzedaży
DELETE FROM produkt WHERE nazwa_produktu LIKE "Jacuzzi";
-- 6 Dodanie produktu do sprzedaży
INSERT INTO produkt (id_produkt,id_cena, id_sekcja , nazwa_produktu, ilosc_produktow) VALUES (0, (SELECT id_cena FROM cena WHERE cena = 7000), (SELECT id_sekcja FROM sekcja WHERE sekcja LIKE "Ogrodnicza"), "Jacuzzi", 2);
-- 7 Zaktualizowanie pensji pracownika
UPDATE pracownik SET pensja = pensja + 100 WHERE imie LIKE "Krzysztof" AND nazwisko LIKE "Krawczyk";
-- 8 Wypisanie ilości rodzajów produktów oraz sumaryczna ilość produktów w danej sekcji
SELECT COUNT(produkt.id_produkt) AS rodzaje,SUM(produkt.ilosc_produktow) as produkty, sekcja.sekcja FROM produkt INNER JOIN sekcja ON produkt.id_sekcja = sekcja.id_sekcja GROUP BY sekcja;
-- 9 Rejestracja nowego klienta
INSERT INTO klient (id_klient, imie, nazwisko, NIP) VALUES (NULL, "przyklad", "przyklad", "9999999999");
-- 10  Wypisanie wszystkich pracowników sortujac ich według stanowiska
SELECT stanowisko.stanowisko, pracownik.imie, pracownik.nazwisko FROM pracownik INNER JOIN stanowisko ON pracownik.id_stanowisko = stanowisko.id_stanowisko ORDER BY stanowisko.stanowisko DESC;
-- 11 Wyszukanie produktu po nazwie, przykładowo kilent chce wyszukać Jacuzzi
SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE nazwa_produktu LIKE "Jacuzzi";
-- 12 Wypisanie wszystkich produktów wraz z ich ilością
SELECT nazwa_produktu, ilosc_produktow FROM produkt;
-- 13 Aktualizacja ilości produktów
UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow + %s WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE Jacuzzi);
-- 14 Złożenie zamówienia
INSERT INTO zamowienie (id_zamowienie,id_produkt, data_zamowienia, id_pracownik, ilosc, id_faktura) VALUES (NULL, (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE Jacuzzi), "2020-05-27", 11, 1, NULL);
UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow - 1 WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE Jacuzzi);
-- 15 Przydzielenie zadań
UPDATE zamowienie SET id_pracownik = (SELECT id_pracownik FROM pracownik WHERE imie LIKE Jacek AND nazwisko LIKE Placek) WHERE id_zamowienie = 1;
-- 16 Wyświetlenie zamówień
SELECT zamowienie.id_zamowienie, produkt.nazwa_produktu, zamowienie.data_zamowienia, pracownik.imie, pracownik.nazwisko, zamowienie.ilosc FROM zamowienie INNER JOIN produkt ON zamowienie.id_produkt = produkt.id_produkt INNER JOIN pracownik ON zamowienie.id_pracownik = pracownik.id_pracownik;
-- 17 Wypisanie faktury - klient chce obejrzeć wszystkie swoje faktury, wyświetlają mu się one w wersji skróconej. Jeśli chce zobaczyć szczegóły jednej z nich musi wprowadzić jej numer id.
SELECT id_faktura, wartosc FROM faktura WHERE id_klient = (SELECT id_klient FROM zamowienie WHERE klogin like "kjan" LIMIT 1);
SELECT produkt.nazwa_produktu, zamowienie.ilosc, cena.cena FROM zamowienie INNER JOIN produkt ON zamowienie.id_produkt = produkt.id_produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE zamowienie.id_faktura = 4;
SELECT wartosc FROM faktura WHERE id_faktura = 4; 