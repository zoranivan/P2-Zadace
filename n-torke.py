polaznici = [
    ("Ivano", "Ahmedovski", 85),
    ("Ana", "Anić", 45),
    ("Marko", "Marić", 72),
    ("Sara", "Šakić", 91),
    ("Luka", "Lukić", 55),
    ("Maja", "Majić", 38),
    ("Petar", "Petrić", 68),
    ("Nina", "Ninić", 95),
    ("Ante", "Antić", 80),
    ("Iva", "Ivić", 50),
    ("Martina", "Martinović", 50),
    ("Stjepan", "Šarić", 100)
]

polaznici = sorted(polaznici, key=lambda x: x[1])

print("Sortirano po prezimenima:")
print("")

for zapis in polaznici:
    print(zapis[0], zapis[1], zapis[2])

print("")
print("")

kategorije = {}
kategorije["Nedovoljan"] = 0
kategorije["Dovoljan"] = 0
kategorije["Dobar"] = 0
kategorije["Vrlodobar"] = 0
kategorije["Izvrstan"] = 0

for zapis in polaznici:
    bodovi = zapis[2]
    if bodovi < 50:
        kategorije["Nedovoljan"] += 1
    elif bodovi < 65:
        kategorije["Dovoljan"] += 1
    elif bodovi < 80:
        kategorije["Dobar"] += 1
    elif bodovi < 90:
        kategorije["Vrlodobar"] += 1
    else:
        kategorije["Izvrstan"] += 1

print("Bodovni rang:")
print("")

for naziv in kategorije:
    print(naziv, ":", kategorije[naziv], "studenata")

print("")
print("")