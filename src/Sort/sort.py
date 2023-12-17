import sys

ent = sys.stdin.read()
liste = ent.splitlines()
a, c = liste[0].split()
a = int(a)
c = int(c)
liste2 = liste[1].split()
vu = []
nb = []
for i in range(a):
    if liste2[i] not in vu:
        vu.append(liste2[i])
        c = liste2.count(liste2[i])
        nb.append(c)

for _ in range(len(vu)):
    maximum = max(nb)
    ind = nb.index(maximum)
    for _ in range(maximum):
        print(int(vu[ind]), end=" ")
    nb.remove(maximum)
    vu.remove(vu[ind])