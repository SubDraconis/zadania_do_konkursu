nawiasy_str = input()

# Stos do przechowywania otwierających nawiasów.
# W Pythonie zwykła lista może działać jak stos.
stos = []

# Słownik do łatwego sprawdzania, czy nawiasy tworzą parę.
pary = {
    '(': ')',
    '[': ']',
    '{': '}'
}

for znak in nawiasy_str:
    # Jeśli znak jest nawiasem otwierającym, dodaj go na stos.
    if znak in pary:
        stos.append(znak)
    # Jeśli znak jest nawiasem zamykającym...
    else:
        # Sprawdź, czy stos jest pusty (nie ma czego zamknąć) LUB
        # czy nawias na szczycie stosu nie pasuje do obecnego nawiasu zamykającego.
        # stos[-1] to ostatni element na liście (szczyt stosu).
        if not stos or pary[stos[-1]] != znak:
            # Jeśli któryś warunek jest spełniony, ciąg jest niepoprawny.
            print("NIE")
            exit() # Kończymy program, bo już znamy odpowiedź.
        else:
            # Jeśli nawiasy pasują, zdejmujemy otwierający nawias ze stosu.
            stos.pop()

# Po przejściu pętli, jeśli stos jest pusty, wszystko się zgadza.
if not stos:
    print("TAK")
else: # Jeśli na stosie coś zostało, to znaczy, że nie wszystkie nawiasy zostały zamknięte.
    print("NIE")
