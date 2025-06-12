# Zadania Algorytmiczne - Przygotowanie do OIJ

## Autor
Maciej Kubiczek

## Opis
Ten plik zawiera zbiór zadań algorytmicznych, stworzonych w celu przygotowania do Olimpiady Informatycznej Juniorów (OIJ). Zadania skupiają się na efektywności, algorytmice i rozwiązywaniu problemów. W folderze rozwiązania są moje rozwiązania

**Struktura Zadań:**

Każde zadanie będzie zawierać następujące sekcje:

*   **Nazwa:** Krótka, opisowa nazwa zadania.
*   **Poziom Trudności:** Określenie trudności zadania (np. Wprowadzający, Łatwy, Średni, Trudny).
*   **Treść Zadania:** Szczegółowy opis problemu do rozwiązania.
*   **Format Wejścia:** Opis formatu danych, które program powinien odczytać.
*   **Format Wyjścia:** Opis formatu danych, które program powinien wypisać.
*   **Ograniczenia:** Limity czasowe i pamięciowe, które program musi spełnić.
*   **Przykłady:** Przykładowe dane wejściowe i odpowiadające im dane wyjściowe.

**Cel:**

Celem tego zbioru zadań jest rozwinięcie umiejętności:

*   Analizy problemów i znajdowania efektywnych algorytmów.
*   Implementacji algorytmów w języku Python.
*   Optymalizacji kodu pod kątem czasu i pamięci.
*   Testowania i debugowania rozwiązań.

**Jak korzystać z tego pliku:**

1.  Wybierz zadanie o odpowiednim poziomie trudności.
2.  Przeczytaj uważnie treść zadania, format wejścia i wyjścia oraz ograniczenia.
3.  Spróbuj rozwiązać zadanie samodzielnie.
4.  Przetestuj swoje rozwiązanie na przykładach podanych w zadaniu oraz na własnych testach.
5.  Jeśli masz problemy, poszukaj wskazówek w Internecie lub skonsultuj się z bardziej doświadczonym programistą.

Powodzenia w rozwiązywaniu zadań!


## łatwe

Jasne, przepraszam za pomyłkę. Oto treść zadania w całości po polsku, sformatowana w stylu `README.md`. Możesz skopiować cały poniższy blok.

```markdown
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
```
5
1 5
8 10
3 9
6 7
2 4
```

**Wyjście:**
```
3
```

**Wyjaśnienie przykładu:**

* W chwili 1: jest 1 gość
* W chwili 2: są 2 gości
* W chwili 3: są 3 gości
* W chwili 4: wychodzi gość [2,4], pozostają 2 gości
* W chwili 5: wychodzi gość [1,5], pozostaje 1 gość
* W chwili 6: przychodzi gość [6,7], są 2 gości
* Itd. Maksymalna liczba gości w jednym momencie to 3.

---

> ### **Wskazówka (jeśli potrzebujesz):**
>
> Pomyśl o każdym przyjściu i wyjściu jako o osobnym "zdarzeniu". Każde przyjście zwiększa liczbę gości o 1, a każde wyjście ją zmniejsza. Co by było, gdybyś posortował wszystkie te zdarzenia (zarówno przyjścia, jak i wyjścia) chronologicznie? Jak wtedy mógłbyś śledzić liczbę obecnych osób?
```