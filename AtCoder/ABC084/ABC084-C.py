n = int(input())

c = []
s = []
f = []

for _ in range(n-1):
    ce,se,fe = map(int, input().split())
    c.append(ce)
    s.append(se)
    f.append(fe)

for i in range(n-1):
    min = 0
    for j in range(i,n-1):
        if min <= s[j]:
            min = s[j] + c[j]
        else:
            md = min % f[j]
            if md != 0: md = f[j] - md
            min += md + c[j]
    print(min)
print(0)
