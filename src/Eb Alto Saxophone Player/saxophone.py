import sys

file = sys.stdin.read()
liste = file.splitlines()

test = int(liste[0])

dic = [("c", [2,3,4,7,8,9,10]), ("d", [2,3,4,7,8,9]), ("e", [2,3,4,7,8]), ("f", [2,3,4,7]),
       ("g", [2,3,4]), ("a", [2,3]), ("b", [2]), ("C", [3]), ("D", [1,2,3,4,7,8,9]),
       ("E", [1,2,3,4,7,8]), ("F",[1,2,3,4,7]), ("G", [1,2,3,4]), ("A", [1,2,3]), ("B", [1,2])]
dico = dict(dic)
res = []

for i in range(1, test + 1):
    finger = [0] * 10
    if liste[i] == " ":
        res.append(finger)
    else:
        memory = []
        for letter in liste[i]:
            l = dico[letter]
            for j in range(1, 11):
                if j in l and j not in memory:
                    finger[j - 1] +=1
            memory = l
        res.append(finger)

for elt in res:
    for i in range(len(elt) - 1):
        print(elt[i], end=" ")
    print(elt[len(elt) - 1])