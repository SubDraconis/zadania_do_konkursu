# Zadanie 6: Poprawne Nawiasowanie

## Treść Zadania

Otrzymujesz ciąg znaków składający się wyłącznie z nawiasów: `( )`, `[ ]` oraz `{ }`. Twoim zadaniem jest sprawdzenie, czy nawiasy w tym ciągu są poprawnie zagnieżdżone i zamknięte.

Poprawny ciąg nawiasów musi spełniać dwa warunki:
1.  Każdy otwierający nawias musi mieć odpowiadający mu zamykający nawias tego samego typu.
2.  Nawiasy muszą być zamykane w odpowiedniej kolejności. Na przykład, `([)]` jest niepoprawne, ponieważ nawias kwadratowy został zamknięty przed okrągłym, który został otwarty wewnątrz niego.

## Format Wejścia

*   W jedynej linii wejścia znajduje się ciąg znaków składający się z nawiasów.

## Format Wyjścia

*   Na wyjściu należy wypisać jedno słowo: `TAK`, jeśli ciąg nawiasów jest poprawny, lub `NIE` w przeciwnym wypadku.

## Ograniczenia

*   Długość ciągu znaków `n` spełnia `1 <= n <= 1 000 000`.
*   Ciąg zawiera wyłącznie znaki: `(`, `)`, `[`, `]`, `{`, `}`.
*   Limit czasu: 1 sekunda
*   Limit pamięci: 256 MB

## Przykłady

### Przykład 1

**Wejście:**
```
()[]{}
```

**Wyjście:**
```
TAK
```

### Przykład 2

**Wejście:**
```
([{}])
```

**Wyjście:**
```
TAK
```

### Przykład 3

**Wejście:**
```
([)]
```

**Wyjście:**
```
NIE
```

### Przykład 4

**Wejście:**
```
((
```

**Wyjście:**
```
NIE
```
