from math import factorial
# cmb = nが大きなときに有効。そうでないときは遅くなる可能性を考慮する。
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

x, y = map(int, input().split())
if x < y:
    tmp = y
    y = x
    x = tmp
plus = x + y
if plus % 3 != 0 or x / y > 2:
    print(0)
    exit()

n = int(plus / 3)

center = int(plus / 2)
dist = center - y
pos = int(n / 2) - dist

div = 10**9 + 7


print(int(cmb(n,pos) % div))

