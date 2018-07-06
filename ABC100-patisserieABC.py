n, m = map(int, input().split())
cakes = []
ans = 0
for i in range(n): cakes.append(list(map(int, input().split())))
for x in [1, -1]:
    for y in [1, -1]:
        for z in [1, -1]:
            tmp = []
            tmpans = 0
            for cake in cakes: tmp.append(x * cake[0] + y * cake[1] + z * cake[2])
            tmp.sort(reverse = True)
            for i in range(m): tmpans += tmp[i]
            ans = max(ans, tmpans)
print(ans)
