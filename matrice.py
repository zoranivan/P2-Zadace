"""
Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice.
"""
import random

velicina = 7
polje = []
ukupno = 0

for red in range(velicina):
    lista = []
    for stupac in range(velicina):
        vrijednost = random.randint(1,9)
        lista.append(vrijednost)
    polje.append(lista)

print("matrica:")
for lista in polje:
    print(*lista)
for red in range(velicina):
    for stupac in range(velicina):
        if red == 0 or red == velicina -1 or stupac == 0 or stupac == velicina -1:
            ukupno += polje[red][stupac]

print("\nZbroj elemenata na rubovima:", ukupno)