import sys

dominant = dict([('A', 11), ('K', 4), ('Q', 3), ('J', 20), ('T', 10), ('9', 14), ('8', 0), ('7', 0)])
notdom = dict([('A', 11), ('K', 4), ('Q', 3), ('J', 2), ('T', 10), ('9', 0), ('8', 0), ('7', 0)])

ent  = sys.stdin.read()
liste = ent.splitlines()
N, B = liste[0].split()
res = 0
for i in range(1, len(liste)):
    val = liste[i][0]
    color = liste[i][1]
    if color == B:
        res += dominant[val]
    else:
        res += notdom[val]

print(res)