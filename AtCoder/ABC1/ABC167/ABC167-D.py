n,k = map(int,input().split())
a = list(map(lambda x: int(x)-1,input().split()))
towns = [0]
added = [-1] * n
added[0] = 0
for i in range(1,k+1):
    tmp = a[towns[-1]]
    pl = added[tmp]
    if pl != -1:
        loop = towns[pl:]
        last = (k-pl) % len(loop)
        print(loop[last]+1)
        exit()
    else:
        added[tmp] = i
        towns.append(tmp)
print(towns[-1]+1)
