n, m = map(int, input().split())
bridge = [list(map(int, input().split())) for _ in range(m)]
for ii in range(m):
    islands = [[x+1] for x in range(n)]
    for b in bridge[ii+1:]:
        for i in islands:
            if b[0] in i:
                if b[1] in i:
                    break
                else:
                    for j in islands:
                        if b[1] in j:
                            i.extend(j)
                            islands.remove(j)
    huben = 0
    for x in islands:
        huben += len(x) * (n - len(x))

    print(int(huben / 2))
