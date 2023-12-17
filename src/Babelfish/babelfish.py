import sys

ent = sys.stdin.read()
liste = ent.splitlines()
i = liste.index("")
dico = liste[0:i]
a_traduire = liste[i + 1:]
for i in range(len(dico)):
    mot, trad = dico[i].split()
    dico[i] = trad, mot
dico = dict(dico)

for elt in a_traduire:
    if elt in dico:
        print(dico.get(elt))
    else:
        print("eh")