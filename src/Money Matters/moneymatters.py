import sys
file = sys.stdin.read()
liste = file.splitlines()

n, m = liste[0].split()
n, m = int(n), int(m)

pliste = [int(liste[i]) for i in range(1, n + 1)]
rliste = []
j = n + 1
while j < m + n + 1:
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

"""Il reste les points isolés, sans relations"""

for p in range(n):
    vu = False
    for partie in parties_connexes:
        if p in partie:
            vu = True
    if not vu:
        parties_connexes.append([p])

"""Conclusion"""

possible = True
for partie in parties_connexes:
    s = 0
    for p in partie:
        s += pliste[p]
    if s != 0:
        possible = False
        break

if possible:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")