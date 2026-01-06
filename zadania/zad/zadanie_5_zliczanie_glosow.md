# Zadanie 5: Zliczanie Głosów

## Treść Zadania

Właśnie zakończyły się wybory na przewodniczącego szkoły. Otrzymujesz listę wszystkich oddanych głosów. Każdy głos to imię jednego z kandydatów. Twoim zadaniem jest policzenie, ile głosów zdobył każdy z kandydatów, i przedstawienie ostatecznych wyników.

Wyniki powinny być posortowane alfabetycznie według imion kandydatów.

## Format Wejścia

*   W pierwszej linii znajduje się jedna liczba całkowita `n`, oznaczająca łączną liczbę oddanych głosów.
*   W kolejnych `n` liniach znajduje się imię kandydata, na którego oddano głos.

## Format Wyjścia

*   Na wyjściu należy wypisać listę kandydatów wraz z liczbą zdobytych przez nich głosów.
*   Każda linia powinna zawierać imię kandydata i jego wynik, oddzielone spacją.
*   Lista powinna być posortowana alfabetycznie (rosnąco) według imion kandydatów.

## Ograniczenia

*   `1 <= n <= 200 000`
*   Imiona składają się z wielkich liter alfabetu angielskiego (`A-Z`) i mają długość od 1 do 30 znaków.
*   Limit czasu: 1 sekunda
*   Limit pamięci: 256 MB

## Przykłady

### Przykład 1

**Wejście:**
```
7
ANNA
JAN
ANNA
PIOTR
JAN
ANNA
TOMEK
```

**Wyjście:**
```
ANNA 3
JAN 2
PIOTR 1
TOMEK 1
```