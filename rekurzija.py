"""
Napisati rekurzivnu funkciju koja
kao parametar prima string, a kao rezultat taj string ispisuje sa zada.

"""

def obrni(tekst):
    if len(tekst) == 0:
        return ""
    else:
        return obrni(tekst[1:]) + tekst[0]

rijec = input("Unesi rijec: ")
ispis = obrni(rijec)
print(ispis)