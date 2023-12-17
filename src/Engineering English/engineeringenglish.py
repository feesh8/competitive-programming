import sys

ent = sys.stdin.read()
texte = ent.splitlines()
liste = []
texte2 = ""
for ligne in texte:
    ligne = ligne.split()
    for elt in ligne:
        if elt.lower() not in liste:
            liste.append(elt.lower())
            texte2 += elt
            texte2 += " "
        else:
            elt = ". "
            texte2 += elt
print(texte2)