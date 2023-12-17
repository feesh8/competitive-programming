import sys

file = sys.stdin.read()
ent = file.splitlines()

liste = ent[0].split("-")
ch = liste[0] + liste[1]
l = []
for elt in ch:
    l.append(int(elt))

val = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

last = [] 

for i in range(10):
    last.append(val[i] * l[i])
    
if sum(last) % 11 == 0:
    print("1")
else:
    print("0")