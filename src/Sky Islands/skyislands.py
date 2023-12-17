import sys
file = sys.stdin.read()
liste = file.splitlines()

n, m = liste[0].split()
n, m = int(n), int(m)

rliste = []
for j in range(1, m + 1):
    p1, p2 = liste[j].split()
    rliste.append([int(p1), int(p2)])
    j += 1

"""Recherche des parties connexes"""

parties_connexes = []
for r in rliste:
    """Pour chaque relation, on fusionne les parties connexes de chaque point.
       Pour deux points sans parties, on créer une nouvelle partie."""
    long = len(parties_connexes)
    p1, p2 = r
    i1, i2 = -1, -1
    for i in range(long):
        if p1 in parties_connexes[i]:
            i1 = i
        if p2 in parties_connexes[i]:
            i2 = i
    if i1 == -1 and i2 == -1:
        parties_connexes.append([p1, p2]) #créer une nouvelle partie connexe
    elif i1 == -1:
        parties_connexes[i2].append(p1) #ajoute p1 à la partie de p2
    elif i2 == -1:
        parties_connexes[i1].append(p2) #ajoute p2 à la partie de p1
    elif i1 != i2:
        parties_connexes[i1] += parties_connexes[i2] #fusionne les parties de p1 et p2
        del(parties_connexes[i2])

"""Conclusion"""

if n == 1:
    print("YES") # Un seul point
elif m == 0:
    print("NO") # Au moins deux points mais pas de ponts
elif len(parties_connexes) == 1 and len(parties_connexes[0]) == n:
    print("YES") # Une seule partie connexe, de taille n
else:
    print("NO") # Plusieurs parties