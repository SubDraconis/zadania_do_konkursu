# Zadanie 3: Płot Malarzy

### Poziom trudności: Łatwy

---

## Wprowadzenie

Wzdłuż drogi stoi bardzo długi, drewniany płot, który można opisać jako oś liczbową. Zatrudniono kilku malarzy do jego odnowienia. Każdy z malarzy otrzymał polecenie, aby pomalować konkretny fragment płotu, na przykład "od metra 2 do metra 6". Niestety, malarze nie dogadali się między sobą i niektóre z ich fragmentów nachodzą na siebie. Chcemy obliczyć, jaka jest całkowita długość płotu, która zostanie pomalowana przynajmniej raz.

## Treść zadania

Napisz program, który na podstawie `N` przedziałów malowania `[początek, koniec]` obliczy sumaryczną długość pomalowanych fragmentów płotu. Jeśli kilka przedziałów nachodzi na siebie, ich wspólna część powinna być policzona tylko raz.

---

## Format Wejścia

* W pierwszej linii wejścia znajduje się jedna liczba całkowita **`N`** (1 ≤ N ≤ 200 000), oznaczająca liczbę malarzy (i jednocześnie liczbę przedziałów do pomalowania).
* W kolejnych **`N`** liniach znajduje się po dwie liczby całkowite **`a_i`** oraz **`b_i`** (1 ≤ a_i < b_i ≤ 1 000 000 000), oznaczające odpowiednio początek i koniec fragmentu płotu malowanego przez i-tego malarza.

## Format Wyjścia

* Program powinien wypisać na standardowe wyjście jedną liczbę całkowitą – całkowitą długość płotu, która zostanie pomalowana przynajmniej jeden raz.

## Ograniczenia

* **Limit czasu:** 1 sekunda
* **Limit pamięci:** 256 MB

---
## Przykład

**Wejście:**
```
3
2 6
8 10
5 9
```

**Wyjście:**
```
8
```

**Wyjaśnienie przykładu:**
* Pierwszy malarz maluje odcinek [2, 6].
* Drugi malarz maluje odcinek [8, 10].
* Trzeci malarz maluje odcinek [5, 9].

Łącząc te odcinki, otrzymujemy jeden ciągły pomalowany fragment od metra 2 do metra 10. Długość tego fragmentu to 10 - 2 = 8. Zauważ, że fragment [5, 6] był malowany przez dwóch malarzy, a fragment [8, 9] również, ale nie liczymy tych części podwójnie.

---

**Wskazówka (jeśli potrzebujesz):**

> Tak jak w zadaniu z gośćmi, potraktuj początek `a_i` i koniec `b_i` każdego malowania jako osobne "zdarzenia". Początek malowania można oznaczyć jako `+1`, a koniec jako `-1`. Posortuj wszystkie zdarzenia po ich współrzędnej. Przechodź przez posortowane zdarzenia, utrzymując licznik "aktywnych" malarzy. Kiedy ten licznik zmienia się z 0 na 1? Kiedy zmienia się z 1 na 0? Jak te momenty i ich współrzędne mogą pomóc Ci obliczyć całkowitą pomalowaną długość?
```