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

## Implementacja zapytań SQL
Tutaj należy wylistować wszystkie funkcjonalności, wraz z odpowiednimi zapytaniami SQL. W tej sekcji należy zawrzeć wyłącznie zapytania z grupy DML oraz DQL.
1. Wypisanie wszystkich produktów i posortowanie ich względem ceny malejąco
 ```sql
    SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;
```

## Aplikacja
Tutaj należy opisać aplikację, która wykorzystuje zapytania SQL z poprzedniego kroku. Można, jednak nie jest to konieczne, wrzucić tutaj istotne snippety z Waszych aplikacji.

## Dodatkowe uwagi
W tej sekcji możecie zawrzeć informacje, których nie jesteście w stanie przypisać do pozostałych. Mogą to być również jakieś komentarze, wolne uwagi, itp.
