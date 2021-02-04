d, g = map(int, input().split())
p = []
c = []
for _ in range(d):
    px, cx = map(int, input().split()) 
    p.append(px)
    c.append(cx)

ans = 2<<9

for m in range(1<<d):
    s = 0
    num = 0
    rest_max = -1
    for i in range(d):
        if m>>i & 1:
            s += 100 * (i+1) * p[i] + c[i]
            num += p[i]
        else:
            rest_max = i
    if s < g:
        s1 = 100 * (rest_max + 1)
        need = (g - s + s1 - 1) // s1
        if need >= p[rest_max]:
            continue
        num += need
    ans = min(ans, num)
print(ans)
