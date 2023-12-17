import sys

file = sys.stdin.read()
liste = file.splitlines()
m = []
for i in range(1, len(liste)):
    x, y = liste[i].split()
    a = float(int(y) - int(x))
    m.append(a)

print(sum(m)/len(m))