# Zadanie 4: Robot

### Poziom trudności: Łatwy

---

## Wprowadzenie

Na nieskończonej, dwuwymiarowej planszy w kratkę, w punkcie startowym (0, 0) znajduje się prosty robot. Robot potrafi rozumieć tylko cztery komendy, które poruszają go o jedną kratkę w danym kierunku:
* `G` - ruch w górę (zwiększa współrzędną Y o 1)
* `D` - ruch w dół (zmniejsza współrzędną Y o 1)
* `P` - ruch w prawo (zwiększa współrzędną X o 1)
* `L` - ruch w lewo (zmniejsza współrzędną X o 1)

Otrzymałeś długi ciąg komend dla tego robota.

## Treść zadania

Napisz program, który obliczy i wypisze końcową pozycję robota (jego współrzędne X i Y) po wykonaniu wszystkich komend z otrzymanego ciągu.

---

## Format Wejścia

* W jedynej linii wejścia znajduje się ciąg znaków **`S`**, składający się wyłącznie z liter `G`, `D`, `P`, `L`. Długość ciągu `S` nie przekracza 1 000 000.

## Format Wyjścia

* Program powinien wypisać na standardowe wyjście dwie liczby całkowite, oddzielone pojedynczą spacją: końcową współrzędną X oraz końcową współrzędną Y robota.

## Ograniczenia

* **Limit czasu:** 1 sekunda
* **Limit pamięci:** 256 MB

---
## Przykład

**Wejście:**

GGPPLDG

**Wyjście:**

1 2

**Wyjaśnienie przykładu:**
Robot wykonuje następujące ruchy:
1.  Startuje w `(0, 0)`
2.  `G` -> pozycja `(0, 1)`
3.  `G` -> pozycja `(0, 2)`
4.  `P` -> pozycja `(1, 2)`
5.  `P` -> pozycja `(2, 2)`
6.  `L` -> pozycja `(1, 2)`
7.  `D` -> pozycja `(1, 1)`
8.  `G` -> pozycja `(1, 2)`

Ostateczna pozycja robota to (1, 2).