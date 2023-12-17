n, m = input().split()
n, m = int(n), int(m)

def expo_rap(x, n):
	"""Renvoie x^n par exponentiation rapide"""
	if n == 0:
		return 1
	y = expo_rap(x, n // 2) % m
	if n % 2 == 0:
		return (y * y) % m
	else:
		return (x * y * y) % m

res = 0

if n == 0: 
    res = 2 % m
elif n == 1:
    res = 4 % m
else:
    res = (5 * expo_rap(2, n - 1) - 1) % m
    
print(res)