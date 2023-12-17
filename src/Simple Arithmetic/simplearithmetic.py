from decimal import Decimal
ent = input()
a, b, c = ent.split()
a, b, c = Decimal(int(a)), Decimal(int(b)), Decimal(int(c))
if c == 1:
    print(a * b)
else:
    print(a * b / c)