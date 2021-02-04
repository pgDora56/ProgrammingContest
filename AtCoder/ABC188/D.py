n, prime = map(int,input().split())
dic = {}
for _ in range(n):
    a, b, c = map(int,input().split())
    if a in dic:
        dic[a] += c
    else:
        dic[a] = c
    if b+1 in dic:
        dic[b+1] -= c
    else:
        dic[b+1] = -c

changes = sorted(dic.items(), key=lambda x:x[0])
d = 0
val = 0
total = 0
for d2, cval in changes:
    total += (d2-d)*min(val,prime)
    val += cval
    d = d2

print(total)
