import sys

ent = sys.stdin.read()

liste = ent.splitlines()

c = 0

for i in range(1, len(liste)):
    s = liste[i].lower()
    if "pink" in s or "rose" in s :
        c += 1

if c != 0:
    print(c)
else:
    print("I must watch Star Wars with my daughter")