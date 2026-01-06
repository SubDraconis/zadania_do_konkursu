# Zadanie 4: Sortowanie Wyników

## Treść Zadania

Otrzymujesz listę wyników uczestników pewnego konkursu. Każdy wynik składa się z imienia uczestnika oraz liczby zdobytych przez niego punktów. Twoim zadaniem jest stworzyć ranking uczestników.

Ranking powinien być posortowany w następujący sposób:
1.  Malejąco według liczby punktów.
2.  Jeśli dwóch lub więcej uczestników ma tę samą liczbę punktów, powinni oni być posortowani alfabetycznie (rosnąco) według swoich imion.

## Format Wejścia

*   W pierwszej linii znajduje się jedna liczba całkowita `n`, oznaczająca liczbę uczestników.
*   W kolejnych `n` liniach znajduje się imię uczestnika (ciąg znaków) oraz jego wynik (liczba całkowita), oddzielone spacją.

## Format Wyjścia

*   Na wyjściu należy wypisać `n` linii.
*   Każda linia powinna zawierać imię i wynik uczestnika, zgodnie z zasadami sortowania opisanymi w treści zadania.

## Ograniczenia

*   `1 <= n <= 100 000`
*   Imiona składają się z wielkich liter alfabetu angielskiego (`A-Z`) i mają długość od 1 do 20 znaków.
*   Wyniki są liczbami całkowitymi z przedziału `[0, 1000]`.
*   Limit czasu: 1 sekunda
*   Limit pamięci: 256 MB

## Przykłady

### Przykład 1

**Wejście:**
```
5
ALA 100
JAN 90
OLA 100
EWA 95
TOMEK 90
```

**Wyjście:**
```
ALA 100
OLA 100
EWA 95
JAN 90
TOMEK 90
```

