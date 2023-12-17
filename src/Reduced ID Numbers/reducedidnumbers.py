import sys

def test_distinct(li):
    return len(set(li)) == len(li)

file = sys.stdin.read()
liste = file.splitlines()

G = int(liste[0])
test = 1
l = []

for i in range(1, G + 1):
    l.append(int(liste[i]) % 1)

if test_distinct(l):
    print(test)

else:
    while not test_distinct(l):
        for i in range(1, G + 1):
            l[i - 1] = int(liste[i]) % test
        test += 1
    
    print(test - 1)
    