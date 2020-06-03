-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 03 Cze 2020, 16:39
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `hurtownia2`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `cena`
--

CREATE TABLE `cena` (
  `id_cena` int(11) NOT NULL,
  `cena` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `cena`
--

INSERT INTO `cena` (`id_cena`, `cena`) VALUES
(1, 1.5),
(2, 2),
(3, 2.5),
(4, 3),
(5, 3.5),
(6, 4),
(7, 4.5),
(8, 5),
(9, 5.5),
(10, 6),
(11, 6.5),
(12, 7),
(13, 7.5),
(14, 8),
(15, 8.5),
(16, 9),
(17, 9.5),
(18, 10),
(19, 50),
(20, 70),
(21, 90.5),
(22, 100),
(23, 1000),
(24, 99.99),
(25, 80.4),
(26, 15.5),
(27, 21),
(28, 17.5),
(29, 47.5),
(30, 250),
(31, 37.5),
(32, 120),
(33, 200),
(34, 7000),
(35, 40.5),
(36, 16.5),
(37, 1),
(38, 1.99),
(39, 30),
(40, 65),
(41, 180),
(42, 150.5),
(43, 120),
(44, 350);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `faktura`
--

CREATE TABLE `faktura` (
  `id_faktura` int(11) NOT NULL,
  `wartosc` double DEFAULT NULL,
  `id_klient` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `faktura`
--

INSERT INTO `faktura` (`id_faktura`, `wartosc`, `id_klient`) VALUES
(1, 95, 1),
(2, 95, 2),
(3, 95, 1),
(4, 95, 1),
(5, 95, 1),
(6, 95, 1),
(7, 95, 1),
(8, 95, 1),
(9, 95, 1),
(10, 95, 1),
(11, 320, 1),
(14, 17.5, 3),
(15, 100, 4),
(17, 250, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `klient`
--

CREATE TABLE `klient` (
  `id_klient` int(11) NOT NULL,
  `imie` varchar(50) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `NIP` varchar(11) DEFAULT NULL,
  `k_login` varchar(50) DEFAULT NULL,
  `k_haslo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `klient`
--

INSERT INTO `klient` (`id_klient`, `imie`, `nazwisko`, `NIP`, `k_login`, `k_haslo`) VALUES
(1, 'Jan', 'Kowalski', '1234567890', 'kjan', 'kjan'),
(2, 'Andrzej', 'Nowak', '1236667890', 'kandrzej', 'kandrzej'),
(3, 'Michal', 'Serwaczak', '1231231231', 'kmichal', 'kmichal'),
(4, 'Kamil', 'Podwika', '2147483647', 'kkamil', 'kkamil'),
(5, 'Bartlomiej', 'Noga', '2147483648', 'kbartlomiej', 'kbartlomiej'),
(6, 'Robert', 'Wach', '9998887776', 'krobert', 'krobert'),
(7, 'Wacław', 'Gaska', '0980980980', 'kwaclaw', 'kwaclaw'),
(8, 'Arkadiusz', 'Nowak', '9876543210', 'karkadiusz', 'karkadiusz'),
(9, 'Izabela', 'Lecka', '8989898998', 'kizabela', 'kizabela'),
(10, 'Pawel', 'Reka', '1234561234', 'kpawel', 'kpawel'),
(13, 'Seba', 'Seba', '5469872368', 'kseba', 'kseba'),
(14, 'Marek', 'Mostowiak', '1597538462', 'kmarek', 'kmarek'),
(15, 'Aleks', 'Aleks', '4561237894', 'kaleks', 'kaleks');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownik`
--

CREATE TABLE `pracownik` (
  `id_pracownik` int(11) NOT NULL,
  `imie` varchar(50) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `pensja` int(11) NOT NULL,
  `id_stanowisko` int(11) DEFAULT NULL,
  `p_login` varchar(50) DEFAULT NULL,
  `p_haslo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pracownik`
--

INSERT INTO `pracownik` (`id_pracownik`, `imie`, `nazwisko`, `pensja`, `id_stanowisko`, `p_login`, `p_haslo`) VALUES
(1, 'Karol', 'Mickiewicz', 9000, 1, 'pkarol', 'pkarol'),
(2, 'Lidia', 'Sklodowska', 2000, 3, 'plidia', 'plidia'),
(3, 'Jan', 'Klocek', 2000, 3, 'pjan', 'pjan'),
(4, 'Mikolaj', 'Kompas', 2000, 3, 'pmikolaj', 'pmikolaj'),
(5, 'Malgorzata', 'Kochanowska', 2500, 2, 'pmalgorzata', 'pmalgorzata'),
(6, 'Ignacy', 'Slowacki', 2500, 2, 'pignacy', 'pignacy'),
(7, 'Jacek', 'Placek', 2500, 2, 'pjacek', 'pjacek'),
(8, 'Adam', 'Bak', 2500, 2, 'padam', 'padam'),
(9, 'Aleksandra', 'Wabicka', 2500, 2, 'paleksandra', 'paleksandra'),
(10, 'Teofil', 'Wybicki', 2500, 2, 'pteofil', 'pteofil'),
(11, 'Krzysztof', 'Krawczyk', 5500, 4, 'pkrzysztof', 'pkrzysztof'),
(12, 'Irena', 'Krawczyk', 5000, 4, 'pirena', 'pirena'),
(14, 'Norbert', 'Wrotek', 1750, 2, 'pnorbert', 'pnorbert');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `produkt`
--

CREATE TABLE `produkt` (
  `id_produkt` int(11) NOT NULL,
  `id_cena` int(11) DEFAULT NULL,
  `id_sekcja` int(11) DEFAULT NULL,
  `nazwa_produktu` varchar(50) NOT NULL,
  `ilosc_produktow` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `produkt`
--

INSERT INTO `produkt` (`id_produkt`, `id_cena`, `id_sekcja`, `nazwa_produktu`, `ilosc_produktow`) VALUES
(1, 3, 1, 'dlugopis', 1150),
(2, 8, 1, 'segregator', 100),
(3, 1, 1, 'olowek', 4000),
(4, 4, 1, 'gumka do mazania', 500),
(5, 26, 1, 'ryza papieru', 800),
(6, 2, 1, 'temperowka', 200),
(7, 11, 1, 'korektor', 300),
(8, 18, 1, 'pioro', 160),
(9, 28, 1, 'piornik', 280),
(10, 7, 1, 'teczka', 1500),
(11, 28, 2, 'Zubrowka', 487),
(12, 20, 2, 'Jack Daniels', 210),
(13, 19, 2, 'Johnnie Walker', 315),
(14, 36, 2, 'Zaladkowa', 400),
(15, 5, 2, 'Zubr', 2400),
(16, 31, 2, 'Finlandia', 264),
(17, 7, 2, 'Desperados', 3000),
(18, 27, 2, 'Stock', 520),
(19, 27, 2, 'Prosecco', 1200),
(20, 18, 2, 'Fresco', 1050),
(21, 27, 4, 'Koszulka', 1500),
(22, 19, 4, 'Spodnie', 460),
(24, 43, 4, 'Koszula ', 300),
(25, 20, 4, 'Sweter', 370),
(39, 2, 4, 'Skarpety', 2800),
(40, 16, 4, 'Majtki', 1500),
(41, 18, 4, 'Szalik', 297),
(42, 13, 4, 'Rekawiczki', 707),
(43, 27, 4, 'Sukienka', 890),
(44, 40, 4, 'Garnitur', 160),
(45, 31, 6, 'Jablon', 700),
(46, 25, 6, 'Tuja', 1500),
(47, 29, 6, 'Krzeslo ogrodowe', 550),
(48, 43, 6, 'Stol ogrodowy', 200),
(50, 42, 6, 'lawka ogrodowa', 260),
(51, 41, 6, 'Hustawka ogrodowa', 145),
(52, 30, 6, 'Kosiarka', 34),
(53, 3, 3, 'lizak', 2080),
(54, 6, 3, 'chipsy', 1580),
(55, 4, 3, 'chrupki', 1000),
(56, 7, 3, 'majonez', 1280),
(57, 9, 3, 'ketchup', 3000),
(58, 8, 3, 'ciastka', 1580),
(59, 7, 3, 'coca-cola', 400),
(60, 5, 3, 'napoj energetyczny', 320),
(61, 9, 3, 'musztarda', 1500),
(63, 26, 5, 'Heetsy mietowe', 2000),
(64, 26, 5, 'Heetsy limonkowe', 1406),
(65, 26, 5, 'Heetsy mentolowe', 1800),
(66, 28, 5, 'LM mentolowe', 1800),
(67, 27, 5, 'Malboro gold', 780),
(68, 27, 5, 'Malboro zielone', 420),
(69, 31, 5, 'Sobranie', 250),
(70, 34, 6, 'Jacuzzi', 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sekcja`
--

CREATE TABLE `sekcja` (
  `id_sekcja` int(11) NOT NULL,
  `sekcja` varchar(50) NOT NULL,
  `sektor_hurtowni` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `sekcja`
--

INSERT INTO `sekcja` (`id_sekcja`, `sekcja`, `sektor_hurtowni`) VALUES
(1, 'Papiernicza', 'Pierwsza alejka'),
(2, 'Alkoholowa', 'Druga alejka'),
(3, 'Spozywcza', 'Trzecia alejka'),
(4, 'Odziezowa', 'Czwarta alejka'),
(5, 'Wyroby tytoniowe', 'Piąta alejka'),
(6, 'Ogrodnicza', 'Szósta alejka');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `stanowisko`
--

CREATE TABLE `stanowisko` (
  `id_stanowisko` int(11) NOT NULL,
  `stanowisko` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `stanowisko`
--

INSERT INTO `stanowisko` (`id_stanowisko`, `stanowisko`) VALUES
(1, 'Prezes'),
(2, 'Magazynier'),
(3, 'Kasjer'),
(4, 'Kierownik');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zamowienie`
--

CREATE TABLE `zamowienie` (
  `id_zamowienie` int(11) NOT NULL,
  `id_produkt` int(11) DEFAULT NULL,
  `data_zamowienia` date NOT NULL,
  `id_pracownik` int(11) DEFAULT NULL,
  `ilosc` int(11) NOT NULL,
  `id_faktura` int(11) DEFAULT NULL,
  `klogin` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `zamowienie`
--

INSERT INTO `zamowienie` (`id_zamowienie`, `id_produkt`, `data_zamowienia`, `id_pracownik`, `ilosc`, `id_faktura`, `klogin`) VALUES
(1, 4, '2020-05-10', 7, 1, 1, 'kjan'),
(2, 5, '2020-05-17', 7, 2, 3, 'kjan'),
(3, 70, '2020-05-21', 7, 1, 4, 'kjan'),
(4, 70, '2020-05-21', 7, 1, 5, 'kjan'),
(5, 70, '2020-06-22', 7, 2, 6, 'kjan'),
(6, 1, '2020-05-25', 7, 500, 7, 'kjan'),
(10, 70, '2020-05-26', 7, 1, 8, 'kjan'),
(11, 1, '2020-05-26', 7, 500, 8, 'kjan'),
(12, 1, '2020-05-30', 11, 10, 9, 'kjan'),
(13, 11, '2020-05-30', 11, 4, 9, 'kjan'),
(15, 1, '2020-05-30', 11, 10, 10, 'kjan'),
(16, 11, '2020-05-30', 11, 4, 10, 'kjan'),
(17, 1, '2020-05-30', 11, 100, 11, 'kjan'),
(18, 11, '2020-05-30', 11, 4, 11, 'kjan'),
(21, 11, '2020-05-31', 11, 1, 14, 'kmichal'),
(23, 16, '2020-05-31', 11, 2, 15, 'kkamil'),
(24, 1, '2020-05-31', 11, 10, 15, 'kkamil'),
(25, 1, '2020-05-31', 11, 100, 17, 'kjan');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `cena`
--
ALTER TABLE `cena`
  ADD PRIMARY KEY (`id_cena`);

--
-- Indeksy dla tabeli `faktura`
--
ALTER TABLE `faktura`
  ADD PRIMARY KEY (`id_faktura`),
  ADD KEY `id_klient` (`id_klient`);

--
-- Indeksy dla tabeli `klient`
--
ALTER TABLE `klient`
  ADD PRIMARY KEY (`id_klient`);

--
-- Indeksy dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  ADD PRIMARY KEY (`id_pracownik`),
  ADD KEY `id_stanowisko` (`id_stanowisko`);

--
-- Indeksy dla tabeli `produkt`
--
ALTER TABLE `produkt`
  ADD PRIMARY KEY (`id_produkt`),
  ADD KEY `id_cena` (`id_cena`),
  ADD KEY `id_sekcja` (`id_sekcja`);

--
-- Indeksy dla tabeli `sekcja`
--
ALTER TABLE `sekcja`
  ADD PRIMARY KEY (`id_sekcja`);

--
-- Indeksy dla tabeli `stanowisko`
--
ALTER TABLE `stanowisko`
  ADD PRIMARY KEY (`id_stanowisko`);

--
-- Indeksy dla tabeli `zamowienie`
--
ALTER TABLE `zamowienie`
  ADD PRIMARY KEY (`id_zamowienie`),
  ADD KEY `id_faktura` (`id_faktura`),
  ADD KEY `id_produkt` (`id_produkt`),
  ADD KEY `id_pracownik` (`id_pracownik`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `cena`
--
ALTER TABLE `cena`
  MODIFY `id_cena` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT dla tabeli `faktura`
--
ALTER TABLE `faktura`
  MODIFY `id_faktura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT dla tabeli `klient`
--
ALTER TABLE `klient`
  MODIFY `id_klient` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  MODIFY `id_pracownik` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT dla tabeli `produkt`
--
ALTER TABLE `produkt`
  MODIFY `id_produkt` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT dla tabeli `sekcja`
--
ALTER TABLE `sekcja`
  MODIFY `id_sekcja` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT dla tabeli `stanowisko`
--
ALTER TABLE `stanowisko`
  MODIFY `id_stanowisko` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT dla tabeli `zamowienie`
--
ALTER TABLE `zamowienie`
  MODIFY `id_zamowienie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `faktura`
--
ALTER TABLE `faktura`
  ADD CONSTRAINT `faktura_ibfk_1` FOREIGN KEY (`id_klient`) REFERENCES `klient` (`id_klient`);

--
-- Ograniczenia dla tabeli `pracownik`
--
ALTER TABLE `pracownik`
  ADD CONSTRAINT `pracownik_ibfk_1` FOREIGN KEY (`id_stanowisko`) REFERENCES `stanowisko` (`id_stanowisko`);

--
-- Ograniczenia dla tabeli `produkt`
--
ALTER TABLE `produkt`
  ADD CONSTRAINT `produkt_ibfk_1` FOREIGN KEY (`id_cena`) REFERENCES `cena` (`id_cena`),
  ADD CONSTRAINT `produkt_ibfk_2` FOREIGN KEY (`id_sekcja`) REFERENCES `sekcja` (`id_sekcja`);

--
-- Ograniczenia dla tabeli `zamowienie`
--
ALTER TABLE `zamowienie`
  ADD CONSTRAINT `zamowienie_ibfk_1` FOREIGN KEY (`id_faktura`) REFERENCES `faktura` (`id_faktura`),
  ADD CONSTRAINT `zamowienie_ibfk_2` FOREIGN KEY (`id_produkt`) REFERENCES `produkt` (`id_produkt`),
  ADD CONSTRAINT `zamowienie_ibfk_3` FOREIGN KEY (`id_pracownik`) REFERENCES `pracownik` (`id_pracownik`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
