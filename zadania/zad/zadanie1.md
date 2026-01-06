# Zadanie 1: Maksymalna Liczba Gości

### Poziom trudności: Wprowadzający

---

## Wprowadzenie

Organizujesz dużą imprezę. Otrzymałeś od każdego z zaproszonych gości informację, o której godzinie przyjdzie i o której godzinie zamierza wyjść. Chciałbyś wiedzieć, ile maksymalnie osób będzie przebywało na imprezie w tym samym momencie, aby upewnić się, że masz wystarczająco dużo przekąsek!

## Treść zadania

Napisz program, który na podstawie czasów przyjścia i wyjścia gości obliczy największą liczbę osób, która w dowolnym momencie znajdowała się na imprezie. Możemy założyć, że jeśli jeden gość wychodzi w tej samej chwili, w której drugi przychodzi, to przez moment są na imprezie razem.

---

## Format Wejścia

* W pierwszej linii wejścia znajduje się jedna liczba całkowita **`N`** (1 ≤ N ≤ 200 000), oznaczająca liczbę zaproszonych gości.
* W kolejnych **`N`** liniach znajduje się po dwie liczby całkowite **`p_i`** oraz **`w_i`** (1 ≤ p_i < w_i ≤ 1 000 000 000), oznaczające odpowiednio czas przyjścia i czas wyjścia i-tego gościa.

## Format Wyjścia

* Program powinien wypisać na standardowe wyjście jedną liczbę całkowitą – maksymalną liczbę gości obecnych na imprezie w tym samym czasie.

## Ograniczenia

* **Limit czasu:** 1 sekunda
* **Limit pamięci:** 256 MB

---

## Przykład

**Wejście:**
5
1 5
8 10
3 9
6 7
2 4


**Wyjście:**
3


**Wyjaśnienie przykładu:**

* W chwili 1: jest 1 gość
* W chwili 2: są 2 gości
* W chwili 3: są 3 gości
* W chwili 4: wychodzi gość [2,4], pozostają 2 gości
* W chwili 5: wychodzi gość [1,5], pozostaje 1 gość
* W chwili 6: przychodzi gość [6,7], są 2 gości
* Itd. Maksymalna liczba gości w jednym momencie to 3.

---

**Wskazówka (jeśli potrzebujesz):**

Pomyśl o każdym przyjściu i wyjściu jako o osobnym "zdarzeniu". Każde przyjście zwiększa liczbę gości o 1, a każde wyjście ją zmniejsza. Co by było, gdybyś posortował wszystkie te zdarzenia (zarówno przyjścia, jak i wyjścia) chronologicznie? Jak wtedy mógłbyś śledzić liczbę obecnych osób?