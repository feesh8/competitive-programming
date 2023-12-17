import sys

file = sys.stdin.read()
liste = file.splitlines()
r, n = liste[0].split()
r, n = int(r), int(n)

if r == n:
    print("too late")
else:
    for i in range(1, r + 1):
        if str(i) not in liste:
            print(i)
            break