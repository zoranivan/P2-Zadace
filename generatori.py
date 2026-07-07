"""
Napraviti generator funkcije za
ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
"""

def parni(n):
    brojac = 0
    while True:
        if brojac % 2 == 0:
            yield brojac
        brojac += 1
        if brojac >= n:
            break

def neparni(n):
    vrijednost = 0
    while True:
        if vrijednost % 2 != 0:
            yield vrijednost
        vrijednost += 1
        if vrijednost >= n:
            break

generator_parni = parni(20)
generator_neparni = neparni(20)

for element in generator_parni:
    print(element)

for element in generator_neparni:
    print(element)