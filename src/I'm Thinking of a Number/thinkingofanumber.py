def TrouveNb2(a, b, div):
    if b == 50001:
        return "infinite"
    else:
        res = []
        if div:
            m = max(div)
            div.remove(max(div))
            if a % m != 0:
                a += (m - (a % m))
            for i in range(a, b, m):
                res.append(i)
            for d in div:
                j = 0
                while j < len(res):
                    if res[j] % d != 0:
                        res.remove(res[j])
                    else:
                        j += 1
        else:
            res = [i for i in range(a, b)]
            
        if res:
            return " ".join(map(str, res))
        else:
            return "none"

n = int(input())
resultat =""
while n != 0:
    div = []
    a = 1
    b = 50001
    for _ in range(n):
        line = input().split()
        if line[:2] == ["less", "than"]:
            b = min(b,int(line[2]))
        elif line[:2] == ["greater", "than"]:
            a = max(a,int(line[2]) + 1)
        elif line[:2] == ["divisible", "by"]:
            div.append(int(line[2]))
    resultat += TrouveNb2(a, b, div) + "\n"
    n = int(input())

print(resultat)
