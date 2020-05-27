# Temat projektu
**WAŻNE: CAŁY TEKST, KTÓRY SIĘ TUTAJ ZNAJDUJE, MA ZOSTAĆ USUNIĘTY!** Powinny zostać wyłącznie nagłówki (oznaczone znakiem #) oraz tabela z nazwiskami.
Tutaj ma znaleźć się skrótowy opis projektu. W tabeli poniżej proszę uzupełnić swoje nazwisko i imię
.

| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :-------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Kamil Podwika         | WIMiIP  | IS       |   4     | 3     | 2019/2020      |
| Michał Serwaczak        | WIMiIP  | IS       |   4     | 3     | 2019/2020      |

## Projekt bazy danych

Tutaj ma znaleźć się opis projektu bazy danych. Na wstępie proszę zagnieździć obraz schematu w formie wektorowej, najlepiej plik SVG. Dodatkowo, w tej sekcji należy zawrzeć kilka przykładowych zapytań tworzących (lub w razie konieczności, modyfikujących) tabelę, tj. grupa DDL.
![diagram-erd](projekt.svg)

## Implementacja zapytań SQL
Tutaj należy wylistować wszystkie funkcjonalności, wraz z odpowiednimi zapytaniami SQL. W tej sekcji należy zawrzeć wyłącznie zapytania z grupy DML oraz DQL.
1. Wypisanie wszystkich produktów i posortowanie ich względem ceny malejąco
 ```sql
    SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;
```
2. Dodanie nowo zatrudnionego pracownika, przykładowo:
```sql
INSERT INTO pracownik (id_pracownik, imie, nazwisko, pensja, id_stanowisko) VALUES (NULL, "przyklad_imie", "przyklad_nazwisko", 9999, (SELECT id_stanowisko FROM stanowisko where id_stanowisko=2));
```
3. Wystawienie faktury, w aplikacji można w pętli ustawić wartość faktury z kilku zamówień
```sql
INSERT INTO faktura (id_faktura, wartosc, id_klient) VALUES (NULL, NULL, 1);
SELECT MAX(id_faktura) FROM faktura;
UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow - 4 WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE "dluigopis");
UPDATE faktura SET faktura.wartosc = (SELECT ilosc FROM zamowienie WHERE id_zamowienie = (SELECT MAX(id_zamowienie) FROM zamowienie)) * (SELECT cena FROM cena INNER JOIN produkt ON cena.id_cena = produkt.id_cena WHERE produkt.nazwa_produktu LIKE "dlugopis") WHERE id_faktura = (SELECT MAX(id_faktura) FROM faktura);
```
4. Zaktualizowanie ceny, przykładowo:
```sql
UPDATE cena SET cena.cena = cena.cena*2 WHERE id_cena = (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE "Jacuzzi");
```
5. Wycofanie produktu ze sprzedaży, przykładowo:
```sql
DELETE FROM produkt WHERE nazwa_produktu LIKE "Jacuzzi";
```
6. Dodanie produktu do sprzedaży, przykładowo:
```sql
INSERT INTO produkt (id_produkt,id_cena, id_sekcja , nazwa_produktu, ilosc_produktow) VALUES (0, (SELECT id_cena FROM cena WHERE cena = 7000), (SELECT id_sekcja FROM sekcja WHERE sekcja LIKE "Ogrodnicza"), "Jacuzzi", 2);
```
7. Zaktualizowanie pensji pracownika
```sql
UPDATE pracownik SET pensja = pensja + 100 WHERE imie LIKE "Krzysztof" AND nazwisko LIKE "Krawczyk";
```
8. Wypisanie ilości rodzajów produktów oraz sumaryczna ilość produktów w danej sekcji
```sql
SELECT COUNT(produkt.id_produkt) AS rodzaje,SUM(produkt.ilosc_produktow) as produkty, sekcja.sekcja FROM produkt INNER JOIN sekcja ON produkt.id_sekcja = sekcja.id_sekcja GROUP BY sekcja;
```
9. Dodanie nowego klienta
```sql
INSERT INTO klient (id_klient, imie, nazwisko, NIP) VALUES (NULL, "przyklad", "przyklad", "9999999999");
```
10. Wypisanie wszystkich pracowników sortujac ich według stanowiska
```sql
SELECT stanowisko.stanowisko, pracownik.imie, pracownik.nazwisko FROM pracownik INNER JOIN stanowisko ON pracownik.id_stanowisko = stanowisko.id_stanowisko ORDER BY stanowisko.stanowisko DESC;
```
11. Wyszukanie produktu po nazwie, przykładowo kilent chce wyszukać Jacuzzi
```sql
SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE nazwa_produktu LIKE "Jacuzzi";
```
12. Wypisanie wszystkich produktów wraz z ich ilością
```sql
SELECT nazwa_produktu, ilosc_produktow FROM produkt;
```
13. Aktualizacja ilości produktów
```sql
UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow + %s WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE Jacuzzi);
```
14. Złożenie zamówienia
```sql
INSERT INTO zamowienie (id_zamowienie,id_produkt, data_zamowienia, id_pracownik, ilosc, id_faktura) VALUES (NULL, (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE Jacuzzi), "2020-05-27", 11, 1, NULL);
UPDATE produkt SET produkt.ilosc_produktow = produkt.ilosc_produktow - 1 WHERE id_produkt = (SELECT id_produkt FROM produkt WHERE nazwa_produktu LIKE Jacuzzi);
```
15. Przydzielenie zadań
```sql
UPDATE zamowienie SET id_pracownik = (SELECT id_pracownik FROM pracownik WHERE imie LIKE Jacek AND nazwisko LIKE Placek) WHERE id_zamowienie = 1;
```

## Aplikacja
Tutaj należy opisać aplikację, która wykorzystuje zapytania SQL z poprzedniego kroku. Można, jednak nie jest to konieczne, wrzucić tutaj istotne snippety z Waszych aplikacji.

## Dodatkowe uwagi
W tej sekcji możecie zawrzeć informacje, których nie jesteście w stanie przypisać do pozostałych. Mogą to być również jakieś komentarze, wolne uwagi, itp.
