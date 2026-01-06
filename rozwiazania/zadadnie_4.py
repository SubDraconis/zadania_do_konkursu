dl = int(input())
# Lepiej od razu przekonwertować dane na właściwe typy
osoby = []
for _ in range(dl):
    imie, punkty_str = input().split()
    osoby.append((imie, int(punkty_str)))

# Sortowanie:
# 1. Malejąco według punktów (dlatego -x[1])
# 2. Rosnąco (alfabetycznie) według imienia (dlatego x[0])
osoby.sort(key=lambda x: (-x[1], x[0]))

for osoba in osoby:
    # Wypisanie w wymaganym formacie "IMIE PUNKTY"
    print(osoba[0], osoba[1])