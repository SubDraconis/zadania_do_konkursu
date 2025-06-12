N = int(input())

zdarzenia = []
for _ in range(N):
    p, w = map(int, input().split())
    zdarzenia.append((p,1))
    zdarzenia.append((w,-1))

zdarzenia.sort(key=lambda x: (x[0] -x[1]))

aktualni = 0
suma = 0
for czas, typ in zdarzenia:
    aktualni += typ
    suma = max(suma, aktualni)

print(suma)