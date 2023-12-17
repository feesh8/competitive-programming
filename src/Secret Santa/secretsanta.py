from math import factorial, exp

n = input()
n = int(n)
res = 1/factorial(1)
if n > 100:
    res = 1 - (1 / exp(1))
else:
    for i in range(2, n + 1):
        res += (-1)**(i + 1) / factorial(i)
print(res)