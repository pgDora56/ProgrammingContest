from math import sqrt
n = int(input())
x = list(map(lambda x: abs(int(x)), input().split()))
mh = 0
euc = 0
ch = 0
for v in x:
    mh += v
    euc += v*v
    ch = max(ch, v)
euc = sqrt(euc)

print(mh)
print(euc)
print(ch)
