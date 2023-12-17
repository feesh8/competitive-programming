import sys

file = sys.stdin.read()
liste = file.splitlines()
s = sorted(list(map(int, liste[0].split())))

dico = dict([('A', s[0]), ('B', s[1]), ('C', s[2])])

for c in liste[1]:
    print(dico[c], end=" ")