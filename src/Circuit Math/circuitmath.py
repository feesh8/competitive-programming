def f(l):
    L = []
    for elt in l:
        if elt == 'F':
            L.append(False)
        else:
            L.append(True)
    return L

n = int(input())
lst = f(input().split())
S = input().split()

operations = ['*', '+', '-']

var = []
op = []

for elt in S:
    if elt in operations:
        op.append(elt)
    else:
        var.append(lst[ord(elt) - 65])
        
var.reverse()
op.reverse()
        
while len(op) != 0:
    ope = op.pop()
    if ope == '*':
        var.append(var.pop() and var.pop())
    elif ope == '+':
        var.append(var.pop() or var.pop())
    else:
        var.append(not var.pop())

res = var.pop()

if res:
    print('T')
else:
    print('F')