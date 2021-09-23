import copy, time
n = int(input())
start = time.time()
divs = [{}] * (n + 1)
ans = 1
prime = []
for i in range(2,n+1):
    if divs[i] == {}:
        ans += 2 * i
        divs[i] = {i:1}
        prime.append(i)
    else:
        tmp = 1
        for v in divs[i].values():
            tmp *= (v+1)
        ans += tmp * i

    for p in prime:
        v = i * p
        if v > n: break
        if divs[v] != {}: continue
        divs[v] = copy.deepcopy(divs[i])
        if p in divs[v]:
            divs[v][p] += 1
        else:
            divs[v][p] = 1

print(f"{n}:{time.time()-start}")
for d in divs:
    print(d)
print(ans)
print("")
