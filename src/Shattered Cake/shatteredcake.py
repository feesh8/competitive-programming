import sys

file = sys.stdin.read()
liste = file.splitlines()

W = int(liste[0])
N = int(liste[1])
area = []
for i in range(2, N + 2):
    w, l = liste[i].split()
    area.append(int(w) * int(l))

print(sum(area) // W)