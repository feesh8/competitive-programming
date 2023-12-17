import sys

ent = sys.stdin.read()
liste = ent.splitlines()


N, M = liste[0].split()
N, M = int(N), int(M)
if N == 2 and M == 1:
    print("1\n1")
    exit(0)
no = M - N
train = dict()
for i in range(1, len(liste)):
    a, b = liste[i].split()
    a, b = int(a), int(b)
    if a > b:
        b, a = a, b
    
    if a + 1 == b:
        train[a] = i
    elif a == 1 and b == N:
        train[b] = i
    else:
        no -= 1

if no >= 0:
    for elt in train:
        print(elt)
else:
    print("impossible")