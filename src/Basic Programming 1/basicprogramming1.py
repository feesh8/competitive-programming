import statistics
import sys
import string

ent = sys.stdin.read()
liste = ent.splitlines()
n, t = liste[0].split()
n = int(n)
t = int(t)
Nlist = liste[1].split()
Nliste = []
for elt in Nlist:
    Nliste.append(int(elt))
if t == 1:
    print(7)
elif t == 2:
    if Nliste[0] > Nliste[1]:
        print("Bigger")
    elif Nliste[0] == Nliste[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    print(statistics.median([Nliste[0], Nliste[1], Nliste[2]]))
elif t == 4:
    print(sum(Nliste))
elif t == 5:
    somme = 0
    for elt in Nliste:
        if elt % 2 == 0:
            somme += elt
    print(somme)
elif t == 6:
    corres = dict(enumerate(string.ascii_lowercase, 0))
    for elt in Nliste:
        print(corres[elt % 26], end="")
else:
    count = 0
    i = 0
    msg = "Cyclic"
    while count < n:
        i = Nliste[i]
        if i < 0 or i > n - 1:
            msg = "Out"
            count = n + 1
        elif i == n - 1:
            msg = "Done"
            count = n + 1
        else:
            count += 1
    print(msg)