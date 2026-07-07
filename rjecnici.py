"""
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1
"""

import random
imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel",
        "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", 
        "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica",
        "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante",
         "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara",
        "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", 
        "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

studenti = {}
ocjene = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for ime in imena:
    ocjena = random.randint(1, 5)
    studenti[ime] = ocjena
    ocjene[ocjena] += 1

print("Ocjene studenata:")
for ime, ocjena in studenti.items():
    print(ime, "-", ocjena)

print("\nBroj pojedinih ocjena:")
for ocjena, broj in ocjene.items():
    print("Ocjena", ocjena, ":", broj)

prolazni = 0

for ocjena in studenti.values():
    if ocjena > 1:
        prolazni += 1

postotak_prolaznosti = prolazni / len(studenti) * 100

print("\nPostotak prolaznosti:", round(postotak_prolaznosti, 2), "%")