N = int(input())

zdarzenia = []

for _ in range(N):
    poczatek, koniec = map(int, input().split())
    zdarzenia.append((poczatek, 1))   # początek malowania
    zdarzenia.append((koniec, -1))    # koniec malowania

zdarzenia.sort()

aktywni = 0
ostatni = 0
suma_pomalowana = 0

for pozycja, typ in zdarzenia:
    if aktywni > 0:
        suma_pomalowana += pozycja - ostatni
    aktywni += typ
    ostatni = pozycja

print(suma_pomalowana)